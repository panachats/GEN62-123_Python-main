Studnet = {
            'Name':'Panachat',
            'Surename':'Aiamnam',
            'Id':64107899,
            'Age':'19',
            'GPAX':3.90}

Address = {
             'บ้านเลขที่':'138/2',
             'หมู่ที่':'2',
             'ตำบล':'ท่าซัก',
             'อำเภอ':'เมือง',
             'จังหวัด':'นครศรีธรรมราช',
             'รหัสไปรษณีย์':80000}

DataStudent ={
                'Student':Studnet,
                'Address':Address
} 
#? การเข้าถึงข้อมูล
print(DataStudent['Student']['Name'])