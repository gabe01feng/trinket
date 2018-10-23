x1 = int(input("What column does the knight start in? "))
y1 = int(input("What row does the knight start in? "))
x2 = int(input("What column does the knight stop in? "))
y2 = int(input("What row does the knight stop in? "))

if (abs(x1 - x2) == 2 or abs(y1 - y2)) == 2 and (abs(x1 - x2) == 1 or abs(y1 - y2) == 1):
    print("Yes, the knight can move there.")
else:
    print("No, the knight cannot move there.")