def strokes(c, d, n):
    field = [0]*(d+1)
    
    for i in range(1, d+1):
        min = 99999999
        for j in range(n):
            temp = i-c[j]
            if temp >= 0 and field[temp] >= 0 and field[temp] < min:
                min = field[temp]
        if min != 99999999:
            field[i] = min+1
        else:
            field[i] = -1
    return field[d]
            




d = int(input())
n = int(input())
c = []
for i in range(n):
    c.append(int(input()))

s = strokes(c, d, n)
if(s == -1):
    print("Roberta acknowledges defeat.")
else:
    print("Roberta wins in", s, "strokes.")