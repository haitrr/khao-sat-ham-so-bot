import sympy


def tim_gioi_han_tai_vo_cuc(ham_so, bien):
    am_vo_cuc = sympy.limit(ham_so, bien, -sympy.oo)
    duong_vo_cuc = sympy.limit(ham_so, bien, sympy.oo)
    return am_vo_cuc, duong_vo_cuc


def tim_gioi_han_hai_phia(ham_so, bien, diem):
    gioi_han_trai = sympy.limit(ham_so, bien, diem, '-')
    gioi_han_phai = sympy.limit(ham_so, bien, diem, '+')
    return gioi_han_trai, gioi_han_phai


def tim_gioi_han_duong(ham_so, bien, diem):
    """
    tìm giới hạn phải của hàm số
    """
    return sympy.limit(ham_so, bien, diem, '+')
