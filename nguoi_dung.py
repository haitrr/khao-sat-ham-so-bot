import de_bai


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

        # Loi giai cua bai toan
        self.loi_giai = None
        self.loi_huong_dan = None

        # Lich su chat
        self.lich_su_chat = list()

        # buoc giai hien tai
        self.buoc = -1
        self.cho = 'ham_so'
