require 'set'

ROCKY = 0
WET = 1
NARROW = 2

NEITHER = 3
CLIMBING = 4
TORCH = 5

TOOLS = {
  ROCKY => [CLIMBING, TORCH],
  NARROW => [TORCH, NEITHER],
  WET => [NEITHER, CLIMBING],
}


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

def move_choices(point, other, tool)
  current_type = $types[point]
  other_type = $types[other]
  tool_choices = TOOLS[other_type]

  choices = []
  if tool_choices.include? tool
    choices << [1, tool]
  else
    tool_choices.each do |t|
      next if !TOOLS[current_type].include? t
      choices << [8, t]
    end
  end
  choices
end


def dijkstra(origin, target)
  to_visit = [[origin, 0, TORCH]]
  distances = Hash.new(Float::INFINITY)
  best = Float::INFINITY
  chunk = []
  until to_visit.empty? and chunk.empty?
    to_visit.sort_by! { |x| x[1] }
    chunk = to_visit.shift(300)
    print "Best: #{best}, Remaining: #{to_visit.size + chunk.size}    \r"

    chunk.each do |position, distance, tool|
      adjacent(position).each do |neighbor|
        move_choices(position, neighbor, tool).each do |time, newtool|
          time += distance
          next if time > best
          next if time >= distances[[newtool, neighbor]]
          if neighbor == target
            time += 7 if newtool != TORCH
            best = time if time < best
            next
          end

          distances[[newtool, neighbor]] = time
          to_visit << [neighbor, time, newtool]
        end
      end
    end
  end
  puts
  best
end


indexes = []
$types = {}
answer = 0
(0..$target[1] + 30).each do |y|
  indexes[y] = [0] * $target[1]
  (0..$target[0] + 30).each do |x|
    index = geologic_index(x, y, indexes)
    index = (index + $depth) % 20183
    indexes[y][x] = index
    type = index % 3
    $types[[x, y]] = type
    answer += type
  end
end

sol = dijkstra([0, 0], $target)
puts "Shortest distance: #{sol}"
