def binSearch(val, data):
    data = sorted(data) 
    bottom = 0
    top = len(data) - 1
    midpoint = (bottom + top) // 2
    found = False

    while (bottom <= top and not found):
        
        midpoint = (bottom + top) // 2
        a = data[midpoint]
        if a == val:
            found = True

        elif a < val:
            bottom = midpoint + 1

        elif a > val:
            top = midpoint - 1

    if (found):
        return midpoint, data

    if (not found):
        return None, data

data = [1,2,1,5,4,57,8]
val = 57

index, data = binSearch(val, data)
if (index != None):
    
    print "Found value at index: ", index
else: print "Value not found"
    
