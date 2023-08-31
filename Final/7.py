import numpy as np
def displayAge(age ):
    i = 1
    for x in age:
        print("Age # {} : {}\n".format(i,x))
        i += 1

age = np.array([10,28,19,12,15])
displayAge(age)