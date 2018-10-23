x1 = int(input("What column did the queen start in? "))
y1 = int(input("What row did the queen start in? "))
x2 = int(input("What column did the queen stop in? "))
y2 = int(input("What row did the queen stop in? "))

if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    print("Yes, the queen can move there.")
else:
    print("No, the queen cannot move there.")