ls = [float(i) for i in str(input()).split(", ")]
x,y = ls[0],ls[1]
result = ""
if (x == 0 and y == 0): result = "the origin point"
elif (x == 0 and y > 0): result = "on y axis"
elif (x == 0 and y < 0): result = "on y axis"
elif (y == 0 and x > 0): result = "on x axis"
elif (y == 0 and x < 0): result = "on x axis"
elif (x > 0 and y > 0): result = "on Quadrant I"  
elif (x < 0 and y > 0): result = "on Quadrant II"
elif (x < 0 and y < 0): result = "on Quadrant III"
elif (x > 0 and y < 0): result = "on Quadrant IV" 
print(f"Point({x:.2f}, {y:.2f}) is {result}")