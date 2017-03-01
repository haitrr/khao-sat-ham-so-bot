import sympy
import phuong_trinh
import xu_ly_chuoi
import hang_so
import bat_dang_thuc


def giai_phuong_trinh_bac_2(ham_so, bien,ket_qua = False):
    loi_giai = list()
    loi_giai.append(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(ham_so, 0))))
    ham_so_rut_gon = phuong_trinh.phan_tich_thanh_nhan_tu(ham_so)
    if ham_so_rut_gon != ham_so:
        loi_giai.append(xu_ly_chuoi.boc_mathjax(
            hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(ham_so_rut_gon, 0))))
        nghiem = phuong_trinh.tim_nghiem_thuc(ham_so_rut_gon, bien)
        if len(nghiem) == 0:
            loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + "Phương trình vô nghiệm"))
        loi_giai.append(xu_ly_chuoi.boc_mathjax(
            hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(bien) + "=" + xu_ly_chuoi.tao_ngoac_nhon(
                nghiem)))
    else:
        a, b, c = sympy.symbols('a b c')
        delta = sympy.Symbol('\Delta')
        pt = bat_dang_thuc.bang(delta, b ** 2 - 4 * a * c)
        loi_giai.append(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(pt)))
        pt = phuong_trinh.the_bien(pt, a, phuong_trinh.lay_he_so(ham_so_rut_gon, bien, 2))
        pt = phuong_trinh.the_bien(pt, b, phuong_trinh.lay_he_so(ham_so_rut_gon, bien, 1))
        pt = phuong_trinh.the_bien(pt, c, phuong_trinh.lay_he_so(ham_so_rut_gon, bien, 0))
        loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(pt)))
        pt = phuong_trinh.rut_gon(pt)
        loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(pt)))
        delta_gia_tri = pt.rhs
        if delta_gia_tri > 0:
            loi_giai.append(
                "Vì " + xu_ly_chuoi.boc_mathjax("\Delta > 0") + " nên phương trình có hai nghiệm phân biệt.")
            x_1 = (-b + sympy.sqrt(delta)) / (2 * a)
            nghiem_1 = xu_ly_chuoi.boc_mathjax(
                xu_ly_chuoi.tao_latex(bien) + "_1=" + xu_ly_chuoi.tao_latex(x_1))
            x_1 = phuong_trinh.the_bien(x_1, a, phuong_trinh.lay_he_so(ham_so_rut_gon, bien, 2))
            x_1 = phuong_trinh.the_bien(x_1, b, phuong_trinh.lay_he_so(ham_so_rut_gon, bien, 1))
            x_1 = phuong_trinh.the_bien(x_1, c, phuong_trinh.lay_he_so(ham_so_rut_gon, bien, 0))
            x_1 = phuong_trinh.the_bien(x_1, delta, delta_gia_tri)
            nghiem_1 += xu_ly_chuoi.boc_mathjax("=" + xu_ly_chuoi.tao_latex(x_1))
            x_1 = phuong_trinh.rut_gon(x_1)
            nghiem_1 += xu_ly_chuoi.boc_mathjax("=" + xu_ly_chuoi.tao_latex(x_1))
            loi_giai.append(nghiem_1)
            x_2 = (-b - sympy.sqrt(delta)) / (2 * a)
            nghiem_2 = xu_ly_chuoi.boc_mathjax(
                xu_ly_chuoi.tao_latex(bien) + "_1=" + xu_ly_chuoi.tao_latex(x_2))
            x_2 = phuong_trinh.the_bien(x_2, a, phuong_trinh.lay_he_so(ham_so_rut_gon, bien, 2))
            x_2 = phuong_trinh.the_bien(x_2, b, phuong_trinh.lay_he_so(ham_so_rut_gon, bien, 1))
            x_2 = phuong_trinh.the_bien(x_2, c, phuong_trinh.lay_he_so(ham_so_rut_gon, bien, 0))
            x_2 = phuong_trinh.the_bien(x_2, delta, delta_gia_tri)
            nghiem_2 += xu_ly_chuoi.boc_mathjax("=" + xu_ly_chuoi.tao_latex(x_2))
            x_2 = phuong_trinh.rut_gon(x_2)
            nghiem_2 += xu_ly_chuoi.boc_mathjax("=" + xu_ly_chuoi.tao_latex(x_2))
            loi_giai.append(nghiem_2)

        elif delta_gia_tri == 0:
            loi_giai.append("Vì " + xu_ly_chuoi.boc_mathjax("\Delta = 0") + " nên phương trình có nghiệm kép.")
            loi_giai.append(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(bien) + "=-b/2a"))
            nghiem = -b / (2 * a)
            loi_giai.append(xu_ly_chuoi.boc_mathjax(
                xu_ly_chuoi.tao_latex(bien) + "=" + xu_ly_chuoi.tao_latex(nghiem)))
        else:
            loi_giai.append("Vì " + xu_ly_chuoi.boc_mathjax("\Delta < 0") + " nên phương trình vô nghiệm")
    loi_giai.append(loi_giai)
    return loi_giai


