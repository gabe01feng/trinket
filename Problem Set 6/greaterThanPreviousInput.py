a = 0
b = 1
c = int(input())

while b != 0:
    b = int(input())
    if c < b:
        a += 1
    c = b
    
print(a)