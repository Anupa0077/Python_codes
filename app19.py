try:
    T = int(input())
    for _ in range(T):
        c = input()
        if (c == 'b' or c == 'B'):
            print("Battleship")
        elif (c == 'c' or c == 'C'):
            print("Curiser")
        elif (c == 'd' or c == 'D'):
            print("Destroyer")
        else:
            print("Frigate")


except:
    pass