def tim_tham_so_de_ham_so_lon_hon_hoac_bang_0(ham_so, bien):
    loi_giai = list()
    tham_so = None
    try:
        cac_bien = list(ham_so.free_symbols)
        cac_bien.remove(bien)
        tham_so = cac_bien[0]
    except:
        raise ValueError("Hàm số chưa được hỗ trợ")
    loi_giai.append("Để " + xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_so) + "\geq0,\\forall " + xu_ly_chuoi.tao_latex(bien) + " \in \mathbb{R} :"))
    a, b, c = sympy.symbols('a b c')
    delta = sympy.Symbol('\Delta')
    dieu_kien = [bat_dang_thuc.lon_hon(a, 0), bat_dang_thuc.nho_hon_hoac_bang(delta, 0)]
    loi_giai.append(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_ngoac_nhon(dieu_kien)))
    dieu_kien = [bat_dang_thuc.lon_hon(a, 0), bat_dang_thuc.nho_hon_hoac_bang(b ** 2 - 4 * a * c, 0)]
    loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_ngoac_nhon(dieu_kien)))
    dieu_kien[0] = phuong_trinh.the_bien(dieu_kien[0], a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    dieu_kien[1] = phuong_trinh.the_bien(dieu_kien[1], a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    dieu_kien[1] = phuong_trinh.the_bien(dieu_kien[1], b, phuong_trinh.lay_he_so(ham_so, bien, 1))
    dieu_kien[1] = phuong_trinh.the_bien(dieu_kien[1], c, phuong_trinh.lay_he_so(ham_so, bien, 0))
    loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_ngoac_nhon(dieu_kien)))
    dieu_kien[0] = bat_dang_thuc.lon_hon(phuong_trinh.rut_gon(bat_dang_thuc.lay_ve_trai(dieu_kien[0])), 0)
    dieu_kien[1] = bat_dang_thuc.nho_hon_hoac_bang(
        phuong_trinh.phan_tich_thanh_nhan_tu(bat_dang_thuc.lay_ve_trai(dieu_kien[1])), 0)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_ngoac_nhon(dieu_kien)))
    dieu_kien_temp = [bat_dang_thuc.giai_bat_dang_thuc(dieu_kien[0], tham_so),
                      bat_dang_thuc.giai_bat_dang_thuc(dieu_kien[1], tham_so)]
    loi_giai.append(
        xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_ngoac_nhon(dieu_kien_temp)))
    dieu_kien[0] = bat_dang_thuc.giai_bat_dang_thuc_set(dieu_kien[0], tham_so)
    dieu_kien[1] = bat_dang_thuc.giai_bat_dang_thuc_set(dieu_kien[1], tham_so)

    # loi_giai.append(xu_ly_chuoi.boc_latex_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_ngoac_nhon_latex(dieu_kien)))
    dieu_kien = bat_dang_thuc.tong_hop_ket_qua(dieu_kien)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(
        hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(tham_so) + "\in" + xu_ly_chuoi.tao_latex(
            dieu_kien)))
    return loi_giai

