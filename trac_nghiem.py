import huong_dan_giai
import dang_toan
import xu_ly_chuoi
import de_bai
import phuong_trinh
import sympy
import khao_sat_ham_so


class BaiToanTracNghiem():
    def __init__(self, de_bai:str, dap_an: list, dap_an_dung: int,ham_giai,du_kien : dict):
        self.de_bai = de_bai
        self.cac_dap_an = list()
        self.dap_an_dung = None
        self.tao_dap_an(dap_an,dap_an_dung)
        self.ham_giai = ham_giai
        self.du_kien = du_kien

    def tao_dap_an(self,dap_an,dap_an_dung):
        cac_ky_hieu = ['A','B','C','D','E','F','G','H']
        for da,gt in enumerate(dap_an):
            self.cac_dap_an.append(DapAnTracNgiem(cac_ky_hieu[da],gt))
        self.dap_an_dung = cac_ky_hieu[dap_an_dung]

    def xuat_dap_an(self):
        cac_dap_an_text = ""
        for da in self.cac_dap_an:
            cac_dap_an_text+=da.xuat_chuoi()+"<br>"

        return cac_dap_an_text[:-1]


    def giai_chi_tiet(self):
        return self.ham_giai(**self.du_kien).xuat_html()

class DapAnTracNgiem():
    def __init__(self,ten:str,gia_tri:str):
        self.ten = ten
        self.gia_tri = gia_tri

    def xuat_chuoi(self):
        return self.ten +". "+self.gia_tri

x= sympy.Symbol('x')
cac_cau_hoi_trac_nghiem = [
    [
        "Giải phương trình",
        [
            "Logarit",
            [
                BaiToanTracNghiem(
                    "Phương trình {pt} có bao nhiêu nghiệm ?".format(
                        pt=xu_ly_chuoi.boc_mathjax("\log_2\left(4\cdot x\\right)-\log_{\\frac{x}{2}}=3"
                                                   )),
                    ["1 nghiệm","vô nghiệm","2 nghiệm","3 nghiệm"],
                    2,
                    phuong_trinh.giai_phuong_trinh,
                    {'bieu_thuc':sympy.Eq(sympy.log(4*x,2) - sympy.log(2,x/2),3),'bien':x}
                )
            ]
        ]
    ],
    [
        "Tính đơn điệu",
        [
            BaiToanTracNghiem(
                "Hàm số {hs} nghịch biến trên khoảng nào".format(
                    hs = xu_ly_chuoi.boc_mathjax("x^4-2\cdot x^2-7")
                ),
                ["(0;1)", "(0;+oo)", "(-1;0)", "(-oo;0)"],
                0,
                khao_sat_ham_so.khao_sat_ham_so,
                {'ham_so':x**4-2*x**2-7,'bien':x}
            )
        ]
    ]
]
