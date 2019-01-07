require './common.rb'

blocks = read_input
all_blocks = blocks.trees | blocks.lumber | blocks.clear
maxx = all_blocks.max_by { |b| b.x }.x + 1
maxy = all_blocks.max_by { |b| b.y }.y + 1
puts("Maxx: #{maxx}, Maxy: #{maxy}")

# Simulate 10 minutes on the initial forest and print out the result
10.times do
  blocks = tick(blocks, maxx, maxy)
end
res = blocks.trees.size * blocks.lumber.size
puts("#{blocks.trees.size} * #{blocks.lumber.size} = #{res}")
