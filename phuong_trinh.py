import sympy

import bat_dang_thuc
import hang_so
import huong_dan_giai
import ky_hieu_latex
import xu_ly_chuoi


# Rut gon ham so
def rut_gon(ham_so):
    ham_so = ham_so.doit()
    return sympy.simplify(ham_so)


def rut_gon_bieu_thuc(ham_so, **kwargs):
    loi_giai = huong_dan_giai.LoiGiai("Rút gọn biểu thức {bt}".format(
        bt=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_so))
    ))
    if str(rut_gon(ham_so)) == str(ham_so):
        loi_giai.them_thao_tac("Hàm số đã tối giản")
        return loi_giai
    loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_so)))
    loi_giai.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(rut_gon(ham_so))))
    return loi_giai


# so sanh 2 bieu thuc
def so_sanh(bieu_thuc_1, bieu_thuc_2):
    if bieu_thuc_1 == bieu_thuc_2:
        return True
    try:
        if rut_gon(bieu_thuc_1 - bieu_thuc_2) == 0:
            return True
        else:
            return False
    except:
        return False


# Tim nghiem thuc cua ham so
def tim_nghiem_thuc(ham_so, bien):
    # Nghiem bao gom ca phuc va thuc
    nghiem = sympy.solve(ham_so, bien)

    # loc ra cac nghiem thuc
    nghiem_thuc = []
    for i in nghiem:
        if i.is_real is True or (i.is_real is None and not i.is_complex):
            if str(i).find("CRootOf") != -1:
                nghiem_thuc.append(sympy.N(i))
            nghiem_thuc.append(i)
    return nghiem_thuc


def lay_mau_so(ham_so):
    return sympy.denom(ham_so)


def loai_ham_so(ham_so, bien=None):
    # Dang thu , chua biet
    cac_bien = list(ham_so.free_symbols)
    if len(cac_bien) > 2:
        return None
    elif len(cac_bien) == 0:
        return None
    elif len(cac_bien) == 1 or (len(cac_bien) == 2 and bien != None):
        ham_so = sympy.factor(ham_so, bien)
        mau = lay_mau_so(ham_so)
        if bien in mau.free_symbols:
            tu = lay_tu_so(ham_so)
            dang_mau = loai_ham_so(mau, bien)
            dang_tu = loai_ham_so(tu, bien)
            if dang_tu == hang_so.LoaiHamSo.HAM_BAC_HAI and dang_mau == hang_so.LoaiHamSo.HAM_BAC_NHAT:
                return hang_so.LoaiHamSo.HAM_HUU_TY
            elif dang_tu == hang_so.LoaiHamSo.HAM_BAC_NHAT and dang_mau == hang_so.LoaiHamSo.HAM_BAC_NHAT:
                return hang_so.LoaiHamSo.HAM_NHAT_BIEN
            else:
                return hang_so.LoaiHamSo.HAM_PHAN_THUC
        else:
            try:
                ham_so = sympy.Poly(ham_so, bien)
            except:
                return None
            he_so = ham_so.all_coeffs()
            if len(he_so) == 5:
                if he_so[1] == 0 and he_so[3] == 0:
                    return hang_so.LoaiHamSo.HAM_BAC_BON_TRUNG_PHUONG
                else:
                    return hang_so.LoaiHamSo.HAM_BAC_BON
            elif len(he_so) == 4:
                return hang_so.LoaiHamSo.HAM_BAC_BA
            elif len(he_so) == 3:
                return hang_so.LoaiHamSo.HAM_BAC_HAI
            elif len(he_so) == 2:
                return hang_so.LoaiHamSo.HAM_BAC_NHAT
            else:
                raise ValueError
    elif len(cac_bien) == 2:
        return 'can bien'
    else:
        raise ValueError


def gop_da_thuc(da_thuc, bien):
    return sympy.collect(da_thuc, bien)


def the_bieu_thuc(bieu_thuc, bien, gia_tri):
    bieu_thuc = bieu_thuc.subs(bien, gia_tri)
    return bieu_thuc


def the_bien(bieu_thuc, bien, gia_tri):
    try:
        with sympy.evaluate(False):
            bieu_thuc = bieu_thuc.subs(bien, gia_tri, simultaneous=True)
    except:
        bieu_thuc = bieu_thuc.subs(bien, gia_tri, simultaneous=True)
    return bieu_thuc


def phan_tich_thanh_nhan_tu(bieu_thuc):
    return sympy.factor(bieu_thuc)


def phan_tich_thanh_nhan_tu_giai(ham_so, **kwargs):
    loi_giai = huong_dan_giai.LoiGiai("Phân tích biểu thức {bt} thành nhân tử".format(
        bt=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_so))
    ))
    if str(phan_tich_thanh_nhan_tu(ham_so)) == str(ham_so):
        loi_giai.them_thao_tac("Không thể phân tích thêm")
        return loi_giai
    loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_so)))
    loi_giai.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(phan_tich_thanh_nhan_tu(ham_so))))
    return loi_giai


def lay_he_so(da_thuc, bien, so_mu):
    return da_thuc.coeff(bien, so_mu)


def nhan_vao(da_thuc):
    return sympy.expand(da_thuc)


def chuyen_thanh_da_thuc(bieu_thuc):
    return sympy.Poly(bieu_thuc)


def lay_cac_bien(bieu_thuc):
    """
    Lay tat ca cac bien tu  1 bieu thuc
    :param bieu_thuc: Sympy expression
    :return: list
    """
    return list(bieu_thuc.free_symbols)


