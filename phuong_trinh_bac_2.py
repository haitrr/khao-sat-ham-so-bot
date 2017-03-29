import sympy
import phuong_trinh
import xu_ly_chuoi
import hang_so
import bat_dang_thuc
import huong_dan_giai


def giai_phuong_trinh_bac_2(ham_so, bien):
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


def tim_tham_so_de_ham_so_lon_hon_hoac_bang_0(ham_so, bien, tham_so):
    # De bai
    loi_giai = huong_dan_giai.LoiGiai(
        "Tìm tham số để {0} {1}".format(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(bat_dang_thuc.lon_hon_hoac_bang(ham_so, 0))),
                                        xu_ly_chuoi.boc_mathjax("\\forall \in \mathbb{R}")))

    # Cac symbol
    a, b, c = sympy.symbols('a b c')
    delta = sympy.Symbol('\Delta')

    # Buoc 1: Tinh delta
    buoc_1 = huong_dan_giai.LoiGiai("Tính {0}".format(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(delta))))

    # Cong thuc tinh delta
    cong_thuc_delta = bat_dang_thuc.bang(delta, b ** 2 - 4 * a * c)

    # In ra cong thuc
    buoc_1.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(cong_thuc_delta)))

    # The cac he so vao cong thuc
    cong_thuc_delta = phuong_trinh.the_bien(cong_thuc_delta, a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    cong_thuc_delta = phuong_trinh.the_bien(cong_thuc_delta, b, phuong_trinh.lay_he_so(ham_so, bien, 1))
    cong_thuc_delta = phuong_trinh.the_bien(cong_thuc_delta, c, phuong_trinh.lay_he_so(ham_so, bien, 0))

    # In ra cong thuc sau khi the so
    buoc_1.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(cong_thuc_delta)))

    # Rut gon ve phai
    cong_thuc_delta = bat_dang_thuc.bang(delta, phuong_trinh.phan_tich_thanh_nhan_tu(cong_thuc_delta.rhs))

    # In ra cong thuc sau khi rut gon
    buoc_1.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(cong_thuc_delta)))

    # Luu ket qua
    buoc_1.dap_an = cong_thuc_delta.rhs

    # Them buoc vao loi giai
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2 giai he
    he = [bat_dang_thuc.lon_hon(a, 0), bat_dang_thuc.nho_hon_hoac_bang(delta, 0)]
    buoc_2 = huong_dan_giai.LoiGiai("Giải hệ bất đẳng thức {0} để tìm {1}".format(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_ngoac_nhon(he)),
                                                                       xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so))))
    # In ra cong thuc
    buoc_2.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_ngoac_nhon(he)))

    # The so vao cong thuc
    he[0] = phuong_trinh.the_bien(he[0], a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    he[1] = phuong_trinh.the_bien(he[1], delta, buoc_1.dap_an)

    # In ra he sau khi thay so
    buoc_2.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_ngoac_nhon(he)))

    # Giai he
    nghiem = bat_dang_thuc.giai_he_bat_dang_thuc(he, tham_so)

    # In ra ket qua
    buoc_2.them_thao_tac("Giải hệ bất đẳng thức ta được {0}".format(
        xu_ly_chuoi.boc_mathjax("{0} \in {1}".format(xu_ly_chuoi.tao_latex(tham_so), xu_ly_chuoi.tao_latex(nghiem)))))
    buoc_2.dap_an = nghiem

    # Them buoc va dap an
    loi_giai.them_thao_tac(buoc_2)
    loi_giai.dap_an = nghiem

    # Tra ve loi giai
    return loi_giai


