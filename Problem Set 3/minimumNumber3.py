a = int(input("What's the first number? "))
b = int(input("What's the second number? "))
c = int(input("What's the third number? "))
x = 0

if a < b:
    if a < c:
        x = a
    elif c < a:
        x = c
elif b < a:
    if b < c:
        x = b
    elif c < b:
        x = c
        
print("The smallest number is " + str(x) + ".")