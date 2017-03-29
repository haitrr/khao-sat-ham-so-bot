
class KichBan():
    def __init__(self,ten_kich_ban):
        self.ten_kich_ban = ten_kich_ban
        self.ket_thuc = False
        self.cac_cau_thoai = list()


class CauThoai():
    def __init__(self,cau_hoi,cho = None,dap_an = None):
        self.cau_hoi = cau_hoi
        self.cho = cho
        self.dap_an = dap_an
