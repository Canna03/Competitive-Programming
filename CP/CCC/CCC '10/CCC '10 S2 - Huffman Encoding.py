def solve(s, d):
    output = ""
    code = ""
    for i in range(len(s)):
        code += s[i]
        if code in d.keys():
            output += d[code]
            code = ""
    print(output)

        

            

n = int(input())
d = {}
for i in range(n):
    s = input()
    d.setdefault(s[2:], s[0])
s = input()
solve(s, d)