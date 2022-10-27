sol = 0
while True:
        opcode = int(input())
        if opcode == 0:
            break
        if opcode == 1:
            sol = (sol+int(input())) & 65535
        elif opcode == 2:
            sol = (sol - int(input())) & 65535
        elif opcode == 3:
            sol = (sol*int(input())) & 65535


print(sol)