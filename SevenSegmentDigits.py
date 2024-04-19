def seven_segment_display(number, maxlen):
    segments = {
        "0": [' -- ', '|  |', '|  |', '|  |', ' -- '],
        "1": ['    ', '   |', '   |', '   |', '    '],
        "2": [' -- ', '   |', ' -- ', '|   ', ' -- '],
        "3": [' -- ', '   |', ' -- ', '   |', ' -- '],
        "4": ['    ', '|  |', ' -- ', '   |', '    '],
        "5": [' -- ', '|   ', ' -- ', '   |', ' -- '],
        "6": [' -- ', '|   ', ' -- ', '|  |', ' -- '],
        "7": [' -- ', '   |', '    ', '   |', '    '],
        "8": [' -- ', '|  |', ' -- ', '|  |', ' -- '],
        "9": [' -- ', '|  |', ' -- ', '   |', ' -- '],
        "p": ['    ', '    ', '    ', '    ', '    '],
    }
    
    number = ("p"*(maxlen - len(str(number)))) + str(number)
    digits = [str(d) for d in str(number)]
    lines = [""] * 5
    
    for a in range(len(digits)):
        digit_segments = segments[digits[a]]
        for i in range(5): 
            if a == len(digits)-1: lines[i] += digit_segments[i]
            else: lines[i] += digit_segments[i] + ' '
    
    display = '\n'.join(lines)
    return display,len(lines[i])

x = int(input())
y = int(input())
result = x+y

maxlen = max([len(str(x)), len(str(y)), len(str(result))])

print(seven_segment_display(x, maxlen)[0])
print(seven_segment_display(y, maxlen)[0])
print("-"*(seven_segment_display(result, maxlen)[1]))
print(seven_segment_display(result, maxlen)[0])
print("="*(seven_segment_display(result, maxlen)[1]))