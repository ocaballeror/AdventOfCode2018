require 'set'
require './common.rb'


MAX = 1000000000
blocks = read_input
all_blocks = blocks.trees | blocks.lumber | blocks.clear
maxx = all_blocks.max_by { |b| b.x }.x + 1
maxy = all_blocks.max_by { |b| b.y }.y + 1

seen = Set.new
pattern = []
recording = false
for minute in (1...MAX)
  blocks = tick(blocks, maxx, maxy)
  res = blocks.trees.size * blocks.lumber.size
  if seen.include?(res)
    if !recording
      recording = true
      pattern = [res]
    else
      if res == pattern[0]
        target = (MAX - minute) % pattern.size
        puts(pattern[target])
        break
      else
        pattern << res
      end
    end
  else
    recording = false
  end
  puts("#{res.to_s} #{seen.include?(res)}")
  seen << res
end
