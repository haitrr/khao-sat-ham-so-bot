
# Luu du lieu ve de bai do nguoi dung nhap vao
class DeBai:
    def __init__(self):

        # Ham giai toan
        self.bai_toan = None

        # Tu dien chua cac tham so va gia tri tuong ung
        self.du_kien = dict()

        # Bai toan mau
        self.du_kien_mau = None

        # Co can tham so khong?
        self.co_tham_so = False

    def giai(self):
        """
        Giai de
        :return: huong_dan_giai.LoiGiai
        """
        # Chay ham giai toan su dung dictionary parametter
        return self.bai_toan(**self.du_kien)

    def giai_mau(self):
        """
        dua ra loi giai mau cho dang toan
        :param dk:
        :return:
        """
        return self.bai_toan(**self.du_kien_mau)

# Du kien cua bai toan
class DuKien:
    def __init__(self):
        self.ten_du_kien = None
        self.gia_tri = None
        self.chu_thich = None
        # Dung de kiem tra du kien co hop le khong
        self.khop = '.+'

# Yeu cau cua bai toan
class YeuCau:
    def __init__(self, khop, co_tham_so, ham_giai, du_kien):
        # So khop cau lenh cua bai toan
        self.khop = khop
        self.co_tham_so = co_tham_so

        # Ham so dung de giai bai toan
        self.ham_giai = ham_giai

        # Danh sach cac du kien
        self.du_kien = du_kien
