my_dict = {}
n = int(input())
for i in range(n):
    x = str(input()).split(" - ")
    my_dict[x[0].rstrip()] = 0
    for i in x[1]:
        if (i == "1"): my_dict[x[0].rstrip()] += 1
for key,val in my_dict.items():
    if ((val/10) * 100 < 80):
        print(f"{key}: {(val/10) * 100:.0f} Percent (Failed)")
    else:
        print(f"{key}: {(val/10) * 100:.0f} Percent (Passed)")