my_dict = {}

while True:
    x = str(input())
    if x == 'exit': break
    if x not in my_dict: my_dict[x] = 1
    else: my_dict[x] += 1
        
print("Shopping list")
if my_dict == {}: print("Nothing...")
else:
    for i in my_dict: print(f"Buy {my_dict[i]} {i}")