def solve(a: int, b: int, c: int, d: int, s: int) -> str:
    byron = 0
    nikky = 0
    
    for i in range(s):
        if i % (a + b) < a:
            nikky += 1
        else:
            nikky -= 1
        if i % (c + d) < c:
            byron += 1
        else:
            byron -= 1
    if byron == nikky:
        return "Tied"
    return "Byron" if byron > nikky else "Nikky"

a, b, c, d ,s = int(input()), int(input()), int(input()), int(input()), int(input())
print(solve(a, b, c, d, s))