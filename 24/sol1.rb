require_relative 'common'

immune, infection = read_input
winner = battle(immune, infection)
winner = winner == 'infection' ? infection : immune
units = winner.reduce(0) { |acc, g| acc + g.units }
puts "Remaining units: #{units}"
