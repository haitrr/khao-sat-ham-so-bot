import phuong_trinh
import sympy
import bat_dang_thuc


def tim_khong_xac_dinh(ham_so, bien):
    # Ham da thuc,xac dinh tren R
    if phuong_trinh.loai_ham_so(ham_so, bien) in phuong_trinh.ham_da_thuc:
        return []

    # Ham phan thuc khong xac dinh khi mau bang 0
    else:
        if phuong_trinh.loai_ham_so(ham_so, bien) == "ham_phan_thuc":
            mau_so = phuong_trinh.lay_mau_so(ham_so)
            return phuong_trinh.tim_nghiem_thuc(mau_so, bien)


def tim_tap_xac_dinh(ham_so, bien):
    loai_ham = phuong_trinh.loai_ham_so(ham_so, bien)

    # Ham da thuc tap xac dinh la R
    if loai_ham in phuong_trinh.ham_da_thuc:
        return sympy.S.Reals

    # Ham phan thuc mau khong xac dinh
    elif loai_ham == "ham_phan_thuc":
        dieu_kien = []
        mau_so = phuong_trinh.lay_mau_so(ham_so)
        khong_xac_dinh = phuong_trinh.tim_nghiem_thuc(mau_so, bien)
        for i in khong_xac_dinh:
            dieu_kien.append(sympy.Unequality(bien, i))
        tap_xac_dinh = bat_dang_thuc.giai_he_bat_dang_thuc(dieu_kien, bien)
        return tap_xac_dinh
    else:
        return "Loi"
