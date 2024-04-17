x = str(input())

def atoi(s: str):
    result = ''
    for i in range(0,len(s)):
        if s[i].isdigit():
            result += s[i]
    return result

print(atoi(x))