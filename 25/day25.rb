require 'set'

input = IO.read 'input'

$allstars = Set.new
input.lines.map(&:strip).each do |line|
  next if line.empty?

  coords = line.split(',').map(&:to_i)
  $allstars << coords
end


def manhattan(one, other)
    x, y, z, t = one
    ox, oy, oz, ot = other

    (ox - x).abs + (oy - y).abs + (oz - z).abs + (ot - t).abs
end

def explore(star, acc)
  ($allstars - acc).each do |other|
    if manhattan(star, other) <= 3
      acc << other
      explore(other, acc)
    end
  end
end


count = 0

until $allstars.empty?
  star = $allstars.first
  $allstars.subtract(star)

  constellation = Set.new [star]
  explore(star, constellation)
  count += 1
  $allstars -= constellation
end

puts count
