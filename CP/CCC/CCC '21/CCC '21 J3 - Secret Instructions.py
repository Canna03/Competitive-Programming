def rl(x):
    return True if x % 2 == 0 else False

s = input()
prev = True
while s != "99999":
    a = int(s[0])+int(s[1])
    if a != 0:
        prev = rl(a)
    print("right " + s[2:] if prev else "left " + s[2:])
    s = input()