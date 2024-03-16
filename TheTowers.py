max,count = 0,0
x = [int(i) for i in str(input()).split(" ")]
for i in x:
    if i > max:
        max = i
        count += 1
print(count)