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
        self.bieu_thuc_hien_tai = None
        self.loi_giai_hien_tai = None
        self.lich_su_chat = list()
        self.buoc_hien_tai = -1
        self.dang_cho = None
        self.bai_toan = None
        self.bien = None
        self.tham_so = None
