a = 0
b = int(input())
c = 1
d = 0

while b != 0:
    if a < b:
        a = b
        d = c
    b = int(input())
    c += 1
    
print(d)