datedata,datenumber = [],[]
WrongDay,WrongMonth = False,False
sundaycount = 0

monthdatabase = {1: 0,2: 31,3: 59,4: 90,5: 120,6: 151,7: 181,8: 212,9: 243,10: 273,11: 304,12: 334}

datedata.append(str(input()).split("-"))
datedata.append(str(input()).split("-"))
startdate = int(input())

if int(datedata[0][0]) > 31 or int(datedata[1][0]) > 31: WrongDay = True 
if int(datedata[0][1]) > 12 or int(datedata[1][1]) > 12: WrongMonth = True
if startdate > 31: WrongDay = True

if not WrongMonth and not WrongDay:
    for i in datedata: 
        datenumber.append(int(i[0])+monthdatabase[int(i[1])])
    datenumber.sort()
    loopy = []
    for i in range(datenumber[0],datenumber[1]+1): loopy.append(i)
    for i in range(startdate,366,7):
        if i in loopy: sundaycount += 1
    print(sundaycount)
else:   
    if WrongMonth: print("Wrong Month")
    if WrongDay: print("Wrong Day")