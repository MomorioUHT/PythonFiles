x = int(input())
y = str(input())
if x % 360 == 0:
    print("X X ^ X X")
    print("X X | X X")
    print("X X | X X")
    print("X X | X X")
    print("X X | X X")    
elif x % 360 == 90:
    if y.lower() == "cw":
        print("X X X X X")
        print("X X X X X")
        print("= = = = >")
        print("X X X X X")
        print("X X X X X")
    elif y.lower() == "ccw":
        print("X X X X X")
        print("X X X X X")
        print("< = = = =")
        print("X X X X X")
        print("X X X X X")
elif x % 360 == 180:
    print("X X | X X")
    print("X X | X X")
    print("X X | X X")
    print("X X | X X")
    print("X X V X X")
elif x % 360 == 270:
    if y.lower() == "cw":
        print("X X X X X")
        print("X X X X X")
        print("< = = = =")
        print("X X X X X")
        print("X X X X X")
    elif y.lower() == "ccw":
        print("X X X X X")
        print("X X X X X")
        print("= = = = >")
        print("X X X X X")
        print("X X X X X")