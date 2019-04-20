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


indexes = []
answer = 0
(0..$target[1]).each do |y|
  indexes[y] = []
  (0..$target[0]).each do |x|
    index = geologic_index(x, y, indexes)
    index = (index + $depth) % 20183
    indexes[y] << index
    answer += index % 3
  end
end

puts(answer)
