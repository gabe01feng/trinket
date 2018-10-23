a = int(input("Pick a start number. "))
b = int(input("Pick an end number. "))

if a < b:
    for i in range(a, b + 1):
        print(i)
elif a >= b:
    for i in range(a, b - 1, -1):
        print(i)