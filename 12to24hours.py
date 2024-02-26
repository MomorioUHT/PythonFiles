ls = [i for i in str(input()).replace(" ",":").split(":")]
hours = int(ls[0])
minutes = int(ls[1])
if (ls[-1].lower() == "am" and hours == 12): hours = 0
elif (ls[-1].lower() == "pm" and hours != 12): hours += 12
print(f"24-hour time is {hours:02d}:{minutes:02d}")