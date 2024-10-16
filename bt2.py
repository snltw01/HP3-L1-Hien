class NhanVien:
    def set_ma_nhan_vien(self, ma_nhan_vien):
        self.__ma_nhan_vien = ma_nhan_vien

    def set_info(self, ten, tuoi, dia_chi, luong, gio_lam):
        self.ten = ten
        self.tuoi = tuoi
        self.dia_chi = dia_chi
        self.luong = luong
        self.gio_lam = gio_lam

    def inputInfo(self):
        self.__ma_nhan_vien = input("Nhập mã nhân viên: ")
        self.ten = input("Nhập tên nhân viên: ")
        self.tuoi = int(input("Nhập tuổi nhân viên: "))
        self.dia_chi = input("Nhập địa chỉ: ")
        self.luong = float(input("Nhập lương: "))
        self.gio_lam = int(input("Nhập số giờ làm: "))

    def printInfo(self):
        print(f"Mã NV: {self.__ma_nhan_vien}, Tên: {self.ten}, Tuổi: {self.tuoi}, Địa chỉ: {self.dia_chi}, Lương: {self.luong}, Giờ làm: {self.gio_lam}")

    def tinhThuong(self):
        if self.gio_lam >= 200:
            return self.luong * 0.2
        elif self.gio_lam >= 100:
            return self.luong * 0.1
        else:
            return 0

# Example usage:
nv = NhanVien()
nv.inputInfo()
nv.printInfo()
print(f"Tiền thưởng: {nv.tinhThuong()}")
