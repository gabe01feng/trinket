a = int(input("Pick a number. "))
b = 0

for i in range(1, a + 1):
    b += (i ** 3)

print("The the cube of the sum of the numbers under " + str(a) + " is " + str(b) + ".")