import sympy


def giai_he_bat_dang_thuc(he_bat_dang_thuc, bien):
    mien_nghiem_he = sympy.S.Reals
    for bat_dang_thuc in he_bat_dang_thuc:
        mien_nghiem_bdt = sympy.solveset(bat_dang_thuc, bien, sympy.S.Reals)
        mien_nghiem_he = mien_nghiem_he.intersect(mien_nghiem_bdt)
    return mien_nghiem_he
