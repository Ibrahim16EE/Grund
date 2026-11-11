def nameAnalyze():

 listnames = ["Stina", "Ibrahim", "Pelle"]
 return listnames


def add_Temperature_to_TemperatureList(temp):
        temp = 24
        temperatureList = [32, 45, 67, 89]
        temperatureList.append(temp)
        return temperatureList

def meanValue():
    myList = add_Temperature_to_TemperatureList(24)
    sum = 0
    for number in myList:
        sum = sum + number  
    mean = sum / len(myList)
    return mean
