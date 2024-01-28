import math
height = float(input())
stepsize = float(input())
totaltick = math.ceil(height/(0.8*stepsize))
print(f"{totaltick} Days")
