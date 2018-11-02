a = int(input("Pick a number. "))

for i in range(1, a + 1):
    for n in range(1, i + 1):
        print(n, sep = '', end = '')
    print()