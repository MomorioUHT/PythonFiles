height,stepsize = float(input()),float(input())
total,day = 0,0
while (total < height):
    total += 0.8*stepsize
    day+=1
print(f"{day} Days")