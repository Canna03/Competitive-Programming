def solve(s):
    temp = [int(x) for x in s.split(' ')[1:]]
    cycle = []
    differences = []
    cycle_pointer = 0
    for i in range(len(temp) - 1):
        difference = temp[i + 1] - temp[i]
        differences.append(difference)
        if cycle:
            if len(cycle) == cycle_pointer:
                cycle_pointer = 0
            if difference == cycle[cycle_pointer]:
                cycle_pointer += 1
            else:
                cycle = differences[:]
                cycle_pointer = 0
        else:
            cycle = differences[:]
            
    return len(cycle)
    
s = ''
while 1:
    s = input()
    if s == '0':
        break
    print(solve(s))