from intcode import compute, Program


def to_dict(arr):
    return {i: arr[i] for i in range(0, len(arr))}


def read_input():
    f = open("input")
    a = list(map(int, f.readlines()[0].split(",")))
    f.close()
    return to_dict(a)

#print(read_input())

assert(compute(Program(to_dict([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]))) == [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])
assert(compute(Program(to_dict([1102,34915192,34915192,7,4,7,99,0]))) == [34915192*34915192])
assert(compute(Program(to_dict([104,1125899906842624,99]))) == [1125899906842624])

print("Part 1:", compute(Program(read_input()), 1))
print("Part 2:", compute(Program(read_input()), 2))


