ar = [int(i) for i in str(input()).split(" ")]
ar.sort()

final = ""
my_dict = { }
ar2 = []

def convertToNumber(x: int):
    if x == 0: return "zero" 
    if x == 1: return "one" 
    if x == 2: return "two" 
    if x == 3: return "three" 
    if x == 4: return "four" 
    if x == 5: return "five" 
    if x == 6: return "six" 
    if x == 7: return "seven" 
    if x == 8: return "eight" 
    if x == 9: return "nine" 
    if x == 10: return "ten" 
    
for i in ar:
    if i not in ar2: ar2.append(i)

for i in range(0,len(ar)):
    if ar[i] not in my_dict: my_dict[ar[i]] = 1
    else: my_dict[ar[i]] += 1
    
final += "There is "
for i in range(0,len(ar2)):
    final += convertToNumber(my_dict[ar2[i]]) + " " + str(ar2[i])
    if i == len(ar2)-1: final += "."
    else: final += ", "
print(final)