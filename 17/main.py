import re

inp = open("input.txt").read()

# inp = """
# Register A: 2024
# Register B: 0
# Register C: 0
#
# Program: 0,3,5,4,3,0
# """.strip()

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
    # print(a)
    output = run_program(program, [a, 0, 0])
    # print(f"Output = {output}")

    if len(output) > maxlen:
        maxlen = len(output)
        print("Maxlen:", maxlen, "A:", a, a // 8)

    if len(output) < len(program):
        a *= 8
    else:
        print(a * 8 - a)
        break

    if output == program:
        # print("Found:", a)
        break

    a += 1
    # if len(output) <= len(program):
    #     seen = a
    #     a += 1_000_000_000
    # else:
    #     if a <= seen:
    #         break
    # a -= 5_000_000
