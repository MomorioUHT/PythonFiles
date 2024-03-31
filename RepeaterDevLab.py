text = str(input())
space = (len(text)-1)*2

def createRight(text: str, n: int):
    temp = ''
    for i in range(n+1):
        if i == len(text): temp += text[i]
        else: temp += text[i] + " "
    return temp

for i in range(len(text)):
    right = createRight(text, i)
    left = right[::-1][0:-1].lstrip()
    temp = left + right
    print(f"{' '*space}{temp}")
    space -= 2