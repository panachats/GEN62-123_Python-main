import numpy as np


day1 = np.array ([[70,75,80,88,72,92],
                [99,101,80,85,79,82],
                [100,89,95,120,122,99]])

for i in day1:
    day = 1
    time = 1
    total = 0
    print("day{}".format(day))
    for x in i:
        total += x
        print("time#{} : {} ".format(time,x))
    print("Average : {:.1f} ".format(total / len(i)))
    day += 1
    time += 1
