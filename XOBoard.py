grid = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]
while True:
    place = str(input()).split(" ")
    if place[0] == "exit": break
    grid[int(place[1])][int(place[2])] = place[0]
    
print("-------")
for i in range(3):
    print("|", end="")
    for j in range(3):
        print(f"{grid[j][i]}|", end="")
    print("\n-------")
