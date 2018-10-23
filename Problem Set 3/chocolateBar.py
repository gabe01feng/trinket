a = int(input("How many chocolate squares are there in a row? "))
b = int(input("How many chocolate squares are there in a column? "))
c = int(input("How many chocolate squares do you want left over? "))

if (c % a == 0 or c % b == 0) and c <= a * b:
    print("Yes, the chocolate bar can be split to have " + str(c) + " squares.")
else:
    print("No, the chocolate bar cannot be split to have " + str(c) + " squares.")