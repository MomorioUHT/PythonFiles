booktype = {
    'Sharpness': 5,
    'Knockback': 2,
    'Protection': 4,
    'FireAspect': 2,
    'Fortune': 3,
    'Power': 5,
    'Unbreaking': 3,
    'Looting': 3
}

def romanToInteger(x: str):
    if x == "I": return 1
    elif x == "II": return 2
    elif x == "III": return 3
    elif x == "IV": return 4
    elif x == "V": return 5
    
def integerToRoman(x: int):
    if x == 1: return "I"
    elif x == 2: return "II"
    elif x == 3: return "III"
    elif x == 4: return "IV"
    elif x == 5: return "V"
    
book1 = str(input()).split(" ")
book1_type = book1[0]
book1_level = romanToInteger(book1[1])
book2 = str(input()).split(" ")
book2_type = book2[0]
book2_level = romanToInteger(book2[1])

last_book_type = ''
last_level = ''

if book2_type != book1_type: 
    print("Enchant is not possible")
else:
    last_book_type = book1_type
    if book1_level == book2_level: 
        last_level = book1_level + 1
    elif book2_level != book1_level:
        if book1_level > book2_level: 
            last_level = book1_level
        else: 
            last_level = book2_level
    
    if last_level > booktype[last_book_type]: print("Max tier reached")
    else: print(last_book_type,integerToRoman(last_level))
