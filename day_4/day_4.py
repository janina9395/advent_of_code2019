def check_number(n):
    digits = list(map(lambda x: int(x), list(str(n))))
    prev = digits[0]
    rest = digits[1:]

    double = False
    increasing = True
    counters = {}
    for next in rest:
        if next < prev:
            increasing = False
            break
        if prev == next:
            double = True
            if prev in counters.keys():
                counters[prev] = counters[prev] + 1
            else:
                counters[prev] = 2
        prev = next

    # print(counters)
    return double and increasing and 2 in counters.values()


print(check_number(122345))
print(check_number(111111))
print(check_number(223450))
print(check_number(123789))

count = 0
for n in range(193651, 649729):
    if check_number(n):
        count += 1

print(count)
