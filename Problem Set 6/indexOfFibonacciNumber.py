a = 1
b = 0
c = int(input())
d = 0

while b != c:
    a, b = a + b, a
    d += 1
    if b > c:
        print("-1")
        break

if b == c:
    print(d)