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
    noi_dung="Để hàm số {hs} có cực trị thì phương trình {dh} có hai nghiệm phân biệt".
    format(
        hs=xu_ly_chuoi.boc_mathjax("f(x)"),
        dh=xu_ly_chuoi.boc_mathjax("f'(x)=0")))
DE_HAM_SO_CO_CUC_DAI_TAI_MOT_DIEM = DinhNghia(
    ten='Điều kiện để hàm số có cực đại tại một điểm',
    noi_dung='Để hàm số {fx} có cực đại tại một điểm {x0} thì hàm số đạt cực trị tại {k} và {dh2k}'.
    format(
        fx=xu_ly_chuoi.boc_mathjax("f(x)"),
        x0=xu_ly_chuoi.boc_mathjax("x_0=k"),
        k=xu_ly_chuoi.boc_mathjax("k"),
        dh2k=xu_ly_chuoi.boc_mathjax("f''(k)>0")))

# todo: test
DE_HAM_SO_CO_CUC_TIEU_TAI_MOT_DIEM = DinhNghia(
    ten='Điều kiện để hàm số có cực tiểu tại một điểm',
    noi_dung='Để hàm số {fx} có cực tiểu tại một điểm {x0} thì hàm số đạt cực trị tại {k} và {dh2k}'.
    format(
        fx=xu_ly_chuoi.boc_mathjax("f(x)"),
        x0=xu_ly_chuoi.boc_mathjax("x_0=k"),
        k=xu_ly_chuoi.boc_mathjax("k"),
        dh2k=xu_ly_chuoi.boc_mathjax("f''(k)<0")))

DE_HAM_SO_DAT_CUC_TRI_TAI_MOT_DIEM = DinhNghia(
    ten='Điều kiện để hàm số có cực trị tại một điểm',
    noi_dung='Để hàm số {fx} có cực trị tại một điểm {x0} thì đạo hàm {dhk}'
    .format(
        fx=xu_ly_chuoi.boc_mathjax("f(x)"),
        x0=xu_ly_chuoi.boc_mathjax("x_0=k"),
        dhk=xu_ly_chuoi.boc_mathjax("f'(k)=0")))

# todo: Test
DE_HAM_SO_CO_CUC_TRI_NAM_O_HAI_PHIA_TRUC_TUNG = DinhNghia(
    ten='Điều kiện để hàm số có cực trị nằm ở hai phía trục tung',
    noi_dung='Để hàm số {fx} có cực trị nằm ở hai phía trục tung thì {fx} đạt cực trị tại điểm {x1} và {x2} sao cho {dk}'.
    format(
        fx=xu_ly_chuoi.boc_mathjax('f(x)'),
        x1=xu_ly_chuoi.boc_mathjax('x_1'),
        x2=xu_ly_chuoi.boc_mathjax('x_2'),
        dk=xu_ly_chuoi.boc_mathjax('x_1 x_2<0')))

# todo: Test
DE_HAM_SO_CO_CUC_TRI_NAM_O_HAI_PHIA_TRUC_HOANH = DinhNghia(
    ten='Điều kiện để hàm số có cực trị nằm ở hai phía trục hoành',
    noi_dung='Để hàm số {fx} có cực trị nằm ở hai phía trục hoành thì {fx} đạt cực trị tại điểm {x1} và {x2} sao cho {dk}'.
    format(
        fx=xu_ly_chuoi.boc_mathjax('f(x)'),
        x1=xu_ly_chuoi.boc_mathjax('(x_1,y_1)'),
        x2=xu_ly_chuoi.boc_mathjax('(x_2,y_2)'),
        dk=xu_ly_chuoi.boc_mathjax('y_1 y_2<0')))

# todo: Test
DE_HAM_SO_DONG_BIEN_TREN_TAP_XAC_DINH = DinhNghia(
    ten="Điều kiện để hàm số đồng biến trên tập xác định",
    noi_dung="Để hàm số {hs} đồng biến trên tập xác định thì {dkdh}".format(
        hs=xu_ly_chuoi.boc_mathjax('f(x)'),
        dkdh=xu_ly_chuoi.boc_mathjax("f'(x)>=0 \\forall x\in\mathbb{R}")))

