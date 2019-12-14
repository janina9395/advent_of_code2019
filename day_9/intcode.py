def param(mode, program, arg):
    if mode == 0:
        return program.instructions.get(arg, 0)
    elif mode == 1:
        return arg
    elif mode == 2:
        return program.instructions.get(program.base + arg, 0)


def write_index(mode, program, index):
    if mode == 0:
        return program.instructions.get(index, 0)
    elif mode == 2:
        return program.base + program.instructions.get(index, 0)


def normalize(instr):
    missed_zeros = 5 - len(instr)
    for i in range(0, missed_zeros):
        instr = "0" + instr
    return instr


class Program:
    def __init__(self, instructions, position = 0, base = 0):
        self.instructions = instructions
        self.position = position
        self.base = base


def compute(program, input = None):
    instr = program.instructions
    output = []
    i = program.position
    while i < len(instr):
        i_code = instr[i]
        s_code = normalize(str(i_code))
        op_code = int(s_code[-2:])
        m1 = int(s_code[2])
        m2 = int(s_code[1])
        m3 = int(s_code[0])

        if op_code == 1:
            p1 = param(m1, program, instr[i + 1])
            p2 = param(m2, program, instr[i + 2])
            p3 = write_index(m3, program, i + 3)
            instr[p3] = p1 + p2
            i = i + 4
        elif op_code == 2:
            p1 = param(m1, program, instr[i + 1])
            p2 = param(m2, program, instr[i + 2])
            p3 = write_index(m3, program, i + 3)
            instr[p3] = p1 * p2
            i = i + 4
        elif op_code == 4:
            p1 = param(m1, program, instr[i + 1])
            output.append(p1)
            i = i + 2
        elif op_code == 5:
            p1 = param(m1, program, instr[i + 1])
            p2 = param(m2, program, instr[i + 2])
            if p1 != 0:
                i = p2
            else:
                i = i + 3
        elif op_code == 6:
            p1 = param(m1, program, instr[i + 1])
            p2 = param(m2, program, instr[i + 2])
            if p1 == 0:
                i = p2
            else:
                i = i + 3
        elif op_code == 7:
            p1 = param(m1, program, instr[i + 1])
            p2 = param(m2, program, instr[i + 2])
            p3 = write_index(m3, program, i + 3)
            if p1 < p2:
                instr[p3] = 1
            else:
                instr[p3] = 0
            i = i + 4
        elif op_code == 8:
            p1 = param(m1, program, instr[i + 1])
            p2 = param(m2, program, instr[i + 2])
            p3 = write_index(m3, program, i + 3)
            if p1 == p2:
                instr[p3] = 1
            else:
                instr[p3] = 0
            i = i + 4
        elif op_code == 9:
            p1 = param(m1, program, instr[i + 1])
            program.base += p1
            i = i + 2
        elif op_code == 3:
            p1 = write_index(m1, program, i + 1)
            instr[p1] = input
            i = i + 2
        elif op_code == 99:
            break
        else:
            print("error opcode", op_code)
            i = i + 1
    return output

