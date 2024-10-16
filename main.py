#khuôn mẫu
class KhachHang:
    #thuộc tính
    name='Nguyễn Văn A'
    age=20
    gender='Male'

    #phương thức

    def inputInfo(self):
        self.name=input('Nhập tên: ')
        self.age=input('Nhập tuổi: ')
        self.gender=input('Nhập giới tính: ')

    def outputInfo(self):
        print('Tên:',self.name)
        print('Tuổi:',self.age)
        print('Giới tính:',self.gender)

    def setName(self,_name):
        self.name=_name 
    
    def getName(self):
        return self.name
    

#tạo đối tượng

kh1=KhachHang()
kh2=KhachHang()

kh1.inputInfo()
kh1.outputInfo()

print('='*100)
print('Đối tượng 2',kh2.name)
print('Đối tượng 2',kh2.age)
print('Đối tượng 2',kh2.gender)


