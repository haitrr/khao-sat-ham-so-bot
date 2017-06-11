"""
Cac dinh nghia , cong thuc
"""
import xu_ly_chuoi
import ky_hieu_latex


class DinhNghia:
    def __init__(self, ten, noi_dung):
        self.ten = ten
        self.noi_dung = noi_dung

    def xuat(self):
        return self.ten + "<br>" + self.noi_dung

DE_HAM_SO_CO_CUC_TRI = DinhNghia(
    ten="Quan hệ giữa nghiệm của đạo hàm và cực trị của hàm số",
    noi_dung="Để hàm số {hs} có cực trị thì phương trình {dh} có hai nghiệm phân biệt".format(
        hs=xu_ly_chuoi.boc_mathjax("f(x)"),
        dh=xu_ly_chuoi.boc_mathjax("f'(x)=0")
    )
)