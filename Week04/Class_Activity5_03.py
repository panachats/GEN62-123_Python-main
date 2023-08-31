# ข้อ 3 
score_list = [3.6, 5.5, 8.7, 9.9, 10.0]
min = 0
sum = 0
for y in range(len(score_list)): #TODO วน 5 รอบ ตามจำนวนใน list ซึ่งมี 5 ตัว
    #! y คือ สมาชิกใน list
    if score_list[y] < 9 : #! คะแนนใน list ที่น้อยกว่า 9 คือ 3.6 5.5 8.7 
        min += 1 #TODO นับจำนวนคนซึ่งมี 3 คน 
        sum += score_list[y] #! y คือ สมาชิกใน list
print("คะแนนเฉลี่ย = {:.2f}".format(sum/min))