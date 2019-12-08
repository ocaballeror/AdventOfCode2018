require_relative 'common'


def simulate(immune, infection)
  immune_initial = immune
  infection_initial = infection
  boost = -1
  winner = 'infection'
  until winner == 'immune'
    immune = immune_initial.map(&:clone)
    infection = infection_initial.map(&:clone)
    boost += 1
    immune.each { |g| g.attack += boost }
    winner = battle(immune, infection)
    puts "Winner: #{winner}, Boost: #{boost}"
  end
  units = immune.reduce(0) { |acc, g| acc + g.units }
  [boost, units]
end

immune, infection = read_input
boost, units = simulate(immune, infection)
puts "Remaining units: #{units}"
puts "Minimum boost: #{boost}"
