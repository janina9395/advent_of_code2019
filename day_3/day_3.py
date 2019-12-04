class HorizontalVector:
    def __init__(self, x1, x2, y, dist_from_start, reverted):
        self.x1 = x1
        self.x2 = x2
        self.y = y
        self.dist_from_start = dist_from_start
        self.reverted = reverted

    def intersects(self, other):
        return other.y1 < self.y < other.y2 and self.x1 < other.x < self.x2

    def intersection(self, other):
        return Point(other.x, self.y)

    def dist(self, p):
        if self.reverted:
            return abs(self.x2 - p.x)
        return abs(p.x - self.x1)

    def __str__(self):
        return "({0}, {1})->({2}, {3}), dist_from_start = {4}".format(self.x1, self.y, self.x2, self.y, self.dist_from_start)

    def __repr__(self):
        return str(self)

class VerticalVector:
    def __init__(self, x, y1, y2, dist_from_start, reverted):
        self.x = x
        self.y1 = y1
        self.y2 = y2
        self.dist_from_start = dist_from_start
        self.reverted = reverted

    def intersects(self, other):
        return other.x1 < self.x < other.x2 and self.y1 < other.y < self.y2

    def intersection(self, other):
        return Point(self.x, other.y)

    def dist(self, p):
        if self.reverted:
            return abs(self.y2 - p.y)
        return abs(p.y - self.y1)

    def __str__(self):
        return "({0}, {1})->({2}, {3}), distance = {4}".format(self.x, self.y1, self.x, self.y2, self.dist_from_start)

    def __repr__(self):
        return str(self)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return str(self)

def build_path(codes):
    verticals = []
    horizontals = []
    cur = Point(0, 0)
    total_dist = 0
    for code in codes:
        direction = code[0]
        step = int(code[1:])
        if direction == 'R':
            next = Point(cur.x + step, cur.y)
            i = HorizontalVector(cur.x, cur.x + step, cur.y, total_dist, False)
            horizontals.append(i)
            # print(i)
        elif direction == 'L':
            next = Point(cur.x - step, cur.y)
            i = HorizontalVector(cur.x - step, cur.x, cur.y, total_dist, True)
            horizontals.append(i)
            # print(i)
        elif direction == 'U':
            next = Point(cur.x, cur.y + step)
            i = VerticalVector(cur.x, cur.y, cur.y + step, total_dist, False)
            verticals.append(i)
            # print(i)
        elif direction == 'D':
            next = Point(cur.x, cur.y - step)
            i = VerticalVector(cur.x, cur.y - step, cur.y, total_dist, True)
            verticals.append(i)
            # print(i)
        cur = next
        total_dist = total_dist + step
    return horizontals, verticals

def find_closest_intersection(c1, c2):
    h1, v1 = build_path(c1)
    h2, v2 = build_path(c2)
    dist = []
    for h in h1:
        for v in v2:
            if h.intersects(v):
                i = h.intersection(v)
                if i.x != 0 and i.y != 0:
                    dist.append(abs(i.x) + abs(i.y))

    for h in h2:
        for v in v1:
            if h.intersects(v):
                i = h.intersection(v)
                if i.x != 0 and i.y != 0:
                    dist.append(abs(i.x) + abs(i.y))

    return min(dist)

def find_closest_intersection_by_steps(c1, c2):
    h1, v1 = build_path(c1)
    h2, v2 = build_path(c2)
    dist = []
    for h in h1:
        for v in v2:
            if h.intersects(v):
                i = h.intersection(v)
                if i.x != 0 and i.y != 0:
                    dist.append(h.dist_from_start + h.dist(i) + v.dist_from_start + v.dist(i))

    for h in h2:
        for v in v1:
            if h.intersects(v):
                i = h.intersection(v)
                if i.x != 0 and i.y != 0:
                    dist.append(h.dist_from_start + h.dist(i) + v.dist_from_start + v.dist(i))

    return min(dist)

# input1
def read_file(name):
    f = open(name, "r")
    lines = f.readlines()
    c1 = lines[0].rstrip('\n').split(',')
    c2 = lines[1].rstrip('\n').split(',')
    print(c1)
    print(c2)
    f.close()
    return c1, c2

# part 1
print(find_closest_intersection(['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']))
print(find_closest_intersection(*read_file("input1")))
print(find_closest_intersection(*read_file("input2")))
print(find_closest_intersection(*read_file("input_main")))


# part 2
print(find_closest_intersection_by_steps(['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']))
print(find_closest_intersection_by_steps(*read_file("input1")))
print(find_closest_intersection_by_steps(*read_file("input2")))
print(find_closest_intersection_by_steps(*read_file("input_main")))
