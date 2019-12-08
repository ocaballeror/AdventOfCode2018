# Defines a group in an army
class Group
  attr_accessor :units, :hp, :weak, :immune, :attack, :attack_type, :initiative, :army, :number

  def initialize
    @units = 0
    @hp = 0
    @weak = []
    @immune = []
    @attack = 0
    @attack_type = nil
    @initiative = 0
    @army = nil
    @number = 0
  end

  def empty?
    @units.zero?
  end

  def power
    @units * @attack
  end

  def name
    "#{army.capitalize} group #{number}"
  end

  def damage(other)
    if other.immune.include? @attack_type
      0
    elsif other.weak.include? @attack_type
      power * 2
    else
      power
    end
  end

  def attack!(other)
    killed = (damage(other) / other.hp)
    killed = other.units if killed > other.units
    other.units -= killed
    killed
  end
end

def read_input
  input = IO.read('input')

  immune = []
  infection = []
  current_army = nil
  properties = {
    /(\d+) units/ => 'units',
    /(\d+) hit points/ => 'hp',
    /weak to (([a-z]+(, )?)+)/ => 'weak',
    /immune to (([a-z]+(, )?)+)/ => 'immune',
    /attack that does (\d+)/ => 'attack',
    /\d+ ([a-z]+) damage/ => 'attack_type',
    /at initiative (\d+)/ => 'initiative'
  }
  input.lines.each do |line|
    line = line.strip
    next if line.empty?

    if line == 'Immune System:'
      current_army = immune
      next
    elsif line == 'Infection:'
      current_army = infection
      next
    end

    group = Group.new
    properties.each_pair do |regex, attr|
      match = regex.match line
      next if match.nil?

      capture = match.captures[0]
      type = group.instance_variable_get("@#{attr}").class
      if type == Array
        capture = capture.split(',').map(&:strip)
      elsif type == Integer
        capture = capture.to_i
      end
      group.instance_variable_set("@#{attr}", capture)
    end
    group.army = current_army.equal?(infection) ? 'infection' : 'immune'
    group.number = current_army.size + 1
    current_army << group
  end
  return immune, infection
end

def select_targets(immune, infection)
  all_groups = (immune + infection).sort_by { |g| [g.power, g.initiative] }
  attacks = {}
  immune_targets = immune.clone
  infection_targets = infection.clone
  all_groups.reverse.each do |group|
    targets = group.army == 'immune' ? infection_targets : immune_targets
    next if targets.empty?

    pick = targets.max_by { |t| [group.damage(t), t.power, t.initiative] }
    next if group.damage(pick).zero?

    attacks[group] = pick
    targets.delete pick
  end
  attacks
end

def attack(attacks)
  dead = []
  total_killed = 0
  attacks = attacks.to_a.sort_by { |at| at[0].initiative }.reverse
  attacks.to_a.each do |attacker, defender|
    killed = attacker.attack! defender
    total_killed += killed

    if defender.units <= 0
      attacks.delete defender
      dead << defender
    end
  end
  [dead, total_killed]
end

def battle(immune, infection)
  until immune.empty? or infection.empty?
    attacks = select_targets(immune, infection)
    dead, killed = attack attacks
    break if killed.zero?

    dead.each do |group|
      army = group.army == 'immune' ? immune : infection
      army.delete group
    end
  end
  if immune.empty?
    'infection'
  elsif infection.empty?
    'immune'
  else
    'stalemate'
  end
end
