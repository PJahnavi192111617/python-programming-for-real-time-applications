def isIso(x,y):
    if len(x) != len(y):
        return False
    for i in range(len(x)):
        count = 0
        if x.count(x[i]) != y.count(y[i]):
            return False
    return True
print(isIso("food","good"))
print(isIso("poor","bad"))
print(isIso("food","bad"))
print(isIso("poor","good"))
    
