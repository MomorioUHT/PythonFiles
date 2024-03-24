a = [i for i in str(input()).split(" ")]
b = [i for i in str(input()).split(" ")]

if a[0] == "0": x = 0
else:
    if a[1].lower() == 'down' or a[1].lower() == 'left': x = -float(a[0])
    else: x = float(a[0])
        
if b[0] == "0": y = 0
else:    
    if b[1].lower() == 'down' or b[1].lower() == 'left': y = -float(b[0])
    else: y = float(b[0])
    
directions = ''

if (x > 0 and y > 0): directions = "North East"
elif (x > 0 and y == 0): directions = "East"
elif (x > 0 and y < 0): directions = "South East"
elif (x == 0 and y > 0): directions = "North"
#skip 0 0
elif (x == 0 and y < 0): directions = "South"
if (x < 0 and y > 0): directions = "North West"
elif (x < 0 and y == 0): directions = "West"
elif (x < 0 and y < 0): directions = "South West"

print(f"Xingyi should go {directions}")