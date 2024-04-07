ls = [int(i) for i in str(input()).split(" ") if i != ""]
ls.sort()
print(*ls)