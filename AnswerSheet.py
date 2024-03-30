name = str(input())
choices = str(input()).split("-")

def drawAnswerSheet(inputName: str, yourChoices: list):
    print(f"Name: {inputName}")
    print("-----------")
    print("  |A|B|C|D|")
    print("-----------")
    for i in range(len(yourChoices)):
        if yourChoices[i] == "A": print(f"{i+1:2d}|X| | | |")
        elif yourChoices[i] == "B": print(f"{i+1:2d}| |X| | |")
        elif yourChoices[i] == "C": print(f"{i+1:2d}| | |X| |")
        elif yourChoices[i] == "D": print(f"{i+1:2d}| | | |X|")
        else: print(f"{i+1:2d}| | | | |")
    print("-----------")    

drawAnswerSheet(name, choices)