def tim_tham_so_de_ham_so_nho_hon_hoac_bang_0(ham_so, bien, tham_so):
    # De bai
    loi_giai = huong_dan_giai.LoiGiai(
        "Tìm tham số để {0} {1}".format(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(bat_dang_thuc.nho_hon_hoac_bang(ham_so, 0))),
                                        xu_ly_chuoi.boc_mathjax("\\forall \in \mathbb{R}")))

    # Cac symbol
    a, b, c = sympy.symbols('a b c')
    delta = sympy.Symbol('\Delta')

    # Buoc 1: Tinh delta
    buoc_1 = huong_dan_giai.LoiGiai("Tính {0}".format(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(delta))))

    # Cong thuc tinh delta
    cong_thuc_delta = bat_dang_thuc.bang(delta, b ** 2 - 4 * a * c)

    # In ra cong thuc
    buoc_1.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(cong_thuc_delta)))

    # The cac he so vao cong thuc
    cong_thuc_delta = phuong_trinh.the_bien(cong_thuc_delta, a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    cong_thuc_delta = phuong_trinh.the_bien(cong_thuc_delta, b, phuong_trinh.lay_he_so(ham_so, bien, 1))
    cong_thuc_delta = phuong_trinh.the_bien(cong_thuc_delta, c, phuong_trinh.lay_he_so(ham_so, bien, 0))

    # In ra cong thuc sau khi the so
    buoc_1.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(cong_thuc_delta)))

    # Rut gon ve phai
    cong_thuc_delta = bat_dang_thuc.bang(delta, phuong_trinh.phan_tich_thanh_nhan_tu(cong_thuc_delta.rhs))

    # In ra cong thuc sau khi rut gon
    buoc_1.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(cong_thuc_delta)))

    # Luu ket qua
    buoc_1.dap_an = cong_thuc_delta.rhs

    # Them buoc vao loi giai
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2 giai he
    he = [bat_dang_thuc.nho_hon(a, 0), bat_dang_thuc.nho_hon_hoac_bang(delta, 0)]
    buoc_2 = huong_dan_giai.LoiGiai("Giải hệ bất đẳng thức {0} để tìm {1}".format(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_ngoac_nhon(he)),
                                                                       xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so))))
    # In ra cong thuc
    buoc_2.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_ngoac_nhon(he)))

    # The so vao cong thuc
    he[0] = phuong_trinh.the_bien(he[0], a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    he[1] = phuong_trinh.the_bien(he[1], delta, buoc_1.dap_an)

    # In ra he sau khi thay so
    buoc_2.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_ngoac_nhon(he)))

    # Giai he
    nghiem = bat_dang_thuc.giai_he_bat_dang_thuc(he, tham_so)

    # In ra ket qua
    buoc_2.them_thao_tac("Giải hệ bất đẳng thức ta được {0}".format(
        xu_ly_chuoi.boc_mathjax("{0} \in {1}".format(xu_ly_chuoi.tao_latex(tham_so), xu_ly_chuoi.tao_latex(nghiem)))))
    buoc_2.dap_an = nghiem

    # Them buoc va dap an
    loi_giai.them_thao_tac(buoc_2)
    loi_giai.dap_an = nghiem

    # Tra ve loi giai
    return loi_giai


def tim_tham_so_de_phuong_trinh_co_nghiem_kep_hoac_vo_nghiem(ham_so, bien, tham_so):
    # Giai
    loi_giai = huong_dan_giai.LoiGiai(
        "Tìm tham số để {0} có nghiệm kép hoặc vô nghiệm".format(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(ham_so, 0)))))

    # Cac symbol
    a, b, c = sympy.symbols('a b c')
    delta = sympy.Symbol('\Delta')

    # Buoc 1: Tinh delta
    buoc_1 = huong_dan_giai.LoiGiai("Tính {0}".format(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(delta))))

    # Cong thuc tinh delta
    cong_thuc_delta = bat_dang_thuc.bang(delta, b ** 2 - 4 * a * c)

    # In ra cong thuc
    buoc_1.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(cong_thuc_delta)))

    # The cac he so vao cong thuc
    cong_thuc_delta = phuong_trinh.the_bien(cong_thuc_delta, a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    cong_thuc_delta = phuong_trinh.the_bien(cong_thuc_delta, b, phuong_trinh.lay_he_so(ham_so, bien, 1))
    cong_thuc_delta = phuong_trinh.the_bien(cong_thuc_delta, c, phuong_trinh.lay_he_so(ham_so, bien, 0))

    # In ra cong thuc sau khi the so
    buoc_1.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(cong_thuc_delta)))

    # Rut gon ve phai
    cong_thuc_delta = bat_dang_thuc.bang(delta, phuong_trinh.phan_tich_thanh_nhan_tu(cong_thuc_delta.rhs))

    # In ra cong thuc sau khi rut gon
    buoc_1.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(cong_thuc_delta)))

    # Luu ket qua
    buoc_1.dap_an = cong_thuc_delta.rhs

    # Them buoc vao loi giai
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2 : delta<=0

    dieu_kien = bat_dang_thuc.nho_hon_hoac_bang(delta,0)
    buoc_2 = huong_dan_giai.LoiGiai("Giải bất đẳng thức {0} để tìm {1}".format(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)),
                                                                       xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so))))

    # In ra dieu kien
    buoc_2.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)))

    # The so vao dieu kien
    dieu_kien = phuong_trinh.the_bien(dieu_kien, delta, buoc_1.dap_an)

    # In ra dieu kien sau khi thay so
    buoc_2.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(dieu_kien)))

    # Giai dieu kien
    nghiem = bat_dang_thuc.giai_bat_dang_thuc_set(dieu_kien, tham_so)


    # In ra ket qua
    buoc_2.them_thao_tac("Giải hệ bất đẳng thức ta được {0}".format(
        xu_ly_chuoi.boc_mathjax("{0} \in {1}".format(xu_ly_chuoi.tao_latex(tham_so), xu_ly_chuoi.tao_latex(nghiem)))))
    buoc_2.dap_an = nghiem

    # Them buoc va dap an
    loi_giai.them_thao_tac(buoc_2)
    loi_giai.dap_an = nghiem

    # Tra ve loi giai
    return loi_giai


