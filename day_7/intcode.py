def param(mode, program, arg):
    if mode == 0:
        return program[arg]
    elif mode == 1:
        return arg


def is_instruction(instr):
    length = len(instr)
    if not (instr[length - 1] in ["1", "2", "5", "6", "7", "8"]):
        return False
    if length >= 3 and instr[length - 2] != "0":
        return False
    for i in range(0, length - 2):
        if not (instr[i] == "0" or instr[i] == "1"):
            return False
    return True


def normalize(instr):
    missed_zeros = 5 - len(instr)
    for i in range(0, missed_zeros):
        instr = "0" + instr
    return instr


class Program:
    def __init__(self, instructions, position = 0):
        self.instructions = instructions
        self.position = position


def compute(program, input, phase = None):
    instr = program.instructions
    if phase is None:
        phase = input
    output = []
    i = program.position
    first_input = True
    while i < len(instr):
        i_code = instr[i]
        s_code = str(i_code)
        if is_instruction(s_code):
            s_code = normalize(s_code)
            op_code = int(s_code[-2:])
            m1 = int(s_code[2])
            m2 = int(s_code[1])

            if op_code == 1:
                p1 = param(m1, instr, instr[i + 1])
                p2 = param(m2, instr, instr[i + 2])
                p3 = instr[i + 3]
                instr[p3] = p1 + p2
                i = i + 4
            elif op_code == 2:
                p1 = param(m1, instr, instr[i + 1])
                p2 = param(m2, instr, instr[i + 2])
                p3 = instr[i + 3]
                instr[p3] = p1 * p2
                i = i + 4
            elif op_code == 5:
                p1 = param(m1, instr, instr[i + 1])
                p2 = param(m2, instr, instr[i + 2])
                if p1 != 0:
                    i = p2
                else:
                    i = i + 3
            elif op_code == 6:
                p1 = param(m1, instr, instr[i + 1])
                p2 = param(m2, instr, instr[i + 2])
                if p1 == 0:
                    i = p2
                else:
                    i = i + 3
            elif op_code == 7:
                p1 = param(m1, instr, instr[i + 1])
                p2 = param(m2, instr, instr[i + 2])
                p3 = instr[i + 3]
                if p1 < p2:
                    instr[p3] = 1
                else:
                    instr[p3] = 0
                i = i + 4
            elif op_code == 8:
                p1 = param(m1, instr, instr[i + 1])
                p2 = param(m2, instr, instr[i + 2])
                p3 = instr[i + 3]
                if p1 == p2:
                    instr[p3] = 1
                else:
                    instr[p3] = 0
                i = i + 4
            else:
                i = i + 1
        elif i_code == 3:
            setting = input
            if first_input:
                setting = phase
                first_input = False
            p1 = instr[i + 1]
            instr[p1] = setting
            i = i + 2
        elif i_code == 4:
            p1 = instr[i + 1]
            output.append(instr[p1])
            i = i + 2
            program.position = i
            return output
        elif i_code == 99:
            return None
        else:
            i = i + 1

