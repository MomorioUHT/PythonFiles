x = str(input())

def HextoInt(s: str):
    hex_digits = "0123456789ABCDEF"
    result = 0
    for i in s.upper():
        if i not in hex_digits: return "Invalid Hexadecimal"
        digit_value = hex_digits.index(i) 
        result = (16 * result) + digit_value
    return result

print(HextoInt(x))