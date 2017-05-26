import de_bai
import huong_dan_giai
import trac_nghiem

# Nguoi dung
class NguoiDung:
    """
    Class nguoi dung
    """

    def __init__(self, ma_nguoi_dung):
        """
        Khoi tao mot nguoi dung
        :param ma_nguoi_dung: string
        """

        # Ma nguoi dung de phan biet khi nhieu nguoi cung su dung
        self.ma_nguoi_dung = ma_nguoi_dung

        # De bai nguoi dung nhap vao
        self.de_bai = de_bai.DeBai()

        # Cau hoi trac nghiem dang lam
        self.trac_nghiem = None     # type: trac_nghiem.BaiToanTracNghiem

        # Loi giai cua bai toan
        self.loi_giai = None    # type: huong_dan_giai.LoiGiai
        self.loi_huong_dan = None

        # Lich su chat
        self.lich_su_chat = list()

        # Tien trinh giai
        self.tien_trinh = []

        # buoc giai hien tai
        self.buoc = -1
        self.cho = 'ham_so'

    def lay_buoc_hien_tai(self):
        """ 
        Lay buoc giai hien tai dang huong dan
        :return: huong_dan_giai.LoiGiai
        """
        if self.loi_giai.lop_cuoi:
            return self.loi_giai
        if self.tien_trinh == []:
            return self.loi_giai
        buoc_hien_tai = self.loi_giai
        for lop in self.tien_trinh:
            buoc_hien_tai = buoc_hien_tai.cac_buoc_giai[lop]
        return buoc_hien_tai

    def lay_buoc_cha_cua_buoc_hien_tai(self):
        """
        Lay buoc cha cua buoc hien tai
        :return: huong_dan_giai.LoiGiai
        """
        if self.tien_trinh == []:
            return None
        buoc_hien_tai = self.loi_giai
        for lop in self.tien_trinh[:-1]:
            buoc_hien_tai = buoc_hien_tai.cac_buoc_giai[lop]

        return buoc_hien_tai


    def xuat_ten_buoc(self):
        """
        Xuat ten buoc hien tai
        :return str:
        """
        if self.loi_giai.lop_cuoi:
            return 'Bài giải'

        if self.tien_trinh == []:
            return ""

        ten_buoc = 'Bước '
        for lop in self.tien_trinh:
            ten_buoc+=str(lop+1)+'.'

        ten_buoc=ten_buoc[:-1]
        ten_buoc+=' : '
        return ten_buoc
