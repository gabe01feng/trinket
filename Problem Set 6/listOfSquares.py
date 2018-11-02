a = int(input())
b = ''

for i in range(1, a + 1):
    if i ** 2 <= a:
        b += str(i ** 2) + ' '
        
print(b)