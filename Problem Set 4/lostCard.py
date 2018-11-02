a = int(input("Pick a number of cards. "))
b = 0

for i in range(1, a + 1):
    b += i

for n in range(0, a - 1):
    c = int(input("Pick a number under or equal to " + str(a) + " that you haven't chosen yet. "))
    b =  b - c
    
print("The number you haven't chosen yet is " + str(b) + ".")