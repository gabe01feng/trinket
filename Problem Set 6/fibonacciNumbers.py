a = 1
b = 0

for i in range(int(input())):
    a, b = a + b, a
    
print(b)