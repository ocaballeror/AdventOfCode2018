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

# We'll keep simulating until we find a pattern of repeating results
(1...MAX).each do |minute|
  blocks = tick(blocks, maxx, maxy)
  res = blocks.trees.size * blocks.lumber.size
  if seen.include?(res)
    if !recording
      # If we've already seen this result, start recording until we get to it again
      recording = true
      pattern = [res]
    else
      if res == pattern[0]
        # We've come full circle and found the same result as when we started
        # recording. We have the pattern of repeating results in the `pattern`
        # array, so we can just calculate where we'll be at minute `MAX`
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
