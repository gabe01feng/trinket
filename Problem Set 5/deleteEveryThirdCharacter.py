a = str(input("Pick a string. "))

print("Your string with every third character removed is: ", sep = '', end = '')

for i in range(0, len(a)):
    if not i % 3 == 0:
        print(a[i], sep = '', end = '')