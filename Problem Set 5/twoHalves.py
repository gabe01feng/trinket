a = input("Pick a string. ")
b = len(a) // 2 + len(a) % 2

print("Your string backwards is: " + a[b:] + a[:b])