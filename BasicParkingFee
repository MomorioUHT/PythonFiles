hours = int(input())
minute = int(input())
time = (hours*60)+minute
if (time <= 15): print("0.00")
elif (15 <= time <= 120): print("10.00")
else:
    if (time%60 == 0): newhours = hours
    else: newhours = hours+1
    fee = ((newhours - 2)*10) + 10
    print(f"{fee:.2f}")
