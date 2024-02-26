ls1 = [float(i) for i in str(input()).split(" ")]
ls2 = [float(i) for i in str(input()).split(" ")]

def add_complex(list1: list, list2: list):
    result_x = list1[0] + list2[0]
    result_y = list1[1] + list2[1]
    return [result_x, result_y]

x,y = add_complex(ls1,ls2)
if x == 0 and y == 0: print("A + B = 0.0")
elif x == 0: print(f"A + B = {y:.1f}i")
elif y == 0: print(f"A + B = {x:.1f}")
elif y < 0: print(f"A + B = {x} - {-y:.1f}i")
else: print(f"A + B = {x:.1f} + {y:.1f}i")