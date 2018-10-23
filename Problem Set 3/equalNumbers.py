a = int(input("What's the first number? "))
b = int(input("What's the second number? "))
c = int(input("What's the third number? "))

if a == b:
    if a == c:
        print("3 numbers are equal.")
    else:
        print("2 numbers are equal.")
elif b == c or a == c:
    print("2 numbers are equal.")
else:
    print("None are equal.")