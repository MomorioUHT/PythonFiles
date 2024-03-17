ls = [i for i in str(input()).split(",")]

def checkComma(ls: list):
    for i in range(0,len(ls)):
        if i == 0:
            if len(ls[i]) > 3 or len(ls[i]) == 0: return False
            elif ls[i].startswith('0'): return False
        else:   
            if len(ls[i]) != 3: return False
    return True

if (checkComma(ls)): print("Correct")
else: print("Incorrect")