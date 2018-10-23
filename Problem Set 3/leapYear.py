a = int(input("What year is it? "))

if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print(str(a) + " year is a leap year.")
else:
    print(str(a) + " year is not a leap year.")