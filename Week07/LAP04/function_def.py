
#* Lap 04 - 1 Week 07
#TODO สร้าง func และ เก็บ parameter radius
def calculate_circle_area(radius):
    PI = 3.14
    area = PI*(radius*radius) #TODO คำนวณและเก็บไว้ใน area
    print("Circle radius {}, area is {}". format(radius,area))

#TODO สร้าง func และ เก็บ parameter radius
def calculate_circle_circumference(radius):
    PI = 3.14
    circumference = 2*PI*radius #TODO คำนวณและเก็บไว้ใน circumference
    print("Circle radius {}, circumference is {}".format(radius,circumference))

#TODO สร้าง func และ เก็บ parameter wide and lenght
def calculate_retangle_area(wide,length):
    area = wide*length #TODO คำนวณและเก็บไว้ใน area
    print("Retangle area of {} X {} is {}".format(wide,length,area))

#TODO สร้าง func และ เก็บ parameter base and high
def calculate_triangle_area(base,high):
    area = 0.5*base*high #TODO คำนวณและเก็บไว้ใน area
    print("Triangle are of {} X {} is {}".format(base,high,area))
