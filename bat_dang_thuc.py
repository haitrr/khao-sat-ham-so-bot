import sympy


# Giai he bat dang thuc
def giai_he_bat_dang_thuc(he_bat_dang_thuc, bien):
    mien_nghiem_he = sympy.S.Reals
    for bat_dang_thuc in he_bat_dang_thuc:
        mien_nghiem_bdt = sympy.solveset(bat_dang_thuc, bien, sympy.S.Reals)
        mien_nghiem_he = mien_nghiem_he.intersect(mien_nghiem_bdt)
    return mien_nghiem_he


def tong_hop_ket_qua(cac_ket_qua):
    ket_qua_tong_hop = sympy.S.Reals
    for ket_qua in cac_ket_qua:
        ket_qua_tong_hop = ket_qua_tong_hop.intersect(ket_qua)
    return ket_qua_tong_hop


def giai_bat_dang_thuc(bat_dang_thuc, bien):
    return sympy.solve(bat_dang_thuc, bien, sympy.S.Reals)


def giai_bat_dang_thuc_set(he_bat_dang_thuc, bien):
    return sympy.solve_univariate_inequality(he_bat_dang_thuc, bien, relational=False)


def lon_hon_hoac_bang(bieu_thuc_1, bieu_thuc_2):
    return sympy.GreaterThan(bieu_thuc_1, bieu_thuc_2)


def lon_hon(bieu_thuc_1, bieu_thuc_2):
    return sympy.StrictGreaterThan(bieu_thuc_1, bieu_thuc_2)


def nho_hon_hoac_bang(bieu_thuc_1, bieu_thuc_2):
    return sympy.LessThan(bieu_thuc_1, bieu_thuc_2)


def nho_hon(bieu_thuc_1, bieu_thuc_2):
    return sympy.StrictLessThan(bieu_thuc_1, bieu_thuc_2)


def lay_ve_trai(bat_dang_thuc):
    return bat_dang_thuc.lhs


# Lay ve phai cua phuong trinh hoac bat dang thuc
def lay_ve_phai(bat_dang_thuc):
    return bat_dang_thuc.rhs


def bang(bieu_thuc_1, bieu_thuc_2):
    return sympy.Eq(bieu_thuc_1, bieu_thuc_2)
