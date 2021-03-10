def simple_assembler(program):
    vars = {}
    i = 0
    print(program)
    while i < len(program):
        instruction = program[i].split(" ")

        if instruction[0] == "mov" and instruction[2].isalpha():
            vars[instruction[1]] = vars[instruction[2]]
            
        elif instruction[0] == "mov" and instruction[2].strip("-").isdigit():
            vars[instruction[1]] = int(instruction[2])
            
        elif instruction[0] == "inc":
            vars[instruction[1]]+=1
            
        elif instruction[0] == "dec":
            vars[instruction[1]]-=1

        elif instruction[0] == "jnz" and instruction[1].isalpha() and vars[instruction[1]]!= 0 or instruction[1].strip("-").isdigit() and instruction[1] != "0":
            i+=int(instruction[2])
            continue
        i+=1
    return vars