a = input()
b = a.split()

for i in range(len(b)):
    if i % 2 == 0:
        print(b[i], end = ' ')