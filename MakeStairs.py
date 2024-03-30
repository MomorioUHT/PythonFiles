x = int(input())
if x == 0: print("__")
else:
  space_needed = x*3
  print(f"{' '*space_needed}__")
  space_needed-=3
  for i in range(0,x):
    print(f"{' '*space_needed}__|")
    space_needed-=3