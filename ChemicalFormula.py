database = {}
context,find = str(input()),str(input())

def numberSearch(text: str):
    if text[0].isalpha(): return 1
    amount = ''
    for i in text:
        if i.isdigit(): amount += i
        if i.isalpha(): break
    return int(amount)
        
def elementSearch(text: str):
    if len(text) == 1: return text
    final = ''
    for i in range(len(text)-1):
        if text[i+1].islower(): final = text[i]+text[i+1]
        if text[i+1].isupper(): final = text[i]
        if text[i+1].isdigit():
            if i == 1: final = text[0]+text[1]
            if i == 0: final = text[0]
        break
    return final
    
def LenOfTwoSearch(text: str):        
    if text[0] == text[1]: 
        if text[0] not in database: database[text[0]] = 2
        else: database[text[0]] += 2       
    elif text[0].isupper() and text[1].isupper():
        if text[0] not in database: database[text[0]] = 1
        else: database[text[0]] += 1  
        if text[1] not in database: database[text[1]] = 1
        else: database[text[1]] += 1 
    elif text[0].isupper() and text[1].islower():
        if text not in database: database[text] = 1
        else: database[text] += 1   
    elif text[0].isalpha() and text[1].isdigit(): 
        if text[0] not in database: database[text[0]] = int(text[1]) 
        else: database[text[0]] += int(text[1])  
    return  

def extract_Chemical(formula: str):
    global database
    while len(formula) > 2:
        headElement = elementSearch(formula)
        formula = formula[len(headElement)::]
        amount = numberSearch(formula)
        
        if amount > 1: formula = formula[len(str(amount))::]
        
        if headElement not in database: database[headElement] = amount
        else: database[headElement] += amount
    
    if len(formula) == 1:
        if formula not in database: database[formula] = 1
        else: database[formula] += 1
    if len(formula) == 2: LenOfTwoSearch(formula) 

extract_Chemical(context)

if find not in database: print("0")
else: print(database[find])

