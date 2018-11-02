a = input("Pick a string with at least 3 'h's. ")

print("You string with every 'h' but the first and last captialized is: " + a[:a.find('h') + 1] + a[a.find('h') + 1: a.rfind('h')].replace('h', 'H') + a[a.rfind('h'):])