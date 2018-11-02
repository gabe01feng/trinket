a = int(input("How many numbers are you going to enter? "))
b = 0

for i in range(0, a):
    c = int(input("Pick a number. "))
    if c == 0:
        b += 1

print("The number of 0s is" + str(b) + ".")