#! ข้อ 2
score_list = [3.6, 5.5, 8.7, 9.9, 10.0]
sum = 0
for x in range(len(score_list)) : #! len จำนวนสมาชิกใน list
    sum += score_list[x] #TODO เอาเลขใน list มารวมกัน (x คือ สมาชิกใน list) 
    avg = sum / len(score_list) #TODO ผลรวมมาหารจำนวนใน list
print("ค่าเฉลี่ย = {:.2f}".format(avg))

