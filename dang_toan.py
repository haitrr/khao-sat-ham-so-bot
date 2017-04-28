class DangToan():
    def __init__(self, khop, ten, can_tham_so, loai_ham_so, ham_giai, cac_du_kien):
        self.khop = khop
        self.ten  = ten
        self.can_tham_so = can_tham_so
        self.loai_ham_so = loai_ham_so
        self.ham_giai = ham_giai
        self.cac_du_kien = list()
        for du_kien in cac_du_kien:
            self.cac_du_kien.append(DuKien(du_kien[0],du_kien[1]))


class DuKien():
    def __init__(self,ten_du_kien,mo_ta):
        self.ten_du_kien = ten_du_kien
        self.mo_ta = mo_ta