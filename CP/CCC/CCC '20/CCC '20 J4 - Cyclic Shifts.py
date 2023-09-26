def shift(s):
    return s[1:] + s[0]

t = input()
s = input()
y = False

for i in range(len(s)):
    if s in t:
        y = True
        break
    s = shift(s)

print("yes" if y else "no")
