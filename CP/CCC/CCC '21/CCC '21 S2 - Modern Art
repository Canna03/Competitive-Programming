m = int(input())
n = int(input())
k = int(input())

r = [0]*m
c = [0]*n
rtotal = 0
ctotal = 0

for i in range(k):
    s = input().split(" ")
    a = int(s[1]) - 1
    if s[0] == "R":
        if r[a] == 1:
            r[a] = 0
        else:
            r[a] = 1
    else:
        if c[a] == 1:
            c[a] = 0
        else:
            c[a] = 1

rl = 0
cl = 0
for i in r:
    if i == 1:
        rl += 1
for i in c:
    if i == 1:
        cl += 1

total = rl*n + cl*m - 2 * rl * cl
print(total)