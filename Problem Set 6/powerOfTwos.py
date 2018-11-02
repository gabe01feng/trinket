a = int(input())
b = 0
c = 1

while a // 2 != 0:
    b += 1
    a //= 2
    
for i in range(1, b + 1):
    c *= 2
    
print(str(b), str(c))