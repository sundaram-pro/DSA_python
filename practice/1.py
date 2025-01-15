tempArray = [11,2,23,7,34,9,8,2,4]
tempValue = 0
for temp in range(0,len(tempArray)):
    for i in range(temp+1, len(tempArray)):
        if tempArray[temp] > tempArray[i]:
            tempValue = tempArray[temp]
            tempArray[temp] = tempArray[i]
            tempArray[i] = tempValue
print(temp)