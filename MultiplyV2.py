n = int(input())
if len(str(n*12)) == 2:
    for i in range(1,13): print(f"{n} x {i:2d} = {n*i:2d}")
if len(str(n*12)) == 3:
    for i in range(1,13): print(f"{n} x {i:2d} = {n*i:3d}")
if len(str(n*12)) == 4:
    for i in range(1,13): print(f"{n} x {i:2d} = {n*i:4d}")
if len(str(n*12)) == 5:
    for i in range(1,13): print(f"{n} x {i:2d} = {n*i:5d}")
if len(str(n*12)) == 6:
    for i in range(1,13): print(f"{n} x {i:2d} = {n*i:6d}")
if len(str(n*12)) == 7:
    for i in range(1,13): print(f"{n} x {i:2d} = {n*i:7d}")