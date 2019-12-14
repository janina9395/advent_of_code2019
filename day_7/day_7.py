import itertools
import copy
from intcode import compute, Program


def amplifier(program, input, mode=None):
    output = compute(program, input, mode)

    if output is not None and len(output) > 0:
        return output[0]
    return None


def thrusters_signal(program, modes, input):
    output = input
    for mode in modes:
        output = amplifier(Program(copy.copy(program)), output, mode)
    return output


assert(thrusters_signal([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], [4,3,2,1,0], 0) == 43210)
assert(thrusters_signal([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0], [0,1,2,3,4], 0) == 54321)
assert(thrusters_signal([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0], [1,0,4,3,2], 0) == 65210)


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
def feedback_loop(program, modes, input):
    program_copies = []
    outputs = []
    output = input

    for i in range(0, 5):
        program_copies.append(Program(program.copy()))
        output = amplifier(program_copies[i], output, modes[i])
        outputs.append(output)

    i = 0
    halts = 0
    while True:
        output = amplifier(program_copies[i], output)
        if output is not None:
            outputs[i] = output
        else:
            halts += 1
            if halts == 5:
                break

        i += 1
        if i == 5:
            i = 0
            halts = 0

    return outputs[4]


def max_feedback_loop():
    program = read_input()
    permutations = itertools.permutations(range(5, 10))

    outputs = []
    for modes in permutations:
        outputs.append(feedback_loop(program, modes, 0))

    return max(outputs)


assert(feedback_loop([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5], [9,8,7,6,5], 0) == 139629729)
assert(feedback_loop([3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10],[9,7,8,5,6],0) == 18216)

print("Part 2:", max_feedback_loop())









