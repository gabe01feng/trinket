a = input("Pick a string with at least two 'h's. ")

print("Your string without the string between the 'h's is: " + a[:a.find('h')] + a[(a.rfind('h') + 1):])