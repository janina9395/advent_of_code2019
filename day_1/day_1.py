def calc_fuel(mass):
    return int((mass / 3)) - 2

assert(calc_fuel(12) == 2)
assert(calc_fuel(14) == 2)
assert(calc_fuel(1969) == 654)
assert(calc_fuel(100756) == 33583)

def calc_total(func):
    f = open("input", "r")
    lines = map(int, f.readlines())
    res = sum(map(func, lines))
    f.close()
    return res

print("Sum is", calc_total(calc_fuel))

# part 2
def fuel_for_fuel(mass):
    fuel = calc_fuel(mass)
    total = 0
    total += fuel
    while fuel > 0:
        add = calc_fuel(fuel)
        if add > 0:
            total += add
        fuel = add
    return total

assert(fuel_for_fuel(14) == 2)
assert(fuel_for_fuel(1969) == 966)
assert(fuel_for_fuel(100756) == 50346)

print("Total sum is", calc_total(fuel_for_fuel))
