import sympy
import huong_dan_giai
import ky_hieu_latex
import xu_ly_chuoi
import hang_so
import phuong_trinh


# Giai he bat dang thuc
def giai_he_bat_dang_thuc(he_bat_dang_thuc, bien):
    """
    Giai he bat dang thang ,
    nhan vao list cac bat dang thuc va bien
    tra ve nghiem cua bat dang thuc
    """
    mien_nghiem_he = sympy.S.Reals
    for bat_dang_thuc in he_bat_dang_thuc:
        bdt_rut_gon = bat_dang_thuc.doit()
        mien_nghiem_bdt = sympy.solveset(bdt_rut_gon, bien, sympy.S.Reals)
        mien_nghiem_he = mien_nghiem_he.intersect(mien_nghiem_bdt)
    return mien_nghiem_he


def tong_hop_ket_qua(cac_ket_qua):
    '''
    Tong hop ket qua thanh mot set,
    nhan vao list cac set,
    tra ve set tong hop
    '''
    ket_qua_tong_hop = sympy.S.Reals
    for ket_qua in cac_ket_qua:
        ket_qua_tong_hop = ket_qua_tong_hop.intersect(ket_qua)
    return ket_qua_tong_hop


def giai_bat_dang_thuc(bat_dang_thuc, bien):
    '''
    Giai bat dang thuc,
    nhan vao bat dang thuc va bien,
    tra ve set nghiem
    '''
    return sympy.solve(bat_dang_thuc, bien, sympy.S.Reals)


def giai_bat_dang_thuc_set(he_bat_dang_thuc, bien):
    '''
    Gia bat dang thuc set,
    phuong thuc du phong trong truong hop
    giai bat dang thuc khong hoat dong
    '''
    return sympy.solve_univariate_inequality(
        he_bat_dang_thuc, bien, relational=False)


def lon_hon_hoac_bang(ve_trai, ve_phai):
    '''
    tao bat dang thuc lon hon hoac bang,
    nhan vao ve trai ve phai,
    tra ve bat dang thuc
    '''
    return sympy.GreaterThan(ve_trai, ve_phai)


def lon_hon(ve_trai, ve_phai):
    '''
    tao bat dang thuc lon hon,
    nhan vao ve trai ve phai,
    tra ve bat dang thuc
    '''
    return sympy.StrictGreaterThan(ve_trai, ve_phai)


def nho_hon_hoac_bang(ve_trai, ve_phai):
    '''
    tao bat dang thuc nho hon hoac bang,
    nhan vao ve trai ve phai,
    tra ve bat dang thuc
    '''
    return sympy.LessThan(ve_trai, ve_phai)


def nho_hon(ve_trai, ve_phai):
    '''
    tao bat dang thuc nho hon,
    nhan vao ve trai ve phai,
    tra ve bat dang thuc
    '''
    return sympy.StrictLessThan(ve_trai, ve_phai)


def lay_ve_trai(bat_dang_thuc):
    '''
    Lay ve trai cua bat dang thuc
    '''
    return bat_dang_thuc.lhs


# Lay ve phai cua phuong trinh hoac bat dang thuc
def lay_ve_phai(bat_dang_thuc):
    '''
    lay ve phai cua bat dang thuc
    '''
    return bat_dang_thuc.rhs


def bang(ve_trai, ve_phai):
    '''
    tai phuong trinh tu ve trai ve phai
    '''
    return sympy.Eq(ve_trai, ve_phai)


def giai_bat_dang_thuc_lg(bat_dang_thuc, bien):
    '''
    Tao loi giai cho bai toan giai dang thuc
    '''
    loi_giai = huong_dan_giai.LoiGiai(
        'Giải bất đẳng thức {bdt} tìm {bien}'.format(
            bdt=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(bat_dang_thuc)),
            bien=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(bien))))
    loi_giai.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(bat_dang_thuc)))

    # rut gon bdt
    bat_dang_thuc_rut_gon = phuong_trinh.rut_gon(bat_dang_thuc)
    if bat_dang_thuc_rut_gon != bat_dang_thuc:
        loi_giai.them_thao_tac(
            xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                    xu_ly_chuoi.tao_latex(
                                        bat_dang_thuc_rut_gon)))

    # phan tich thanh nhan tu
    bat_dang_thuc_nhan_tu = phuong_trinh.phan_tich_thanh_nhan_tu(
        bat_dang_thuc_rut_gon)
    if bat_dang_thuc_nhan_tu != bat_dang_thuc_rut_gon:
        loi_giai.them_thao_tac(
            xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                    xu_ly_chuoi.tao_latex(
                                        bat_dang_thuc_nhan_tu)))

    # giai thuong
    nghiem_thuong = sympy.solve(bat_dang_thuc_nhan_tu, bien, sympy.S.Reals)
    loi_giai.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                xu_ly_chuoi.tao_latex(nghiem_thuong)))

    # giai set
    nghiem_set = sympy.solveset(bat_dang_thuc_nhan_tu, bien, sympy.S.Reals)
    loi_giai.them_thao_tac("Vậy ta được {nghiem}".format(
        nghiem=xu_ly_chuoi.boc_mathjax("{bien} \\in {set}").format(
            bien=xu_ly_chuoi.tao_latex(bien),
            set=xu_ly_chuoi.tao_latex(nghiem_set))))

    loi_giai.dap_an = nghiem_set

    return loi_giai


if __name__ == "__main__":
    hs = sympy.sympify("(x-1)/(x^2+2)")
    x = sympy.Symbol('x')
    giai_bat_dang_thuc_lg(lon_hon(hs, 0), x).xuat_html('loi_giai.html')
