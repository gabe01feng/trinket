a = int(input("Pick a number. "))
b = 1

for i in range(1, a + 1):
    b *= i

print("The factorial of " + str(a) + " is " + str(b) + ".")