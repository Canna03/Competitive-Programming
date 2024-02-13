x = []
y = []
d = {}
v = 0

for i in range(int(input())):
    x.append([a for a in input().split(' ')])

for i in range(int(input())):
    y.append([a for a in input().split(' ')])
    
for i in range(int(input())):
    n = [a for a in input().split(' ')]
    for a in n:
        d[a] = n
        

for i in x:
    if not i[1] in d[i[0]]:
        v += 1

for i in y:
    if i[1] in d[i[0]]:
        v += 1

print(v)