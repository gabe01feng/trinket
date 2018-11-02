a = 0
b = 1
c = 0

while b != 0:
    b = int(input())
    if c < b:
        c = b
    
    if a < b:
        a, c = b, a

print(c)