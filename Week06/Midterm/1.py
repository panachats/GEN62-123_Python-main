fee = 3500
regis_fee = 0
lec_credit = int(input("ค่าหนาวยกิตบรรยาย : "))
leb_credit = int(input("ค่าหนาวยกิตปฎิบัติ : "))
sum_lec = leb_credit * 1000
sum_leb = leb_credit * 750
total = sum_lec + sum_leb

if total + fee <= 5000:
    regis_fee = 5000
elif total + fee > 15000:
    regis_fee = 15000
else:
    regis_fee = total
print("ค่าลงทะเบียน",regis_fee)
    