require 'set'


Blocks = Struct.new(:trees, :lumber, :clear)

class Point
  attr_reader :x
  attr_reader :y

  def initialize(x, y)
    @x = x
    @y = y
  end

  def +(other)
    Point.new(@x + other.x, @y + other.y)
  end

  def eql?(other)
    @x == other.x and @y == other.y
  end

  def to_s
    "(#{@x}, #{@y})"
  end

  def inspect
    to_s
  end

  def hash
    to_s.hash
  end
end


def read_input
  trees = Set.new
  lumber = Set.new
  clear = Set.new
  open("input") do |file|
    file.each_with_index do |line, y|
      (0...line.size).each do |x|
        point = Point.new(x, y)
        block = line[x]
        if block == '.'
          clear << point
        elsif block == '|'
          trees << point
        elsif block == '#'
          lumber << point
        end
      end
    end
  end
  Blocks.new(trees, lumber, clear)
end


# Return the list of points that are adjacent to this coord and are inside the
# height and width constraints
def adjacent(coord, maxx, maxy)
  moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1],
            [0, 1], [1, -1], [1, 0], [1, 1]]
  moves.collect { |d| coord + Point.new(d[0], d[1]) }.
         select { |p| p.x >= 0 and p.x < maxx and p.y >= 0 and p.y < maxy }
end


# Calculate the transformations that will occur in one minute to the given set
# of blocks and return the new state of the forest
def tick(blocks, maxx, maxy)
  trees = Set.new
  lumber = Set.new
  clear = Set.new
  (0..maxx + 1).each do |x|
    (0..maxy + 1).each do |y|
      coord = Point.new(x, y)
      lumbercount = treecount = 0
      adjacent(coord, maxx, maxy).each do |c|
        lumbercount += 1 if blocks.lumber.include?(c)
        treecount += 1 if blocks.trees.include?(c)
      end
      newtype = clear
      if blocks.clear.include?(coord)
        newtype = trees if treecount >= 3
      elsif blocks.trees.include?(coord)
        newtype = (lumbercount >= 3? lumber : trees)
      elsif blocks.lumber.include?(coord)
        newtype = lumber if lumbercount >= 1 and treecount >= 1
      else
        next
      end
      newtype << coord
    end
  end
  Blocks.new(trees, lumber, clear)
end
