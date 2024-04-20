IP = str(input()).split(".")

def isValidIpAddress(context: list):
    if len(context) != 4 : return "No"
    for i in context:
        if len(i) == 0 or int(i) > 255: return "No"
    return "Yes"

print(isValidIpAddress(IP))     