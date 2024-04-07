text = str(input())

def stringFrame(s: str):
    length = len(s)
    if length <= 2: print("ERROR")
    else:
        for i in range(length):
            if i == length-1: print(f"{s[i]}")
            else: print(f"{s[i]} ", end="")
            
        for i in range(1, length-1):
            print(f"{s[i]}{' '*(length+length-3)}{s[length-i-1]}")
            
        for i in range(length-1,-1,-1):
            if i == 0: print(f"{s[i]}")
            else: print(f"{s[i]} ", end="")

stringFrame(text)