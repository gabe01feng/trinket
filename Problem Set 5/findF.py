a = input("Pick a string. ")
b = a[::-1]

if a.count('f') == 0:
    print("There is no letter 'f' in your string.")
elif a.count('f') == 1:
    print("The letter 'f' is at the index " + str(a.find('f')) + ".")
else:
    print("The first letter 'f' is at the index " + str(a.find('f')) + " the last letter 'f' is at the index " + str(len(a) - (b.find('f') + 1)) + ".")