PreMath = int(input("คะแนน Pre-MATH : "))
if PreMath > 80 :
    print("Excellent")
elif PreMath > 50 :
    print("PASS")
elif PreMath < 50 and PreMath >= 40 :
    print("PASS with condition")
else:
    print("FAIL, Test Again")