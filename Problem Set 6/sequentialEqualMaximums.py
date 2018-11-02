a = int(input())
b = 1
c = 1
d = 0

while b != 0:
    b = int(input())
    if a == b:
        c += 1
    else:
        a = b
        c = 1
        
    if c > d:
        d = c
        
print(d)