def seven_segment_display(number):
    segments = {
        0: [' -- ', '|  |', '|  |', '|  |', ' -- '],
        1: ['    ', '   |', '   |', '   |', '    '],
        2: [' -- ', '   |', ' -- ', '|   ', ' -- '],
        3: [' -- ', '   |', ' -- ', '   |', ' -- '],
        4: ['    ', '|  |', ' -- ', '   |', '    '],
        5: [' -- ', '|   ', ' -- ', '   |', ' -- '],
        6: [' -- ', '|   ', ' -- ', '|  |', ' -- '],
        7: [' -- ', '   |', '    ', '   |', '    '],
        8: [' -- ', '|  |', ' -- ', '|  |', ' -- '],
        9: [' -- ', '|  |', ' -- ', '   |', ' -- ']
    }
    
    def digit_to_segments(digit):
        return segments[digit]
    
    digits = [int(d) for d in str(number)]
    
    lines = [""] * 5
    
    for digit in digits:
        digit_segments = digit_to_segments(digit)
        for i in range(5): 
            lines[i] += digit_segments[i] + ' '
    
    display = '\n'.join(lines)
    return display

number = int(input())
display = seven_segment_display(number)
print(display)