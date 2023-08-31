from datetime import date, datetime
now  = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Excuted time: ", dt_string)
name = "Panachat Aiamnam"
std_id = "64107899"
lab = "Quiz3"
print(lab +" Name : "+name+" Student ID: "+std_id)
print("-"*52)

def mobile_bililng(call,data):
    rate_call = call * 2
    rate_data = data * 50
    print("Current charge {} THB".format(rate_call + rate_data))
    return discout(rate_call + rate_data)

def discout(amount):
    if amount <= 500:
        result = amount * 0.03
    elif amount <= 800:
        result = amount * 0.04
    elif amount <= 1000:
        result = amount * 0.05
    elif amount > 1000:
        result = amount * 0.06
    print("Discount {:.2f} THB".format(result)) 
    print("Charge excluded vat. {} THB".format(amount - result))
    return vatable(amount - result)

def vatable (amount):
    tax = amount * 1.07
    print("Total pament {:.2f} THB (vat.7 included)".format(tax))





