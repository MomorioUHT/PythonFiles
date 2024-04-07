context = str(input())
ls = [int(i) for i in context.replace("[","").replace("]","").split(",")]

def checkMiniSum(ls: list):
    currsum = 0
    for currindex in range(0,len(ls)):
        currsum = sum(ls) - ls[currindex]
        if ls[currindex] > currsum: return False
    return True

if (checkMiniSum(ls)): print("true")
else: print("false")