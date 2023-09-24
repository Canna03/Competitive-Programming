case = [[[-1]*251 for j in range(251)] for i in range(251)]
def countN(n, k, u):
    if n < 0:
        case[n][k][u] = 0
        return 0
    if k == 0:
        case[n][k][u] = 1 if n == 0 else 0
        return case[n][k][u]
    if k == 1:
        case[n][k][u] = 1 if n >= u else 0
        return case[n][k][u]
    if case[n][k][u] != -1:
        return case[n][k][u]
    total = 0
    for i in range(u, n//k+1):
        count = countN(n-i,k-1,i)
        total += count
        case[n-i][k-1][i] = count
    return total

n = int(input())
k = int(input())

print(countN(n, k, 1))