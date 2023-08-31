
def room (hours):
    pay = 0
    days = (hours // 24) * 2000
    pay = (hours % 24)*150
    return days + pay
hours = int(input("Enter your hours : "))
x = room(hours)
print(x)

