x1 = int(input("What column did the rook start in? "))
y1 = int(input("What row did the rook start in? "))
x2 = int(input("What column did the rook stop in? "))
y2 = int(input("What row did the rook stop in? "))

if x1 == x2 or y1 == y2:
    print("Yes, the rook can make the move in 1 move.")
else:
    print("No, the rook cannot make the move in 1 move.")