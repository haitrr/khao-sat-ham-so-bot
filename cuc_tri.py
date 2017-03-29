import dao_ham
import phuong_trinh
import tinh_xac_dinh
import huong_dan_giai
import xu_ly_chuoi
import phuong_trinh_bac_2
import bat_dang_thuc
import hang_so
import tap_hop


def tim_diem_cuc_tieu(ham_so, bien):
    dao_ham_cap_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien).dap_an
    dao_ham_cap_2 = dao_ham.tinh_dao_ham_cap_1(dao_ham_cap_1, bien).dap_an
    nghiem_dao_ham_cap_1 = phuong_trinh.tim_nghiem_thuc(dao_ham_cap_1, bien)
    txd = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien).dap_an
    nghiem_cuc_tieu = []
    for nghiem in nghiem_dao_ham_cap_1:
        if txd.contains(nghiem) is False:
            continue
        else:
            if dao_ham_cap_2.subs(bien, nghiem) > 0:
                nghiem_cuc_tieu.append(nghiem)
    dct = []
    for nghiem in nghiem_cuc_tieu:
        dct.append((nghiem, ham_so.subs(bien, nghiem)))
    return dct


def tim_diem_cuc_dai(ham_so, bien):
    dao_ham_cap_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien).dap_an
    dao_ham_cap_2 = dao_ham.tinh_dao_ham_cap_1(dao_ham_cap_1, bien).dap_an
    nghiem_dao_ham_cap_1 = phuong_trinh.tim_nghiem_thuc(dao_ham_cap_1, bien)
    txd = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien).dap_an
    nghiem_cuc_dai = []
    for nghiem in nghiem_dao_ham_cap_1:
        if txd.contains(nghiem) is False:
            continue
        else:
            if dao_ham_cap_2.subs(bien, nghiem) < 0:
                nghiem_cuc_dai.append(nghiem)
    dcd = []
    for nghiem in nghiem_cuc_dai:
        dcd.append((nghiem, ham_so.subs(bien, nghiem)))
    return dcd


def tim_tham_so_de_ham_so_co_cuc_tri(ham_so, bien, tham_so):
    ham_f = phuong_trinh.tao_ham('f', ham_so, bien)
    loi_giai = huong_dan_giai.LoiGiai(
        "Tìm {0} để {1} có cực trị".format(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
                                           xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_f))))

    # Buoc 1 tim tap xac dinh
    buoc_1 = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien)
    buoc_1.ten_loi_giai = "Tìm tập xác định của hàm số"
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2 Tinh dao ham cua ham so
    buoc_2 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_2.ten_loi_giai = "Tìm đạo hàm của hàm số"

    loi_giai.them_thao_tac(buoc_2)

    if phuong_trinh.loai_ham_so(ham_so, bien) == 'ham_phan_thuc':
        can_xet = phuong_trinh.lay_tu_so(ham_so)
    else:
        can_xet = buoc_2.dap_an

    # Buoc 3 Tim tham so de f' co 2 nghiem phan biet
    buoc_3 = phuong_trinh_bac_2.tim_tham_so_de_phuong_trinh_hai_nghiem_phan_biet(can_xet, bien, tham_so)
    buoc_3.ten_loi_giai = "Tìm {0} để đạo hàm có hai nghiệm phân biệt".format(
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)))
    loi_giai.them_thao_tac(buoc_3)

    # Buoc 4 tong hop
    buoc_4 = huong_dan_giai.LoiGiai("Tổng hợp kết quả")
    buoc_4.them_thao_tac("Tổng hợp kết quả với tập xác định:")
    tong_ket = tap_hop.tim_giao(buoc_1.dap_an, buoc_3.dap_an)
    buoc_4.them_thao_tac(xu_ly_chuoi.boc_mathjax(
        "{ts} \in {tk}".format(ts=xu_ly_chuoi.tao_latex(tham_so), tk=xu_ly_chuoi.tao_latex(tong_ket))))

    buoc_4.dap_an = tong_ket
    loi_giai.them_thao_tac(buoc_4)
    loi_giai.dap_an = tong_ket
    return loi_giai


def tim_phuong_trinh_duong_thang_di_qua_hai_diem_cuc_tri(ham_so, bien):
    ham_so_f = phuong_trinh.tao_ham('f', ham_so, bien)
    loi_giai = huong_dan_giai.LoiGiai("Viết phương trình đường thẳng đi qua hai điểm cực trị của hàm số {ham_f}".format(
        ham_f=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_so_f))))
    loai_ham = phuong_trinh.loai_ham_so(ham_so, bien)
    if loai_ham == 'ham_bac_ba':
        pass


