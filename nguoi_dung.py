import de_bai

class NguoiDung:
    """
    Class nguoi dung
    """

    def __init__(self, ma_nguoi_dung):
        """
        Khoi tao mot nguoi dung
        :param ma_nguoi_dung: string
        """
        self.ma_nguoi_dung = ma_nguoi_dung
        self.de_bai = de_bai.DeBai()
        self.loi_giai = None
        self.loi_huong_dan = None
        self.lich_su_chat = list()
        self.buoc = -1
        self.cho = 'ham_so'
