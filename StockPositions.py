amount = int(input())
ls = []
for i in range(amount):
  x = str(input())
  ls.append(x)
find = str(input())

res = ""
for i in range(0,len(ls)):
  if ls[i] == find: 
      res += str(i+1) + ","

if res.endswith(","): res = res[0:-1]
print(f"Position: {res}")