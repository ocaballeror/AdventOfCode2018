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
      for x in (0...line.size)
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


def adjacent(coord, maxx, maxy)
  points = []
  for direction in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    move = coord + Point.new(direction[0], direction[1])
    if move.x >= 0 and move.x < maxx and move.y >= 0 and move.y < maxy
      points << move
    end
  end
  points
end


def tick(blocks, maxx, maxy)
  trees = Set.new
  lumber = Set.new
  clear = Set.new
  for x in (0..maxx + 1)
    for y in (0..maxy + 1)
      coord = Point.new(x, y)
      lumbercount = treecount = 0
      for c in adjacent(coord, maxx, maxy)
        if blocks.lumber.include?(c)
          lumbercount += 1
        elsif blocks.trees.include?(c)
          treecount += 1
        end
      end
      if blocks.clear.include?(coord)
        if treecount >= 3
          trees << coord
        else
          clear << coord
        end
      elsif blocks.trees.include?(coord)
        if lumbercount >= 3
          lumber << coord
        else
          trees << coord
        end
      elsif blocks.lumber.include?(coord)
        if lumbercount >= 1 and treecount >= 1
          lumber << coord
        else
          clear << coord
        end
      end
    end
  end
  Blocks.new(trees, lumber, clear)
end
