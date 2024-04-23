ls = []
amount = int(input())
for i in range(amount):
    ls.append(str(input()))
if len(ls) == 1: print(ls[0])
else: 
    result = ', '.join(ls[0:-1]) + " and " + ls[-1]
    print(result)