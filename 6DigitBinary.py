num = int(input())

def convertToBinary(num: int):
    result = ''
    while(num >= 1):
        temp = num%2
        result += str(temp)
        num = num//2
    return result[::-1]

print(f"{int(convertToBinary(num)):06d}")