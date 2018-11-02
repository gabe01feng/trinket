a = input("Pick a string with two 'h's. ")

print("Your string with the string between the two 'h's reversed is: " + a[:a.find('h')] + a[a.rfind('h'):a.find('h'):-1] + a[a.rfind('h'):])