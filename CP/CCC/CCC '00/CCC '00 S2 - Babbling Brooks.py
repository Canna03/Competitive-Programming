n = int(input())

streams = []
for i in range(n):
    streams.append(int(input()))
    
join = int(input())
while join != 77:
    if join == 99:
        index = int(input())
        factor = int(input())
        left = streams[index - 1] * factor / 100
        right = streams[index - 1] * (100 - factor) / 100
        streams = streams[:index - 1] + [left] + [right] + streams[index:]
        
    elif join == 88:
        index = int(input())
        right = streams[index]
        streams = streams[:index] + streams[index + 1:]
        streams[index - 1] = streams[index - 1] + right
        
    join = int(input())
    
s = ""
for i in streams:
    s += str(round(i)) + " "
print(s[:-1])