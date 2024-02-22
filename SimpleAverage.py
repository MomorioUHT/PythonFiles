sum,count = 0,0
while True:
    score = int(input())
    if score == -1: break
    sum += score
    count+=1
if count == 0: print("0.00")
else: print(f"{sum/count:.2f}")