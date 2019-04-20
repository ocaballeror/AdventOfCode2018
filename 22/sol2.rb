require 'set'

ROCKY = 0
WET = 1
NARROW = 2

NEITHER = 0
CLIMBING = 1
TORCH = 2


open("input") do |file|
  line = file.gets
  $depth = line.split(":")[1].strip.to_i
  line = file.gets
  $target = line.split(":")[1].strip.split(",")
  $target = $target.map { |t| t.to_i }
end


def geologic_index(x, y, indexes)
  if x == 0 and y == 0
    0
  elsif [x, y] == $target
    0
  elsif x == 0
    (y * 48271)
  elsif y == 0
    (x * 16807)
  else
    indexes[y][x-1] * indexes[y-1][x]
  end
end


def adjacent(point)
  [[-1, 0], [0, -1], [1, 0], [0, 1]].map {
    |move| [point[0] + move[0], point[1] + move[1]] }.select {
    |p| $types.include?(p) and p[0] >= 0 and p[1] >= 0 }
end


def get_distance(point, other, tool)
  point_type = $types[point]
  other_type = $types[other]
  return 1, tool if point_type == other_type

  tools = {
    [ROCKY, WET] => CLIMBING,
    [ROCKY, NARROW] => TORCH,
    [WET, NARROW] => NEITHER,
  }
  proper_tool = tools[[point_type, other_type]]
  if proper_tool.nil?
    proper_tool = tools[[other_type, point_type]]
  end
  if proper_tool == tool
    return 1, tool
  else
    return 8, proper_tool
  end
end


# TODO prune if a path has been found and is shorter
# TODO end if we already found a path?
# TODO Use a heap?
# TODO Carry the path around
#
#

def dijkstra(origin, target)
  to_visit = [[origin, 0, [], TORCH]]
  distances = {origin => [0, []]}
  seen = Set.new
  until to_visit.empty?
    # node = to_visit.min_by {|x| x[1]}
    node = to_visit.min_by {|x| x[1]}
    position, distance, tool = node
    # break if distances.include?(target) and distance > distances[target][0]
    to_visit.delete(node)
    adjacent(position).each do |neighbor|
      time, newtool = get_distance(position, neighbor, tool)
      time += distance
      time += 7 if neighbor == target and newtool != TORCH
      known = distances[neighbor]
      if known.nil? or time < known[0]
        distances[neighbor] = time, position
      end
      if !seen.include?(neighbor)
        if !to_visit.any? { |field| neighbor == field[0] }
          to_visit << [neighbor, time, newtool]
        end
      end
    end
    seen << position
  end
  # distances[target]
  distances
end

def shortest_path(origin, target)
  distances = dijkstra(origin, target)
  puts(distances.to_s)
  ret = []
  t = distances[target][1]
  while t != origin
    ret << t
    t = distances[t][1]
  end
  return distances[target], ret.reverse + [target]
end


def print_thing(path)
  tool = TORCH
  last = [0, 0]
  d = 0
  path.each do |point|
    distance, tool = get_distance(last, point, tool)
    d += distance
    puts("#{d} #{point[0]} #{point[1]}")
    last = point
  end
end



indexes = []
$types = {}
answer = 0
(0..$target[1] + 7).each do |y|
  indexes[y] = [0] * $target[1]
  (0..$target[0] + 7).each do |x|
    index = geologic_index(x, y, indexes)
    index = (index + $depth) % 20183
    indexes[y][x] = index
    type = index % 3
    $types[[x, y]] = type
    answer += type
  end
end

print_thing(shortest_path([0, 0], $target)[1])
