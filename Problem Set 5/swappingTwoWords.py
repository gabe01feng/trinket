a = input("Choose two strings. ")
b = a.rfind(' ')
    
print("Your strings flipped are:" + a[b:] + " " + a[:b])