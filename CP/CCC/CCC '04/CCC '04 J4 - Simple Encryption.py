def solve(s, m):
    newWord = ""
    for i in range(len(m)):
        shift = ord(s[i % len(s)]) % 65
        new = ord(m[i]) + shift
        if new > 90:
            new -= 26
        newWord += chr(new)
    return newWord
        

            

s = input().upper()
m = input().upper()
replace = []
for i in range(len(m)):
    if not 64 < ord(m[i]) < 91:
        replace.append(m[i])
for i in replace:
    m = m.replace(i, "")

print(solve(s,m))