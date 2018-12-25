def manhattan(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


all_points = []
with open('input') as f:
    for line in f:
        all_points.append(tuple(map(int, line.split(','))))

start_x = min(all_points, key=lambda x: x[0])[0]
end_x = max(all_points, key=lambda x: x[0])[0]
start_y = min(all_points, key=lambda x: x[1])[1]
end_y = max(all_points, key=lambda x: x[1])[1]
