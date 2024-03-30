score = 0
correct,your = str(input()).split("-"), str(input()).split("-")
if (len(correct) != len(your)): print("ERROR")
else:
    for i in range(len(your)):
        if your[i] == correct[i]: score += 1
    print(f"Total score = {score}/{len(your)}")