def longestPalindrome(s):
    n = 1
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[j:i:-1]:
                if n < j-i+1:
                    n = j-i+1
    return n

s = input()
print(longestPalindrome(s))