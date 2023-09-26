n = int(input())

x = input().split()
y = input().split()

a = 0
b = 0

index = 0

for i in range(0,n):
    a += int(x[i])
    b += int(y[i])

    if(a == b):
        index = i + 1

print(index)