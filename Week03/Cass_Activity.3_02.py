deposit = int(input("Enter deposit : "))
if deposit > 100000  :
    interest = deposit * 0.05
elif deposit >= 50001  :
    interest = deposit * 0.04
elif deposit >= 10001   :
    interest = deposit * 0.03
else :
    interest = deposit * 0.02
print('Interest =',int(interest))