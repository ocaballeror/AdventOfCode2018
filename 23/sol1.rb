Bot = Struct.new(:x, :y, :z, :range)

def distance(bot1, bot2)
	(bot1.x - bot2.x).abs +
	(bot1.y - bot2.y).abs +
	(bot1.z - bot2.z).abs
end

def in_range(bot1, bot2)
	distance(bot1, bot2) <= bot1.range
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
puts(nanobots.select { |bot| in_range(biggest, bot) }.size)
