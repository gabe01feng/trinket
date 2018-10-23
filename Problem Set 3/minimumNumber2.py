a = int(input("What's the first number? "))
b = int(input("What's the second number? "))
x = 0

if a < b:
    x = a
else:
    x = b

print("The smaller number is " + str(x) + ".")