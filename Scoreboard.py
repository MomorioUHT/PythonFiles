A = []
B = []
ls = str(input()).split(" ")
for i in ls:
    if i == "A": 
        A.append("X")
        B.append(" ")
    else:
        A.append(" ")
        B.append("X")
ACount = sum([1 for i in A if i.isalpha()])
BCount = sum([1 for i in B if i.isalpha()])

print(f"SCOREBOARD")
print("----------------------------------")
print(f"| Team A |", end="")       
for i in range(12):
    print(f"{A[i]}|", end="")
print("")
print("----------------------------------")
print(f"| Team B |", end="")       
for i in range(12):
    print(f"{B[i]}|", end="")
print("")
print("----------------------------------")
print(f"Scores: A/B = {ACount}/{BCount}")

if (ACount == BCount):
    print("TIE")
elif (ACount > BCount):
    print("Team A is the Winner")
else:
    print("Team B is the Winner")