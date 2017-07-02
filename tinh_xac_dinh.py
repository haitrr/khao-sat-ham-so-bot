"""
Tinh xac dinh cua ham so
"""

import phuong_trinh
import sympy
import bat_dang_thuc
import huong_dan_giai
import xu_ly_chuoi
import hang_so


def tim_khong_xac_dinh(ham_so, bien):
    """
    Tim cac gia tri khong xac dinh cua ham so phan thuc
    :param ham_so: 
    :param bien: 
    :return: 
    """
    # Ham da thuc,xac dinh tren R
    if phuong_trinh.loai_ham_so(ham_so, bien) in hang_so.LoaiHamSo.CAC_HAM_DA_THUC:
        return []

    # Ham phan thuc khong xac dinh khi mau bang 0
    else:
        if phuong_trinh.loai_ham_so(ham_so, bien) in hang_so.LoaiHamSo.CAC_HAM_PHAN_THUC:
            mau_so = phuong_trinh.lay_mau_so(ham_so)
            return phuong_trinh.tim_nghiem_thuc(mau_so, bien)
    return []

def tim_tap_xac_dinh(ham_so, bien):
    """
    Tim tap xac dinh cua ham so 
    :param ham_so: 
    :param bien: 
    :return: 
    """
    ham_f = phuong_trinh.tao_ham('f',ham_so,bien)
    loi_giai = huong_dan_giai.LoiGiai("Tìm tập xác định của hàm số {0}".format(
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_f))))

    # Tim loai ham so
    loai_ham = phuong_trinh.loai_ham_so(ham_so, bien)

    # Ham da thuc tap xac dinh la R
    if loai_ham in hang_so.LoaiHamSo.CAC_HAM_DA_THUC:
        txd = sympy.S.Reals
        loi_giai.them_thao_tac("Hàm số là hàm đa thức nên luôn xác định trên tập số thực")
        loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax("D={r}".format(r=xu_ly_chuoi.tao_latex(txd))))
        loi_giai.dap_an=txd

    # Ham phan thuc mau khong xac dinh
    elif loai_ham in hang_so.LoaiHamSo.CAC_HAM_PHAN_THUC:
        # Xac dinh mau so
        dieu_kien = []
        mau_so = phuong_trinh.lay_mau_so(ham_so)
        loi_giai.them_thao_tac("Mẫu số của hàm số là {0}".format(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(mau_so))))

        # Giai lay nghiem cua mau so
        giai_mau = phuong_trinh.giai_phuong_trinh(mau_so,bien)
        loi_giai.them_danh_sach_thao_tac(giai_mau.cac_buoc_giai)
        khong_xac_dinh = giai_mau.dap_an
        for i in khong_xac_dinh:
            dieu_kien.append(sympy.Unequality(bien, i))
        tap_xac_dinh = bat_dang_thuc.giai_he_bat_dang_thuc(dieu_kien, bien)

        # Ket luan
        loi_giai.them_thao_tac("Để hàm số xác định thì mẫu số phải khác 0")
        loi_giai.them_thao_tac("Vậy ta có tập xác định {tap_xd}".format(tap_xd=xu_ly_chuoi.boc_mathjax("D={txd}".format(txd=xu_ly_chuoi.tao_latex(tap_xac_dinh)))))

        loi_giai.dap_an=tap_xac_dinh
    return loi_giai

if __name__ == '__main__':
    import sympy

    hs = sympy.sympify("(x-1)/(x^2+2)")
    x = sympy.Symbol('x')
    tim_tap_xac_dinh(hs,x).xuat_html("loi_giai.html")