def tim_tham_so_de_phuong_trinh_hai_nghiem_phan_biet(ham_so, bien,tham_so):
    """
    Tìm tham số để phương trình có hai nghiệm phân biệt
    Trả về lời giải và hai nghiệm
    :rtype: huong_dan_giai.LoiGiai
    """
    # Giai
    loi_giai = huong_dan_giai.LoiGiai(
        "Tìm tham số để {0} có hai nghiệm phân biệt".format(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(ham_so, 0)))))

    # Cac symbol
    a, b, c = sympy.symbols('a b c')
    delta = sympy.Symbol('\Delta')

    # Buoc 1: Tinh delta
    buoc_1 = huong_dan_giai.LoiGiai("Tính {0}".format(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(delta))))

    # Cong thuc tinh delta
    cong_thuc_delta = bat_dang_thuc.bang(delta, b ** 2 - 4 * a * c)

    # In ra cong thuc
    buoc_1.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(cong_thuc_delta)))

    # The cac he so vao cong thuc
    cong_thuc_delta = phuong_trinh.the_bien(cong_thuc_delta, a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    cong_thuc_delta = phuong_trinh.the_bien(cong_thuc_delta, b, phuong_trinh.lay_he_so(ham_so, bien, 1))
    cong_thuc_delta = phuong_trinh.the_bien(cong_thuc_delta, c, phuong_trinh.lay_he_so(ham_so, bien, 0))

    # In ra cong thuc sau khi the so
    buoc_1.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(cong_thuc_delta)))

    # Rut gon ve phai
    cong_thuc_delta = bat_dang_thuc.bang(delta, phuong_trinh.phan_tich_thanh_nhan_tu(cong_thuc_delta.rhs))

    # In ra cong thuc sau khi rut gon
    buoc_1.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(cong_thuc_delta)))

    # Luu ket qua
    buoc_1.dap_an = cong_thuc_delta.rhs

    # Them buoc vao loi giai
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2 : delta<=0

    dieu_kien = bat_dang_thuc.lon_hon(delta, 0)
    buoc_2 = huong_dan_giai.LoiGiai("Giải bất đẳng thức {0} để tìm {1}".format(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)),
                                                                     xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so))))

    # In ra dieu kien
    buoc_2.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)))

    # The so vao dieu kien
    dieu_kien = phuong_trinh.the_bien(dieu_kien, delta, buoc_1.dap_an)

    # In ra dieu kien sau khi thay so
    buoc_2.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(dieu_kien)))

    # Giai dieu kien
    nghiem = bat_dang_thuc.giai_bat_dang_thuc_set(dieu_kien, tham_so)

    # In ra ket qua
    buoc_2.them_thao_tac("Giải hệ bất đẳng thức ta được {0}".format(
        xu_ly_chuoi.boc_mathjax("{0} \in {1}".format(xu_ly_chuoi.tao_latex(tham_so), xu_ly_chuoi.tao_latex(nghiem)))))

    # Luu dap an
    buoc_2.dap_an = nghiem

    # Them buoc va dap an
    loi_giai.them_thao_tac(buoc_2)

    # Buoc 3 xac dinh hai nghiem cua pt
    buoc_3 = huong_dan_giai.LoiGiai('Xác định hai nghiệm của phương trình')

    # Cong thuc nghiem
    nghiem_1,nghiem_2 = sympy.symbols(str(bien)+'_1 '+str(bien)+'_2')
    nghiem = list()
    nghiem.append(bat_dang_thuc.bang(nghiem_1,(-b+sympy.sqrt(delta))/(2*a)))
    nghiem.append(bat_dang_thuc.bang(nghiem_2, (-b - sympy.sqrt(delta)) / (2 * a)))

    # In ra cong thuc nghiem
    buoc_3.them_thao_tac('Hai nghiệm của phương trình là:')
    buoc_3.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_ngoac_nhon(nghiem)))

    # Thay so va cong thuc nghiem
    nghiem[0] = phuong_trinh.the_bien(nghiem[0], a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    nghiem[0] = phuong_trinh.the_bien(nghiem[0], b, phuong_trinh.lay_he_so(ham_so, bien, 1))
    nghiem[0] = phuong_trinh.the_bien(nghiem[0], delta, buoc_1.dap_an)
    nghiem[1] = phuong_trinh.the_bien(nghiem[1], a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    nghiem[1] = phuong_trinh.the_bien(nghiem[1], b, phuong_trinh.lay_he_so(ham_so, bien, 1))
    nghiem[1] = phuong_trinh.the_bien(nghiem[1], delta, buoc_1.dap_an)

    # In ra cong thuc sau khi thay so
    buoc_3.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG+xu_ly_chuoi.tao_ngoac_nhon(nghiem)))

    # Rut gon nghiem neu duoc
    nghiem[0]=bat_dang_thuc.bang(nghiem_1,phuong_trinh.phan_tich_thanh_nhan_tu(nghiem[0].rhs))
    nghiem[1]=bat_dang_thuc.bang(nghiem_2,phuong_trinh.phan_tich_thanh_nhan_tu(nghiem[1].rhs))

    # In ra cong thuc sau khi thay so
    buoc_3.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG+xu_ly_chuoi.tao_ngoac_nhon(nghiem)))

    # Luu dap an
    buoc_3.dap_an=[nghiem[0].rhs,nghiem[1].rhs]

    # Them buoc 3 vao loi giai
    loi_giai.them_thao_tac(buoc_3)

    # Luu dap an cua loi giai
    loi_giai.dap_an = buoc_2.dap_an

    # Tra ve loi giai
    return loi_giai

