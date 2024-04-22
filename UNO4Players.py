#R G B Y #0-9
color_piority = ["R","G","B","Y"]
value_piority = ["0","1","2","3","4","5","6","7","8","9"]
def helper(card: str): return color_piority.index(card[1]),value_piority.index(card[0])

p1 = sorted([i for i in str(input()).split(" ")], key=helper)
p2 = sorted([i for i in str(input()).split(" ")], key=helper)
p3 = sorted([i for i in str(input()).split(" ")], key=helper)
p4 = sorted([i for i in str(input()).split(" ")], key=helper)
players = [p1,p2,p3,p4]
startCard = str(input())
    
def place(playerList: list, playerIndex: int, currFaceCard: str):
    currPlayer = playerList[playerIndex]
    
    for i in range(len(currPlayer)):
        if currPlayer[i] == currFaceCard: #Check ALL
            print(f"Player {playerIndex+1} place {currPlayer[i]} card to match {currFaceCard} in both number and color")
            foundCard = currPlayer[i]
            currPlayer.pop(i)
            return [True,foundCard]

    for i in range(len(currPlayer)): #Check numbers
        if currPlayer[i][0] == currFaceCard[0]: 
            print(f"Player {playerIndex+1} place {currPlayer[i]} card to match {currFaceCard} in number")
            foundCard = currPlayer[i]
            currPlayer.pop(i)
            return [True,foundCard]
        
    for i in range(len(currPlayer)): #Check colors
        if currPlayer[i][1] == currFaceCard[1]: 
            print(f"Player {playerIndex+1} place {currPlayer[i]} card to match {currFaceCard} in color")
            foundCard = currPlayer[i]
            currPlayer.pop(i)
            return [True,foundCard]
        
    print(f"Player {playerIndex+1} does not have a card to place")
    return [False]

index = 0
currCard = startCard
while True:
    currIndex = index%4
    response = place(players, currIndex, currCard)
    if (len(response) == 2): #If placeble
        currCard = response[1] #Updates the current card
        print(f"Now the current card is {currCard}...")
        if len(players[0]) == 0: break
        if len(players[1]) == 0: break
        if len(players[2]) == 0: break
        if len(players[3]) == 0: break
    else:
        break
    index += 1

print(f"------------------")
print(f"Current Card: {currCard}")
print(f"Table hands:")
for i in range(4):
    print(f"Player {i+1}: ", end='')
    print(*players[i])
print(f"------------------")