x1 = int(input("What column did the king start in? "))
y1 = int(input("What row did the king start in? "))
x2 = int(input("What column did the king stop in? "))
y2 = int(input("What row did the king stop in? "))

if 1 >= x1 - x2 >= -1 and 1 >= y1 - y2 >= -1:
    print("Yes, the king can move there.")
else:
    print("No, the king cannot move there.")