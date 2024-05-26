length = float(input())
curr = 0.0
rulerLines = ' |'
numberLines = ''

while (curr < length):
    numberLines += (str(curr) + "  ") 
    rulerLines += "----|"
    curr += 0.5
    
numberLines += (str(curr)) 

print(rulerLines)
print(numberLines)