def tim_tham_so_de_ham_so_nho_hon_hoac_bang_0(ham_so, bien):
    loi_giai = list()
    tham_so = None
    try:
        cac_bien = list(ham_so.free_symbols)
        cac_bien.remove(bien)
        tham_so = cac_bien[0]
    except:
        raise ValueError("Hàm số chưa được hỗ trợ")
    loi_giai.append("Để " + xu_ly_chuoi.boc_mathjax(
        xu_ly_chuoi.tao_latex(ham_so) + "\leq0,\\forall " + xu_ly_chuoi.tao_latex(
            bien) + " \in \mathbb{R} :"))
    a, b, c = sympy.symbols('a b c')
    delta = sympy.Symbol('\Delta')
    dieu_kien = [bat_dang_thuc.nho_hon(a, 0), bat_dang_thuc.nho_hon_hoac_bang(delta, 0)]
    loi_giai.append(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_ngoac_nhon(dieu_kien)))
    dieu_kien = [bat_dang_thuc.nho_hon(a, 0), bat_dang_thuc.nho_hon_hoac_bang(b ** 2 - 4 * a * c, 0)]
    loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_ngoac_nhon(dieu_kien)))
    dieu_kien[0] = phuong_trinh.the_bien(dieu_kien[0], a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    dieu_kien[1] = phuong_trinh.the_bien(dieu_kien[1], a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    dieu_kien[1] = phuong_trinh.the_bien(dieu_kien[1], b, phuong_trinh.lay_he_so(ham_so, bien, 1))
    dieu_kien[1] = phuong_trinh.the_bien(dieu_kien[1], c, phuong_trinh.lay_he_so(ham_so, bien, 0))
    loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_ngoac_nhon(dieu_kien)))

    dieu_kien[0] = bat_dang_thuc.nho_hon(phuong_trinh.rut_gon(bat_dang_thuc.lay_ve_trai(dieu_kien[0])), 0)
    dieu_kien[1] = bat_dang_thuc.nho_hon_hoac_bang(
        phuong_trinh.phan_tich_thanh_nhan_tu(bat_dang_thuc.lay_ve_trai(dieu_kien[1])), 0)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_ngoac_nhon(dieu_kien)))

    dieu_kien_temp = [bat_dang_thuc.giai_bat_dang_thuc(dieu_kien[0], tham_so),
                      bat_dang_thuc.giai_bat_dang_thuc(dieu_kien[1], tham_so)]
    loi_giai.append(
        xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_ngoac_nhon(dieu_kien_temp)))
    dieu_kien[0] = bat_dang_thuc.giai_bat_dang_thuc_set(dieu_kien[0], tham_so)
    dieu_kien[1] = bat_dang_thuc.giai_bat_dang_thuc_set(dieu_kien[1], tham_so)

    # loi_giai.append(xu_ly_chuoi.boc_latex_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_ngoac_nhon_latex(dieu_kien)))
    dieu_kien = bat_dang_thuc.tong_hop_ket_qua(dieu_kien)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(
        hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(tham_so) + "\in" + xu_ly_chuoi.tao_latex(
            dieu_kien)))

    return loi_giai

def tim_tham_so_de_phuong_trinh_co_nghiem_kep_hoac_vo_nghiem(ham_so,bien):

    # Lay tham so
    cac_bien = list(ham_so.free_symbols)
    cac_bien.remove(bien)
    tham_so = cac_bien[0]

    # Giai
    loi_giai = list()

    # De phuong trinh co nghiem kep hoac vo nghiem
    loi_giai.append("Để " + xu_ly_chuoi.boc_mathjax(
        xu_ly_chuoi.tao_latex(ham_so) + "=0") + " có nghiệm kép hoặc vô nghiệm")
    # Delta <=0
    a, b, c = sympy.symbols('a b c')
    delta = sympy.Symbol('\Delta')
    dieu_kien = bat_dang_thuc.nho_hon_hoac_bang(delta,0)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)))

    # delta = b^2-4*a*c
    dieu_kien = bat_dang_thuc.nho_hon_hoac_bang(b**2-4*a*c,0)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(dieu_kien)))

    # The so vao delta
    dieu_kien = phuong_trinh.the_bien(dieu_kien, a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    dieu_kien = phuong_trinh.the_bien(dieu_kien, b, phuong_trinh.lay_he_so(ham_so, bien, 1))
    dieu_kien = phuong_trinh.the_bien(dieu_kien, c, phuong_trinh.lay_he_so(ham_so, bien, 0))
    loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(dieu_kien)))

    # Phan tich thanh nhan tu
    dieu_kien = bat_dang_thuc.nho_hon_hoac_bang(
        phuong_trinh.phan_tich_thanh_nhan_tu(bat_dang_thuc.lay_ve_trai(dieu_kien)), 0)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(dieu_kien)))

    # Giai dang thuong
    dieu_kien_temp = bat_dang_thuc.giai_bat_dang_thuc(dieu_kien, tham_so)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(dieu_kien)))

    # Giai dang set
    dieu_kien = bat_dang_thuc.giai_bat_dang_thuc_set(dieu_kien, tham_so)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(
        hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(tham_so) + "\in" + xu_ly_chuoi.tao_latex(
            dieu_kien)))
    return loi_giai

