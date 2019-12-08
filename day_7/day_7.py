from day_5.day_5 import compute
import itertools
import copy


def amplifier(program, input, mode=None):
    output = compute(program, input, mode)

    if len(output) > 0:
        return output[0]
    return None


def thrusters_signal(program, modes, input):
    output = input
    for mode in modes:
        output = amplifier(copy.copy(program), output, mode)
    return output


print(thrusters_signal([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], [4,3,2,1,0], 0) == 43210)
print(thrusters_signal([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0], [0,1,2,3,4], 0) == 54321)
print(thrusters_signal([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0], [1,0,4,3,2], 0) == 65210)


def read_input():
    f = open("input")
    a = list(map(int, f.readlines()[0].split(",")))
    f.close()
    return a


def max_thrusters_signal():
    program = read_input()
    permutations = itertools.permutations([0, 1, 2, 3, 4])

    outputs = []
    for p in permutations:
        outputs.append(thrusters_signal(program, p, 0))
    return max(outputs)

print("Part 1:", max_thrusters_signal())

# part 2
def feedback_loop(programs, modes, input):
    output = input

    i = 0
    for mode in modes:
        output = amplifier(programs[i], output, mode)
        i += 1

    i = 0
    while True:
        print("i = ", i, "input = ", output)
        print(programs[i])

        try:
            output = amplifier(programs[i], output)
        except:
            return output

        i += 1
        if i == 5:
            i = 0

    return output


def max_feedback_loop():
    program = read_input()
    program_copies = [program] * 5
    permutations = itertools.permutations(range(5, 10))

    outputs = []
    for modes in permutations:
        print(modes)
        outputs.append(feedback_loop(program_copies, modes, 0))

    return max(outputs)

print("Part 2:", max_feedback_loop())









