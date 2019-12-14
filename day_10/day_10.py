import math


def read_file(file):
    points = set()
    with open(file) as fp:
        row = 0
        line = fp.readline()
        while line:
            for col in range(0, len(line)):
                if line[col] == '#':
                    points.add((row, col))
            line = fp.readline()
            row += 1
    fp.close()
    return points


def sight(p1, p0):
    x1, y1 = p1
    x0, y0 = p0
    dx, dy = x1 - x0, y1 - y0
    gcd = math.gcd(dx, dy)
    return dx // gcd, dy // gcd


def count_visible_asteroids(from_point, all_points):
    all_sights = set()
    for point in all_points:
        if point != from_point:
            all_sights.add(sight(point, from_point))
    return len(all_sights)


def count_max_asteroids(file):
    all_points = read_file(file)
    counts = [count_visible_asteroids(p, all_points) for p in all_points]
    return max(counts)


assert(count_max_asteroids("test_input") == 8)
assert(count_max_asteroids("test_input2") == 33)
assert(count_max_asteroids("test_input3") == 35)
assert(count_max_asteroids("test_input4") == 41)
assert(count_max_asteroids("test_input5") == 210)

print(count_max_asteroids("input"))


