context = str(input()).replace("-", " ").replace("?", " ").replace("_", " ").split(" ")
final = ''
if context[0] == "": context = context[1::]
for i in range(0,len(context)):
    if i == 0: final += context[i].lower()
    else: final += context[i].title()
print(final)