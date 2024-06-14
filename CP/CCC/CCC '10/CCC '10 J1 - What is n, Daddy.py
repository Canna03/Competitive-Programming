def solve(n: int) -> int:
    a = max(0, n - 5)
    n = min(5, n)
    total = 1
    while a + 1 < n:
        n -= 1
        a += 1
        total += 1
    return total

n = int(input())
print(solve(n))