def solve(s):
    if s == "A":
        return True
    elif s.find("ANA") == s.find("BAS") == -1:
        return False
    
    s = s.replace("ANA", "A")
    s = s.replace("BAS", "A")
    return solve(s)

s = input()
while not s == "X":
    if solve(s):
        print("YES")
    else:
        print("NO")
    s = input()