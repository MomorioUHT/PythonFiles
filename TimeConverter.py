time = int(input())
days = time//1440
hours = (time%1440)//60
minutes = (time%1440)%60

day_s,hour_s,minute_s = "","",""

if days != 1: day_s = "s"
if hours != 1: hour_s = "s"
if minutes != 1: minute_s = "s"

if days == 0:
    if minutes == 0: print(f"Last online: {hours} hour{hour_s} ago.")
    elif hours == 0: print(f"Last online: {minutes} minute{minute_s} ago.")
    else: print(f"Last online: {hours} hour{hour_s} {minutes} minute{minute_s} ago.")
else:
    if hours == 0 and minutes == 0: print(f"Last online: {days} day{day_s} ago.")
    elif hours == 0: print(f"Last online: {days} day{day_s} {minutes} minute{minute_s} ago.")
    elif minutes == 0: print(f"Last online: {days} day{day_s} {hours} hour{hour_s} ago.")
    else: print(f"Last online: {days} day{day_s} {hours} hour{hour_s} {minutes} minute{minute_s} ago.")