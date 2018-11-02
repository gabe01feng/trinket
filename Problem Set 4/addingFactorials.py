a = int(input("Pick a number. "))
c = a

for i in range(a, 0, -1):
    b = c + 1
    if i - 1 == 0:
        b = b
    else:
        c = (i - 1) * (b)
    
print("The sum of the factorials up to " + str(a) + " is " + str(c) + ".")