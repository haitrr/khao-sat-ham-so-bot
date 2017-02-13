import sympy as sp 


def giai_he_bat_dang_thuc(he_bat_dang_thuc,bien):
    mien_nghiem_he = sp.S.Reals
    for bat_dang_thuc in he_bat_dang_thuc:
        mien_nghiem_bdt = sp.solveset(bat_dang_thuc,bien,sp.S.Reals)
        mien_nghiem_he = mien_nghiem_he.intersect(mien_nghiem_bdt)
    return mien_nghiem_he
        
