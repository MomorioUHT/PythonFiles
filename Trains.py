RailCars = str(input())
Train = ''
if RailCars.lower() == "true":
    Cars = int(input())
    for i in range(Cars):
        if i == 0: Train += "[1000]-"
        elif i == Cars-1: Train += "[0001]"
        else: Train += "[0000]-"
else:
    Locomotives = int(input())
    PassengerCars = int(input())
    for i in range(Locomotives):
        if PassengerCars == 0: Train += "[1111]"
        else: Train += "[1111]-"
    for i in range(PassengerCars):
        if i == PassengerCars-1: Train += "[0000]"
        else: Train += "[0000]-"    
print(Train)