def lay_tham_so(ham_so, bien):
    cac_bien = list(ham_so.free_symbols)
    cac_bien.remove(bien)
    return cac_bien[0]


def kiem_tra_bang_nha(bieu_thuc_1, bieu_thuc_2):
    """
    Kiem tra su bang nhau cua 2 bieu thuc
    :param bieu_thuc_1: Sympy expression
    :param bieu_thuc_2: Sympy expression
    :return: bool
    """
    if rut_gon(bieu_thuc_1 - bieu_thuc_2) == 0:
        return True
    else:
        return False


def tao_ham(ten_ham, ham_so, bien):
    """
    Tao mot ham so theo dang f(bien) = ham_so
    :param ten_ham: char
    :param ham_so: bieu_thuc
    :param bien: sympy.Symbol
    :return: sympy.Eq
    """
    return sympy.Eq(sympy.Function(ten_ham)(bien), ham_so)


def thay_bien(ham_so, bien, thay):
    if isinstance(bien, list):
        if len(bien) != len(thay):
            raise ValueError
        chuoi_b = ''
        for i in range(len(bien)):
            chuoi_b += xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien[i], thay[i]))) + ','
        chuoi_b = chuoi_b[:-1]
        loi_giai = huong_dan_giai.LoiGiai('Thế {b} vào {hs}'.format(
            b=chuoi_b,
            hs=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_so))
        ))
        loi_giai.them_thao_tac('Thế {b} vào {hs} ta được:'.format(
            b=chuoi_b,
            hs=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_so))
        ))
        ham_the = ham_so
        for i in range(len(bien)):
            ham_the = the_bien(ham_the, bien[i], thay[i])
        loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_the)))
        ham_the = tach_ra(ham_the)
        loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(ham_the)))
        loi_giai.dap_an = ham_the
        return loi_giai
    loi_giai = huong_dan_giai.LoiGiai('Thế {b} vào {hs}'.format(
        b=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien, thay))),
        hs=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_so))
    ))
    loi_giai.them_thao_tac('Thế {b} vào {hs} ta được:'.format(
        b=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien, thay))),
        hs=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_so))
    ))
    ham_the = the_bien(ham_so, bien, thay)
    try:
        loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_the)))
    except:
        pass
    ham_the = tach_ra(ham_the)
    loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(ham_the)))
    loi_giai.dap_an = ham_the
    return loi_giai


def tao_ten_ham(ten_ham, bien):
    return sympy.Function(ten_ham)(bien)


def giai_phuong_trinh(ham_so, bien):
    """
    Giai phuong trinh va tra ve loi giai
    :param ham_so: bieu_thuc
    :param bien: sympy.Symbols
    :return: LoiGiai
    """
    if isinstance(ham_so, sympy.Eq):
        pt = ham_so
        loi_giai = huong_dan_giai.LoiGiai(
            "Giải phương trình {phuong_trinh}".format(phuong_trinh=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(pt))))
        loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(pt)))
        pt = bat_dang_thuc.bang(pt.lhs - pt.rhs, 0)
        loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(pt)))
    else:
        pt = sympy.Eq(ham_so, 0)
        loi_giai = huong_dan_giai.LoiGiai(
            "Giải phương trình {phuong_trinh}".format(phuong_trinh=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(pt))))
        loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(pt)))
    # In ra pt

    # Rut gon
    pt_rut_gon = rut_gon(pt)
    if pt_rut_gon != pt:
        loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(
            ky_hieu_latex.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(pt_rut_gon)))

    # Phan tich thanh nhan tu
    pt_da_thuc = phan_tich_thanh_nhan_tu(pt_rut_gon)
    if pt_da_thuc != pt_rut_gon:
        loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(
            ky_hieu_latex.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(pt_da_thuc)))

    # Tim nghiem
    nghiem_thuc = tim_nghiem_thuc(ham_so, bien)

    if len(nghiem_thuc) == 0:
        loi_giai.them_thao_tac(
            "{tuong_duong} Phương trình vô nghiệm".format(tuong_duong=xu_ly_chuoi.boc_mathjax(
                ky_hieu_latex.DAU_TUONG_DUONG)))
    else:
        loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(
            "{tuong_duong} {bien_cac_nghiem}".format(tuong_duong=ky_hieu_latex.DAU_TUONG_DUONG,
                                                     bien_cac_nghiem="{bien}={cac_nghiem}".format(
                                                         bien=xu_ly_chuoi.tao_latex(bien),
                                                         cac_nghiem=xu_ly_chuoi.tao_ngoac_nhon(nghiem_thuc)))))

    # Luu dap an
    loi_giai.dap_an = nghiem_thuc

    return loi_giai


def lay_tu_so(bieu_thuc):
    """
    Tra ve tu so cua 1 bieu thuc
    :param bieu_thuc: bieu thuc
    :return: bieu thuc
    """
    return sympy.numer(bieu_thuc)


def lay_so_bien(bieu_thuc):
    """
    Tra ve so bien trong mot bieu thuc
    :param bieu_thuc: bieu_thuc
    :return: int
    """
    return len(list(bieu_thuc.free_symbols))


def tach_ra(bieu_thuc):
    return sympy.expand(bieu_thuc)


# Thu nghiem
if __name__ == '__main__':
    x = sympy.Symbol('x')
    t = sympy.Eq(sympy.log(4 * x, 2) - sympy.log(2, x / 2), 3)
    giai_phuong_trinh(t, x).xuat_html('loi_giai.html')