def tim_tham_so_de_phuong_trinh_hai_nghiem_phan_biet(ham_so,bien):
    """
    Tìm tham số để phương trình có hai nghiệm phân biệt
    Trả về lời giải và hai nghiệm
    :rtype: list,list
    """
    # Lay tham so
    cac_bien = list(ham_so.free_symbols)
    cac_bien.remove(bien)
    tham_so = cac_bien[0]

    # Giai
    loi_giai = list()

    # De phuong trinh co nghiem kep hoac vo nghiem
    loi_giai.append("Để " + xu_ly_chuoi.boc_mathjax(
        xu_ly_chuoi.tao_latex(ham_so) + "=0") + " có hai nghiệm phân biệt")

    # Delta >0
    a, b, c = sympy.symbols('a b c')
    delta = sympy.Symbol('\Delta')
    dieu_kien = bat_dang_thuc.lon_hon(delta,0)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)))

    # delta = b^2-4*a*c
    dieu_kien = bat_dang_thuc.lon_hon(b**2-4*a*c,0)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(dieu_kien)))

    # The so vao delta
    dieu_kien = phuong_trinh.the_bien(dieu_kien, a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    dieu_kien = phuong_trinh.the_bien(dieu_kien, b, phuong_trinh.lay_he_so(ham_so, bien, 1))
    dieu_kien = phuong_trinh.the_bien(dieu_kien, c, phuong_trinh.lay_he_so(ham_so, bien, 0))
    loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(dieu_kien)))

    # Phan tich thanh nhan tu
    dieu_kien = bat_dang_thuc.lon_hon(
        phuong_trinh.phan_tich_thanh_nhan_tu(bat_dang_thuc.lay_ve_trai(dieu_kien)), 0)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(dieu_kien)))

    gia_tri_delta = bat_dang_thuc.lay_ve_trai(dieu_kien)

    # Giai dang thuong
    dieu_kien_temp = bat_dang_thuc.giai_bat_dang_thuc(dieu_kien, tham_so)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(dieu_kien)))

    # Giai dang set
    dieu_kien = bat_dang_thuc.giai_bat_dang_thuc_set(dieu_kien, tham_so)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(
        hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(tham_so) + "\in" + xu_ly_chuoi.tao_latex(
            dieu_kien)))

    # Liet ke nghiem
    loi_giai.append("Khi đó phương trình có 2 nghiệm :")
    x_1,x_2 = sympy.symbols("x_1 x_2")

    # 2 nghiem
    nghiem = [bat_dang_thuc.bang(x_1,(-b + sympy.sqrt(delta)) / (2 * a)),bat_dang_thuc.bang(x_2,(-b - sympy.sqrt(delta)) / (2 * a))]
    loi_giai.append(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_ngoac_nhon(nghiem)))

    # Thay so vao nghiem
    nghiem[0] = phuong_trinh.the_bien(nghiem[0], delta,gia_tri_delta)
    nghiem[0] = phuong_trinh.the_bien(nghiem[0], a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    nghiem[0] = phuong_trinh.the_bien(nghiem[0], b, phuong_trinh.lay_he_so(ham_so, bien, 1))
    nghiem[0] = phuong_trinh.the_bien(nghiem[0], c, phuong_trinh.lay_he_so(ham_so, bien, 0))
    nghiem[1] = phuong_trinh.the_bien(nghiem[1], delta, gia_tri_delta)
    nghiem[1] = phuong_trinh.the_bien(nghiem[1], a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    nghiem[1] = phuong_trinh.the_bien(nghiem[1], b, phuong_trinh.lay_he_so(ham_so, bien, 1))
    nghiem[1] = phuong_trinh.the_bien(nghiem[1], c, phuong_trinh.lay_he_so(ham_so, bien, 0))
    loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_ngoac_nhon(nghiem)))

    # Rut gon nghiem
    nghiem[0] = bat_dang_thuc.bang(x_1,
        phuong_trinh.phan_tich_thanh_nhan_tu(bat_dang_thuc.lay_ve_phai(nghiem[0])))
    nghiem[1] = bat_dang_thuc.bang(x_2,
        phuong_trinh.phan_tich_thanh_nhan_tu(bat_dang_thuc.lay_ve_phai(nghiem[1])))
    loi_giai.append(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_ngoac_nhon(nghiem)))

    return loi_giai,nghiem

if __name__ == "__main__":
    import tao_loi_giai

    hs = sympy.sympify("3*m*x^2-2*(m-1)*x+1")
    b = sympy.Symbol('x')
    tao_loi_giai.xuat_html(tim_tham_so_de_phuong_trinh_hai_nghiem_phan_biet(
        hs, b), "loi_giai.html")
