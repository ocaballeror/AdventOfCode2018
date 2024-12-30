Bot = Struct.new(:x, :y, :z, :range)


class Cube
  attr_reader :minx
  attr_reader :maxx
  attr_reader :miny
  attr_reader :maxy
  attr_reader :minz
  attr_reader :maxz

  def initialize(minx, maxx, miny, maxy, minz, maxz)
    @minx = minx
    @maxx = maxx
    @miny = miny
    @maxy = maxy
    @minz = minz
    @maxz = maxz
  end

  def to_s
    "Cube((#{@minx}, #{@maxx}), (#{@miny}, #{@maxy}), (#{@minz}, #{@maxz}))"
  end

  def manhattan
    total = 0
    total += [@minx.abs, @maxx.abs].min if @minx > 0 || @maxx < 0
    total += [@miny.abs, @maxy.abs].min if @miny > 0 || @maxy < 0
    total += [@minz.abs, @maxz.abs].min if @minz > 0 || @maxz < 0

    total
  end

  def splitat(coord)
    if coord == :x    
      first = @minx, (@maxx + @minx) / 2, @miny, @maxy, @minz, @maxz
      second = (@maxx + @minx) / 2 + 1, @maxx, @miny, @maxy, @minz, @maxz
    elsif coord == :y
      first = @minx, @maxx, @miny, (@maxy + @miny) / 2, @minz, @maxz
      second = @minx, @maxx, (@maxy + @miny) / 2 + 1, @maxy, @minz, @maxz
    else coord == :z
      first = @minx, @maxx, @miny, @maxy, @minz, (@maxz + @minz) / 2
      second = @minx, @maxx, @miny, @maxy, (@maxz + @minz) / 2 + 1, @maxz
    end

    [first, second]
  end
end

def bot_distance(bot1, bot2)
	(bot1.x - bot2.x).abs +
	(bot1.y - bot2.y).abs +
	(bot1.z - bot2.z).abs
end

def bot_in_range(bot1, bot2)
	bot_distance(bot1, bot2) <= bot1.range
end

def bots_in_cube(nanobots, cube)
    count = 0
    nanobots.each do |bot|
      range = bot.range
      range -= [(bot.x - cube.minx).abs, (bot.x - cube.maxx).abs].min if bot.x < cube.minx || bot.x > cube.maxx
      range -= [(bot.y - cube.miny).abs, (bot.y - cube.maxy).abs].min if bot.y < cube.miny || bot.y > cube.maxy
      range -= [(bot.z - cube.minz).abs, (bot.z - cube.maxz).abs].min if bot.z < cube.minz || bot.z > cube.maxz

      count += 1 unless range < 0
    end

    count
end

nanobots = []
open("input") do |file|
	file.each do |line|
		match = line.match(/pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)$/)
		match = match.captures.map { |x| x.to_i }
		nanobots << Bot.new(match[0], match[1], match[2], match[3])
	end
end
puts("read #{nanobots.size} bots")

biggest = nanobots.max_by { |bot| bot.range }
puts(nanobots.select { |bot| bot_in_range(biggest, bot) }.size)


minx = nanobots.map { |bot| bot.x - bot.range }.min
miny = nanobots.map { |bot| bot.y - bot.range }.min
minz = nanobots.map { |bot| bot.z - bot.range }.min
maxx = nanobots.map { |bot| bot.x + bot.range }.max
maxy = nanobots.map { |bot| bot.y + bot.range }.max
maxz = nanobots.map { |bot| bot.z + bot.range }.max

cube = Cube.new(minx, maxx, miny, maxy, minz, maxz)

loop do
  if cube.minx < cube.maxx
    first, second = cube.splitat(:x)
  elsif cube.miny < cube.maxy
    first, second = cube.splitat(:y)
  elsif cube.minz < cube.maxz
    first, second = cube.splitat(:z)
  else
    fail unless cube.maxx == cube.minx and cube.maxy == cube.miny and cube.maxz == cube.minz
    break
  end

  first = Cube.new(*first)
  second = Cube.new(*second)
  if bots_in_cube(nanobots, first) > bots_in_cube(nanobots, second)
    cube = first
  elsif bots_in_cube(nanobots, first) < bots_in_cube(nanobots, second)
    cube = second
  else
    cube = [first, second].min_by &:manhattan
  end
end

puts cube.manhattan
