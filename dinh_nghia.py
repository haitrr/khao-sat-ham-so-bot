"""
Cac dinh nghia , cong thuc
"""
import xu_ly_chuoi
import ky_hieu_latex


class DinhNghia:
    def __init__(self, ten, noi_dung):
        self.ten = ten
        self.noi_dung = noi_dung


DE_HAM_SO_CO_CUC_TRI = DinhNghia(
    ten="Quan hệ giữa nghiệm của đạo hàm và cực trị của hàm số",
    noi_dung="Để hàm số {hs} có cực trị thì phương trình {dh} có hai nghiệm phân biệt <br> {ct}".format(
        hs=xu_ly_chuoi.boc_mathjax("f(x)"),
        dh=xu_ly_chuoi.boc_mathjax("f''(x)=0"),
        ct=xu_ly_chuoi.boc_mathjax(
            "f(x)" + ky_hieu_latex.TEXT + "{ có cực đại, cực tiểu}" + ky_hieu_latex.SUY_RA +
            "f''(x)=0" + ky_hieu_latex.TEXT + "{ có 2 nghiệm phân biệt}")
    )
)
