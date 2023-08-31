import numpy as np
def avgAge(age,n):
    avg = 0
    sumAge = 0
    for x in age:
        sumAge += x
    avg = sumAge / n
    return avg

age = [10,28,19,12,15]
print(avgAge(age,len(age)))


def displayAge(age ):
    i = 1
    for x in age:
        print("Age # {} : {}\n".format(i,x))
        i += 1

avg = 0
avg = avgAge(age,len(age))
print(avg)
displayAge(age)