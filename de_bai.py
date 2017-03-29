class DeBai():
    def __init__(self):
        self.bai_toan = None
        self.du_kien = dict()

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