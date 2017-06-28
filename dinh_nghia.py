"""
Cac dinh nghia , cong thuc
"""
import xu_ly_chuoi


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
DE_HAM_SO_CO_CUC_DAI_TAI_MOT_DIEM = DinhNghia(
    ten='Điều kiện để hàm số có cực đại tại một điểm',
    noi_dung='Để hàm số {fx} có cực đại tại một điểm {x0} thì hàm số đạt cực trị tại {k} và {dh2k}'.format(
        fx=xu_ly_chuoi.boc_mathjax("f(x)"),
        x0=xu_ly_chuoi.boc_mathjax("x_0=k"),
        k=xu_ly_chuoi.boc_mathjax("k"),
        dh2k=xu_ly_chuoi.boc_mathjax("f''(k)>0")
    )
)

DE_HAM_SO_DAT_CUC_TRI_TAI_MOT_DIEM = DinhNghia(
    ten='Điều kiện để hàm số có cực trị tại một điểm',
    noi_dung='Để hàm số {fx} có cực trị tại một điểm {x0} thì đạo hàm {dhk}'.format(
        fx=xu_ly_chuoi.boc_mathjax("f(x)"),
        x0=xu_ly_chuoi.boc_mathjax("x_0=k"),
        dhk=xu_ly_chuoi.boc_mathjax("f'(k)=0")
    )
)
