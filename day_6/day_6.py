def read_file(name):
    f = open(name, "r")
    lines = f.readlines()
    res = {}
    for l in lines:
        orbits = l.rstrip('\n').split(")")
        if orbits[1] in res.keys():
            res[orbits[1]].append(orbits[0])
        else:
            res[orbits[1]] = [orbits[0]]
    f.close()
    return res


# return tuples (source, destination, distance)
def find_all_orbits(from_orbit, dir_orbits):
    all_orbits = set()
    orbits = [from_orbit]
    count = 0
    while len(orbits) > 0:
        orbit = orbits.pop()
        next_orbits = dir_orbits.get(orbit, [])

        for next_orbit in next_orbits:
            all_orbits.add((from_orbit, next_orbit, count))
            orbits.append(next_orbit)
            count += 1
    return all_orbits


def count_orbits(file):
    dir_orbits = read_file(file)

    all_orbits = set()
    for orbit in dir_orbits.keys():
        all_orbits.update(find_all_orbits(orbit, dir_orbits))

    return len(all_orbits)


def found_shortest_path(from_orbit, to, file):
    dir_orbits = read_file(file)
    orbits1 = find_all_orbits(from_orbit, dir_orbits)
    orbits2 = find_all_orbits(to, dir_orbits)

    paths = []
    for o1 in orbits1:
        for o2 in orbits2:
            (from1, to1, dist1) = o1
            (from2, to2, dist2) = o2
            if to1 == to2:
                paths.append(dist1 + dist2)

    return min(paths)


assert(count_orbits("test") == 42)
print(count_orbits("input"))

assert(found_shortest_path("YOU", "SAN", "test2") == 4)
print(found_shortest_path("YOU", "SAN", "input2"))