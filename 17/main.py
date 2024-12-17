import re

inp = open("input.txt").read()
registers, program = inp.split("\n\n")
registers = [int(x) for x in re.findall(r"\d+", registers)]
program = [int(x) for x in re.findall(r"\d+", program)]


def run_program(program, registers):
    a, b, c = registers.copy()
    output = []
    ip = 0

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]

        def combo():
            if operand == 4:
                return a
            elif operand == 5:
                return b
            elif operand == 6:
                return c
            else:
                return operand

        if opcode == 0:
            # adv divide
            a //= 2 ** combo()
        elif opcode == 1:
            # bxl bitwisexor
            b ^= operand
        elif opcode == 2:
            # modulo 8
            b = combo() % 8
        elif opcode == 3:
            # jnz jump not zero
            if a != 0:
                ip = operand
                continue
        elif opcode == 4:
            # bxc bitise xor
            b ^= c
        elif opcode == 5:
            # out
            output.append(combo() % 8)
        elif opcode == 6:
            # bdv division
            b = a // (2 ** combo())
        elif opcode == 7:
            # cdv division
            c = a // (2 ** combo())

        ip += 2

    return output


print(",".join(str(x) for x in run_program(program, registers)))

a = 1
maxlen = 0
while True:
    output = run_program(program, [a, 0, 0])
    # print(f"A={a} O={output}")

    if output == program[-3:]:
        print("Found bytes 1-3:", a)
        a *= 8 * 8 * 8
    elif output == program[-6:]:
        print("Found bytes 4-6:", a)
        a *= 8 * 8 * 8
    elif output == program[-9:]:
        print("Found bytes 7-9:", a)
        a *= 8 * 8 * 8
    elif output == program[-12:]:
        print("Found bytes 10-12:", a)
        a *= 8 * 8 * 8
    elif output == program[-15:]:
        print("Found bytes 13-15:", a)
        a *= 8
    elif output == program:
        print("Found byte 16:", a)
        break
    else:
        a += 1