# todo: Test
DE_HAM_SO_NGHICH_BIEN_TREN_TAP_XAC_DINH = DinhNghia(
    ten="Điều kiện để hàm số nghịch biến biến trên tập xác định",
    noi_dung="Để hàm số {hs} nghịch biến trên tập xác định thì {dkdh}".format(
        hs=xu_ly_chuoi.boc_mathjax('f(x)'),
        dkdh=xu_ly_chuoi.boc_mathjax("f'(x)<=0 \\forall x\in\mathbb{R}")))

# todo: Test
DE_HAM_SO_DON_DIEU_TREN_MOT_KHOANG_CO_DO_DAI_CHO_TRUOC = DinhNghia(
    ten='Điều kiện để hàm số đơn điệu trên một khoảng cho trước',
    noi_dung="Để hàm số {hs} đơn điệu trên một khoảng {k} cho trước thì {dh} có hai nghiệm phân biệt tại {x1x2} sao cho {dk}".
    format(
        hs=xu_ly_chuoi.boc_mathjax("f(x)"),
        k=xu_ly_chuoi.boc_mathjax('k'),
        dh=xu_ly_chuoi.boc_mathjax("f'(x)"),
        x1x2=xu_ly_chuoi.boc_mathjax("x_1,x_2"),
        dk=xu_ly_chuoi.boc_mathjax('|x_1-x_2|=k')))

# todo: Test
DINH_LY_VI_ET = DinhNghia(
    ten="Định lý Vi-et",
    noi_dung="Nếu phương trình bậc hai có hai nghiệm phân biệt {nghiem} thì {ct1} và {ct2}".
    format(
        nghiem=xu_ly_chuoi.boc_mathjax("x_1,x_2"),
        ct1=xu_ly_chuoi.boc_mathjax("x_1+x_2=\\frac{c}{a}"),
        ct2=xu_ly_chuoi.boc_mathjax("x_1\cdot x_2=\\frac{-b}{a}")))

# todo: Test
GIAO_DIEM_CUA_DO_THI_HAM_SO_VOI_DUONG_THANG = DinhNghia(
    ten="Giao điểm của đồ thị hàm số với một đường thẳng",
    noi_dung="Giao điểm của đồ thị hàm số {hs} với đường thẳng {dt} là nghiệm của phương trình hoành độ giao điểm {pt}".
    format(
        hs=xu_ly_chuoi.boc_mathjax("f(x)"),
        dt=xu_ly_chuoi.boc_mathjax("d"),
        pt=xu_ly_chuoi.boc_mathjax("f(x)=d")))

# todo: test
DE_DO_THI_HAM_SO_CAT_TRUC_HOANH_TAI_MOT_DIEM_DUY_NHAT = DinhNghia(
    ten="Điều kiện để đồ thị hàm số cắt trục hoành tại một điểm duy nhất",
    noi_dung="{th1}<br>{th2}".format(
        th1="Trường hợp 1:<br>{nd}".format(nd="Hàm số không có cực trị"),
        th2="Trường hợp 2:<br>{nd}".format(
            nd="Hàm số có hai cực trị nằm ở hai phía của trục hoành")))

# todo: test
'''
Định nghĩa về dạng của phương trình tiếp tuyến của đồ thị
hàm số tại một điểm cho trước
'''
PHUONG_TRINH_TIEP_TUYEN_TAI_MOT_DIEM_CHO_TRUOC = DinhNghia(
    ten="Dạng của phương trình tiếp tuyến",
    noi_dung="Phương trình đường tiếp tuyến với đồ thị hàm số {hs} tại điểm {d} là {pt}".
    format(
        hs=xu_ly_chuoi.boc_mathjax("f(x)"),
        d=xu_ly_chuoi.boc_mathjax("x_0"),
        pt=xu_ly_chuoi.boc_mathjax("f'(x_0)(x-x_0)+f(x_0)")))
