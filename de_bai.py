class DeBai():
    def __init__(self):
        self.bai_toan = None
        self.du_kien = dict()
        self.co_tham_so = False

    def giai(self):
        """
        Giai de
        :return: huong_dan_giai.LoiGiai
        """
        return self.bai_toan(**self.du_kien)


class DuKien():
    def __init__(self,ten_du_kien,chu_thich):
        self.ten_du_kien = None
        self.gia_tri = None
        self.chu_thich = None
        self.khop = '.+'

class YeuCau():
    def __init__(self,khop,co_tham_so,ham_giai,du_kien):
        self.khop=khop
        self.co_tham_so = co_tham_so
        self.ham_giai = ham_giai
        self.du_kien = du_kien