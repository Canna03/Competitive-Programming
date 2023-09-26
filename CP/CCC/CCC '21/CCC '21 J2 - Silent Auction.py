n = int(input())
b = 0
p = ""

for i in range(n):
    s = input()
    x = int(input())
    if x > b:
        b = x
        p = s

print(p)