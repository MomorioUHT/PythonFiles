my_dict = {}
while True:
    x = str(input()).lower()
    if x == "-1": break   
    if x not in my_dict: my_dict[x] = 1
    else: my_dict[x] += 1
print("Result")
for i in my_dict: print(f"{i.title()}: {my_dict[i]}")
