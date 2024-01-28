text = input()
if len(text) == 1: print(text)
elif len(text)%2 == 0: print(f"{text[(len(text)//2)-1::-1]}{text[:(len(text)//2)-1:-1]}")
else: print(f"{text[(len(text)//2)-1::-1]}{text[(len(text)//2)]}{text[:(len(text)//2):-1]}")