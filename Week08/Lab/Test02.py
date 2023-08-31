import keyboard
'''
def validate_person_id (id): #TODO ประกาศ func
    sum_digit = 0
    count = 13
    for x in range(len(id)):
        if count == 1:
            last_digit = int(id[x])
            break
        sum_digit += int(id[x])*count
        count -= 1
    mod = sum_digit % 11
    check_digit = (11 - mod)%10
    if check_digit == last_digit :
        return True
    else:
        return False
print(validate_person_id('1800101352582'))




def get_email (): #TODO ประกาศ func
    input_email = input("Enter your email : ") #TODO รับค่า
    check_at = input_email.count('@') #TODO เช็คว่า @ มีกี่ตัวใน input_email แล้วเก็บค่าใน check_at
    dot = False #TODO กำหนดให้เป็น false
    if input_email[0] == '@': #TODO เช็คว่า index ที่ 0 เท่ากับ @ ไหม
        print('Error')
        return get_email() #TODO ให้ return กลับไปทำ func ใหม่
    if check_at > 1: #TODO เช็คว่าค่า @ มีมากกว่า 1 ตัวรึป่าว
        print("Error")
        return get_email() #TODO ให้ return กลับไปทำ func ใหม่
    for x in input_email: #TODO loop ใน str 
        if check_at == 1 and x == '.': #TODO เช็คว่า @ มีค่าเท่ากับ 1 ตัวไหม และ x ที่วนนั้นมี . ไหม
            dot = True #TODO ถ้า if ข้างบนถูก ให้เปลี่ยนเป็น True
            print("Succes")
    if dot : #TODO ถ้าค่าเป็น True จะทำ
        return input_email #TODO return ค่ากลับไปแสดงมรส่วนของการเรียก func
    return get_email() #TODO ให้ return กลับไปทำ func ใหม่    

'''