def tinh_delta(ham_so,bien):
    # Cac symbol
    a, b, c = sympy.symbols('a b c')
    delta = sympy.Symbol('\Delta')

    # Buoc 1: Tinh delta
    loi_giai = huong_dan_giai.LoiGiai("Tính {0}".format(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(delta))))

    # Cong thuc tinh delta
    cong_thuc_delta = bat_dang_thuc.bang(delta, b ** 2 - 4 * a * c)

    # In ra cong thuc
    loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(cong_thuc_delta)))

    # The cac he so vao cong thuc
    cong_thuc_delta = phuong_trinh.the_bien(cong_thuc_delta, a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    cong_thuc_delta = phuong_trinh.the_bien(cong_thuc_delta, b, phuong_trinh.lay_he_so(ham_so, bien, 1))
    cong_thuc_delta = phuong_trinh.the_bien(cong_thuc_delta, c, phuong_trinh.lay_he_so(ham_so, bien, 0))

    # In ra cong thuc sau khi the so
    loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(cong_thuc_delta)))

    # Rut gon ve phai
    cong_thuc_delta = bat_dang_thuc.bang(delta, phuong_trinh.phan_tich_thanh_nhan_tu(cong_thuc_delta.rhs))

    # In ra cong thuc sau khi rut gon
    loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(cong_thuc_delta)))

    # Luu ket qua
    loi_giai.dap_an = cong_thuc_delta.rhs

    return loi_giai


def quan_he_2_nghiem_viet(ham_so, bien):
    pt = bat_dang_thuc.bang(ham_so, 0)
    loi_giai=huong_dan_giai.LoiGiai("Áp dụng định lý Viet tìm quan hệ giữa hai nghiệm của phương trình {pt}".format(pt = xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(pt))))
    a, b, c = sympy.symbols('a b c')
    nghiem_1, nghiem_2 = sympy.symbols(str(bien) + '_1 ' + str(bien) + '_2')
    # Cong thuc
    quan_he=[bat_dang_thuc.bang(nghiem_1+nghiem_2,-b/a),bat_dang_thuc.bang(nghiem_1*nghiem_2,c/a)]
    loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_ngoac_nhon(quan_he)))

    # The so
    quan_he[0] = phuong_trinh.the_bien(quan_he[0], a, phuong_trinh.lay_he_so(ham_so, bien, 2))
    quan_he[0] = phuong_trinh.the_bien(quan_he[0], b, phuong_trinh.lay_he_so(ham_so, bien, 1))
    quan_he[1] = phuong_trinh.the_bien(quan_he[1], c, phuong_trinh.lay_he_so(ham_so, bien, 0))
    quan_he[1] = phuong_trinh.the_bien(quan_he[1], a, phuong_trinh.lay_he_so(ham_so, bien, 2))

    loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG+xu_ly_chuoi.tao_ngoac_nhon(quan_he)))
    # Rut gon
    quan_he_rut_gon = [phuong_trinh.phan_tich_thanh_nhan_tu(quan_he[0]),phuong_trinh.phan_tich_thanh_nhan_tu(quan_he[1])]
    if phuong_trinh.so_sanh(quan_he_rut_gon[0].rhs,quan_he[0].rhs) is False or phuong_trinh.so_sanh(quan_he_rut_gon[1].rhs,quan_he[1].rhs) is False:
        loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_ngoac_nhon(quan_he_rut_gon)))

    loi_giai.dap_an=[quan_he_rut_gon[0].rhs,quan_he_rut_gon[1].rhs]
    return loi_giai


if __name__ == "__main__":

    hs = sympy.sympify("3*m*x^2-2*(m-1)*x+1")
    b = sympy.Symbol('x')
    ts = sympy.Symbol('m')
    quan_he_2_nghiem_viet(
        hs, b).xuat_html("loi_giai.html")
