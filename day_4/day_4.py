def to_digits(n):
    return list(map(int, list(str(n))))

def check_number(n):
    digits = to_digits(n)
    prev = digits[0]
    rest = digits[1:]

    double = False
    increasing = True
    for next in rest:
        if next < prev:
            increasing = False
            break
        if prev == next:
            double = True
        prev = next
    return double and increasing

def check_number_part2(n):
    digits = to_digits(n)
    prev = digits[0]
    rest = digits[1:]

    increasing = True
    counters = {}
    for next in rest:
        if next < prev:
            increasing = False
            break
        if prev == next:
            counters[prev] = counters.get(prev, 1) + 1
        prev = next

    # print(counters)
    return increasing and 2 in counters.values()

assert(check_number(122345) == True)
assert(check_number(111111) == True)
assert(check_number(223450) == False)
assert(check_number(123789) == False)

def count_matches(match_func):
    count = 0
    for n in range(193651, 649729):
        if match_func(n):
            count += 1
    return count

print("Part 1:", count_matches(check_number))

assert(check_number_part2(122345) == True)
assert(check_number_part2(111111) == False)
assert(check_number_part2(223450) == False)
assert(check_number_part2(123789) == False)

print("Part 2:", count_matches(check_number_part2))