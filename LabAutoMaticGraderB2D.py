result = ''
labcase,yours = [],[]

while True:
    x = str(input())
    if x == '======END======': break
    else: labcase.append(x)

while True:
    x = str(input())
    if x == '======END======': break
    else: yours.append(x)

for i in range(0,len(labcase)):
    if labcase[i] == yours[i]: result += "P"
    else: result += "-"

correct,wrong = 0,0
for i in result: 
    if i == "P": correct += 1
    else: wrong += 1
percentage = (correct/(correct+wrong))*100

print(f"Lab Result: [{result}]")
print(f"Meaning: {correct} Passed {wrong} Failed")
print(f"Percentage: {percentage:.2f}")