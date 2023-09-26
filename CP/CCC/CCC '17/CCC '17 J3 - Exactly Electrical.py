def solve(a,b,c,d,n):
    s = abs(d - b) + abs(c - a)
    return abs(s - n) % 2 == 0 and s <= n

c1 = input().split(" ")
c2 = input().split(" ")
a, b, c, d = int(c1[0]), int(c1[1]), int(c2[0]), int(c2[1])
n = int(input())
print("Y" if solve(a,b,c,d,n) else "N")