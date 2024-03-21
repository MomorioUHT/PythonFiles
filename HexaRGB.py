red = int(input())
green = int(input())
blue = int(input())

def intToHexa(x: int):
    if x <= 0: return "00"
    if x > 255: return "FF"
    
    hex_digits = "0123456789ABCDEF"
    result = ''
    while x >= 1:
        y = x%16
        result += hex_digits[int(y)] 
        x /= 16
    if len(result) == 1: return "0" + result
    return result

print(f"Color Code: {intToHexa(red)}{intToHexa(green)}{intToHexa(blue)}")