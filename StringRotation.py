text,shift = str(input()), int(input())
if shift == 0: print(text)
else:
    x = shift % len(text)
    if x < 0: print(text[x:]+text[:x])
    else: print(text[-x:]+text[:-x])