def tim_tham_so_de_cuc_tri_nam_o_hai_phia_truc_tung(ham_so, bien, tham_so):
    ham_f = phuong_trinh.tao_ham('f', ham_so, bien)
    loi_giai = huong_dan_giai.LoiGiai(
        "Tìm {0} để {1} có cực trị nằm ở hai phía của trục tung".format(
            xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
            xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_f))))

    # Buoc 1 tim tham so de ham so co cuc tri
    buoc_1 = tim_tham_so_de_ham_so_co_cuc_tri(ham_so, bien, tham_so)
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2 tim tham so de tich 2 nghiem am
    nghiem = buoc_1.cac_buoc_giai[2].cac_buoc_giai[2].dap_an
    nghiem_1, nghiem_2 = sympy.symbols(str(bien) + '_1 ' + str(bien) + '_2')
    dieu_kien = bat_dang_thuc.nho_hon(nghiem_1 * nghiem_2, 0)
    buoc_2 = huong_dan_giai.LoiGiai(
        'Giải bất đẳng thức {bdt} tìm {ts}'.format(bdt=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)),
                                                   ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so))))
    buoc_2.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)))

    # The bien
    dieu_kien = phuong_trinh.the_bien(dieu_kien, nghiem_1, nghiem[0])
    dieu_kien = phuong_trinh.the_bien(dieu_kien, nghiem_2, nghiem[1])

    # Giai bat dang thuc
    giai_bat_dang_thuc = bat_dang_thuc.giai_bat_dang_thuc_lg(dieu_kien, tham_so)
    buoc_2.cac_buoc_giai += giai_bat_dang_thuc.cac_buoc_giai
    buoc_2.dap_an=giai_bat_dang_thuc.dap_an

    loi_giai.them_thao_tac(buoc_2)

    # Buoc 3 tong hop
    buoc_3 = huong_dan_giai.LoiGiai("Tổng hợp kết quả")
    buoc_3.them_thao_tac("Tổng hợp 2 bước trên ta được:")
    tong_ket = tap_hop.tim_giao(buoc_1.dap_an, buoc_2.dap_an)
    buoc_3.them_thao_tac(xu_ly_chuoi.boc_mathjax(
        "{ts} \in {tk}".format(ts=xu_ly_chuoi.tao_latex(tham_so), tk=xu_ly_chuoi.tao_latex(tong_ket))))

    buoc_3.dap_an = tong_ket
    loi_giai.them_thao_tac(buoc_3)
    loi_giai.dap_an=tong_ket
    return loi_giai


def tim_tham_so_de_cuc_tri_nam_o_hai_phia_truc_hoanh(ham_so, bien, tham_so):
    ham_f = phuong_trinh.tao_ham('f', ham_so, bien)
    loi_giai = huong_dan_giai.LoiGiai(
        "Tìm {0} để {1} có cực trị nằm ở hai phía của trục hoành".format(
            xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
            xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_f))))

    # Buoc 1 tim tham so de ham so co cuc tri
    buoc_1 = tim_tham_so_de_ham_so_co_cuc_tri(ham_so, bien, tham_so)
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2 tim tham so de tich 2 nghiem am
    nghiem = buoc_1.cac_buoc_giai[2].cac_buoc_giai[2].dap_an
    nghiem_1, nghiem_2 = sympy.symbols(str(bien) + '_1 ' + str(bien) + '_2')
    dieu_kien = bat_dang_thuc.nho_hon(nghiem_1 * nghiem_2, 0)
    buoc_2 = huong_dan_giai.LoiGiai("Tìm nghiệm của bất đẳng thức {0}".format(
        xu_ly_chuoi.boc_mathjax("f({0})f({1})<0".format(xu_ly_chuoi.tao_latex(nghiem_1), xu_ly_chuoi.tao_latex(nghiem_2)))))

    # In ra dieu kien
    buoc_2.them_thao_tac(xu_ly_chuoi.boc_mathjax("f({0})f({1})<0".format(xu_ly_chuoi.tao_latex(nghiem_1), xu_ly_chuoi.tao_latex(nghiem_2))))

    # Thay cac nghiem vao
    f_nghiem_1 = phuong_trinh.the_bien(ham_so, bien, nghiem_1)
    f_nghiem_2 = phuong_trinh.the_bien(ham_so, bien, nghiem_2)

    dieu_kien = bat_dang_thuc.nho_hon(f_nghiem_1 * f_nghiem_2, 0)

    # In ra dieu kien sau khi thay nghiem
    buoc_2.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(dieu_kien)))

    # Thay bien vao
    dieu_kien = phuong_trinh.the_bien(dieu_kien, nghiem_1, nghiem[0])
    dieu_kien = phuong_trinh.the_bien(dieu_kien, nghiem_2, nghiem[1])

    # In ra dieu kien sau khi thay bien
    buoc_2.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(dieu_kien)))

    # Giai bat dang thuc
    giai_dieu_kien = bat_dang_thuc.giai_bat_dang_thuc_lg(dieu_kien,tham_so)
    buoc_2.cac_buoc_giai+=giai_dieu_kien.cac_buoc_giai
    buoc_2.dap_an=giai_dieu_kien.dap_an

    loi_giai.them_thao_tac(buoc_2)

    # buoc 3 tong hop ket qua
    buoc_3 = huong_dan_giai.LoiGiai("Tổng hợp kết quả")
    buoc_3.them_thao_tac("Tổng hợp kết quả của hai bước trước ta được")
    tong_hop = tap_hop.tim_giao(buoc_1.dap_an,buoc_1.dap_an)
    buoc_3.them_thao_tac(xu_ly_chuoi.boc_mathjax("{ts} \in {th}".format(ts=xu_ly_chuoi.tao_latex(tham_so),th=xu_ly_chuoi.tao_latex(tong_hop))))

    buoc_3.dap_an=tong_hop

    loi_giai.them_thao_tac(buoc_3)
    loi_giai.dap_an=tong_hop
    return loi_giai


if __name__ == "__main__":
    import sympy

    hs = sympy.sympify("x^3 - 3*m**2*x-2*m")
    b = sympy.Symbol('x')
    ts = sympy.Symbol('m')
    tim_tham_so_de_cuc_tri_nam_o_hai_phia_truc_hoanh(
        hs, b, ts).xuat_html("loi_giai.html")
