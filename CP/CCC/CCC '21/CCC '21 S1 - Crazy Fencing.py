n = int(input())
h = [int(x) for x in input().split(' ')]
b = [int(x) for x in input().split(' ')]
area = 0

for i in range(n):
    area += (h[i] + h[i + 1])/2 * w[i]
print(area)