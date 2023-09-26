n = int(input())
for x in range(0,n):
    s = list(input())
    c = s[0]
    l = 1
    st = ""
    for y in range(1,len(s)):
        if s[y] == c:
            l += 1
        else:
            st += str(l) + " " + c + " "
            c = s[y]
            l = 1
    st += str(l) + " " + c
    print(st)