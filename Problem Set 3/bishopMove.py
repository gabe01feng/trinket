x1 = int(input("What column did the bishop start in? "))
y1 = int(input("What row did the bishop start in? "))
x2 = int(input("What column did the bishop stop in? "))
y2 = int(input("What row did the bishop stop in? "))

if abs(x1 - x2) == abs(y1 - y2):
    print("Yes, the bishop can move there.")
else:
    print("No, the bishop cannot move there.")