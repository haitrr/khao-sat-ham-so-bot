from bieu_thuc import *
from bat_dang_thuc import *

def khong_xac_dinh(ham_so, bien):

    # Ham da thuc,xac dinh tren R
    if loai_ham_so(ham_so, bien) in ham_da_thuc:
        return []

    # Ham phan thuc khong xac dinh khi mau bang 0
    else:
        if loai_ham_so(ham_so, bien) == "ham_phan_thuc":
            mau_so = lay_mau_so(ham_so)
            return tim_nghiem_thuc(mau_so, bien)


def tap_xac_dinh(ham_so, bien):
    loai_ham = loai_ham_so(ham_so, bien)

    # Ham da thuc tap xac dinh la R
    if loai_ham in ham_da_thuc:
        return sympy.S.Reals

    # Ham phan thuc mau khong xac dinh
    elif loai_ham == "ham_phan_thuc":
        dieu_kien = []
        mau_so = lay_mau_so(ham_so)
        khong_xac_dinh = tim_nghiem_thuc(mau_so, bien)
        for i in khong_xac_dinh:
            dieu_kien.append(sympy.Unequality(bien, i))
        tap_xac_dinh = giai_he_bat_dang_thuc(dieu_kien, bien)
        return tap_xac_dinh
    else:
        return "Loi"