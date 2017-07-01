import bat_dang_thuc
import dao_ham
import dinh_nghia
import huong_dan_giai
import ky_hieu_latex
import phuong_trinh
import phuong_trinh_bac_2
import tinh_xac_dinh
import xu_ly_chuoi


# todo: Test
def tim_tham_so_de_ham_so_dong_bien_tren_tap_xac_dinh(ham_so, bien, tham_so):
    # De bai
    loi_giai = huong_dan_giai.LoiGiai("Tìm {0} để hàm số {1} đồng biến trên tập xác định".format(
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
        xu_ly_chuoi.boc_mathjax("f({0})={1}".format(xu_ly_chuoi.tao_latex(bien), xu_ly_chuoi.tao_latex(ham_so)))))
    # ----------------------CAU HOI---------------------------------
    ch1 = huong_dan_giai.HoiDap("Hàm số đồng biến tại một điểm khi nào ?")
    ch1.cac_goi_y.append("Giá trị của đạo hàm tại điểm đó như thế nào ?")
    da1 = huong_dan_giai.DapAnCauHoi(
        ("Đạo hàm có giá trị dương tại điểm đó!", [('dao ham', "f'"), ('duong', 'lon hon 0', '>0', '> 0')]))
    ch1.dap_an.append(da1)

    # ---------------------DINH NGHIA----------------------------
    loi_giai.cac_dinh_nghia.append(dinh_nghia.DE_HAM_SO_DONG_BIEN_TREN_TAP_XAC_DINH)

    # ------------------------BAI TOAN MAU----------------------
    hs_mau = sympy.sympify("x^3 + 3*m*x^2 + m*x + m")
    ts_mau = sympy.Symbol('m')
    bien_mau = sympy.Symbol('x')

    if ham_so - hs_mau != 0:
        loi_giai.loi_giai_mau = tim_tham_so_de_ham_so_dong_bien_tren_tap_xac_dinh(hs_mau, bien_mau, ts_mau).xuat_html()

    # -------------------LOI GIAI--------------------------
    # Buoc 1 tim tap xac dinh
    buoc_1 = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien)
    buoc_1.ten_loi_giai = 'Tìm tập xác định của hàm số'
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2 tim dao ham
    buoc_2 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)

    buoc_2.ten_loi_giai = "Tính đạo hàm của hàm số"

    loi_giai.them_thao_tac(buoc_2)

    # Buoc 3 tim tham so de dao ham lon hon hoac bang 0 tren R
    buoc_3 = phuong_trinh_bac_2.tim_tham_so_de_ham_so_lon_hon_hoac_bang_0(buoc_2.dap_an, bien, tham_so)
    buoc_3.ten_loi_giai = 'Tìm tham số để {bdt}'.format(
        bdt=xu_ly_chuoi.boc_mathjax("{dh}\ \\forall \in \mathbb{{R}}").format(
            dh=xu_ly_chuoi.tao_latex(bat_dang_thuc.lon_hon_hoac_bang(phuong_trinh.tao_ham("f'", bien, bien).lhs, 0))))
    loi_giai.them_thao_tac(buoc_3)
    loi_giai.dap_an = buoc_3.dap_an

    buoc_4 = huong_dan_giai.LoiGiai("Kết luận")
    if phuong_trinh.so_sanh(buoc_3.dap_an, sympy.EmptySet()):
        buoc_4.them_thao_tac('Vậy hàm số không đồng biến trên tập xác định với bất kỳ giá trị {ts} nào'.format(
            ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so))
        ))
    else:
        buoc_4.them_thao_tac('Vậy hàm số đồng biến trên tập xác định khi {ts}'.format(
            ts=xu_ly_chuoi.boc_mathjax("{ts}\ \in {ng}").format(ts=xu_ly_chuoi.tao_latex(tham_so),
                                                                ng=xu_ly_chuoi.tao_latex(buoc_3.dap_an)
                                                                )))
    loi_giai.them_thao_tac(buoc_4)
    return loi_giai


# todo: Test
def tim_tham_so_de_ham_so_nghich_bien_tren_tap_xac_dinh(ham_so, bien, tham_so):
    # De bai
    loi_giai = huong_dan_giai.LoiGiai("Tìm {0} để hàm số {1} nghịch biến trên tập xác định".format(
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
        xu_ly_chuoi.boc_mathjax("f({0})={1}".format(xu_ly_chuoi.tao_latex(bien), xu_ly_chuoi.tao_latex(ham_so)))))
    # --------------------------CAU HOI--------------------------
    ch1 = huong_dan_giai.HoiDap('Để hàm số nghịch biến trên tập xác định thì giá trị đạo hàm như thế nào?')
    ch1.cac_goi_y.append('Lớn hơn hay nhỏ hơn 0')
    da1 = huong_dan_giai.DapAnCauHoi('Nhỏ hơn hoặc bằng 0', ['nho hon', 'bang', ('khong', 0)])
    da2 = huong_dan_giai.DapAnCauHoi('<=0', ['<=0'])
    ch1.dap_an.append(da1)
    ch1.dap_an.append(da2)
    loi_giai.cac_cau_hoi.append(ch1)

    # --------------------------DINH NGHIA------------------------
    loi_giai.cac_dinh_nghia.append(dinh_nghia.DE_HAM_SO_NGHICH_BIEN_TREN_TAP_XAC_DINH)

    # ----------------------------MAU------------------------------
    hs_mau = sympy.sympify("x^3 + 3*m*x^2 + m*x + m")
    ts_mau = sympy.Symbol('m')
    bien_mau = sympy.Symbol('x')

    if ham_so - hs_mau != 0:
        loi_giai.loi_giai_mau = tim_tham_so_de_ham_so_nghich_bien_tren_tap_xac_dinh(hs_mau, bien_mau,
                                                                                    ts_mau).xuat_html()

    # --------------------------------LOI GIAI---------------------------
    # Buoc 1 tim tap xac dinh
    buoc_1 = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien)
    buoc_1.ten_loi_giai = 'Tìm tập xác định của hàm số'
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2 tim dao ham
    buoc_2 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)

    buoc_2.ten_loi_giai = "Tính đạo hàm của hàm số"

    loi_giai.them_thao_tac(buoc_2)

    # Buoc 3 tim tham so de dao ham lon hon hoac bang 0 tren R
    buoc_3 = phuong_trinh_bac_2.tim_tham_so_de_ham_so_nho_hon_hoac_bang_0(buoc_2.dap_an, bien, tham_so)
    buoc_3.ten_loi_giai = 'Tìm tham số để {bdt}'.format(
        bdt=xu_ly_chuoi.boc_mathjax("{dh}\ \\forall \in \mathbb{{R}}").format(
            dh=xu_ly_chuoi.tao_latex(bat_dang_thuc.nho_hon_hoac_bang(phuong_trinh.tao_ham("f'", bien, bien).lhs, 0))))
    loi_giai.them_thao_tac(buoc_3)
    loi_giai.dap_an = buoc_3.dap_an

    buoc_4 = huong_dan_giai.LoiGiai("Kết luận")
    if phuong_trinh.so_sanh(buoc_3.dap_an, sympy.EmptySet()):
        buoc_4.them_thao_tac('Vậy hàm số không nghịch biến trên tập xác định với bất kỳ giá trị {ts} nào'.format(
            ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so))
        ))
    else:
        buoc_4.them_thao_tac('Vậy hàm số nghịch biến trên tập xác định khi {ts}'.format(
            ts=xu_ly_chuoi.boc_mathjax("{ts}\ \in {ng}").format(ts=xu_ly_chuoi.tao_latex(tham_so),
                                                                ng=xu_ly_chuoi.tao_latex(buoc_3.dap_an)
                                                                )))
    loi_giai.them_thao_tac(buoc_4)
    return loi_giai


# todo: test
def tim_tham_so_de_ham_so_don_dieu_tren_1_khoang_co_do_dai_k(ham_so, bien, tham_so, do_dai_khoang):
    # De bai
    loi_giai = huong_dan_giai.LoiGiai("Tìm {0} để hàm số {1} đơn điệu trên khoảng có độ dài {do_dai}".format(
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
        xu_ly_chuoi.boc_mathjax("f({0})={1}".format(xu_ly_chuoi.tao_latex(bien), xu_ly_chuoi.tao_latex(ham_so))),
        do_dai=str(do_dai_khoang)))

    # ------------------------------------------CAU HOI----------------------
    ch1 = huong_dan_giai.HoiDap('Để làm được bài này ta sử dụng định lý nào đã học ?')
    ch1.cac_goi_y.append('Định nghĩa liên quan đến nghiệm của phương trình bậc 2')
    da = huong_dan_giai.DapAnCauHoi('Định lý Vi-et', [('vi-et', 'vi et')])
    ch1.dap_an.append(da)
    loi_giai.cac_cau_hoi.append(ch1)

    # -------------------------DINH NGHIA--------------------------------
    loi_giai.cac_dinh_nghia.append(dinh_nghia.DE_HAM_SO_DON_DIEU_TREN_MOT_KHOANG_CO_DO_DAI_CHO_TRUOC)
    loi_giai.cac_dinh_nghia.append(dinh_nghia.DINH_LY_VI_ET)

    # ------------------------------MAU------------------------------
    hs_mau = sympy.sympify("x^3 + 3*m*x^2 + m*x + m")
    ts_mau = sympy.Symbol('m')
    bien_mau = sympy.Symbol('x')
    khoang_mau = 1

    if ham_so - hs_mau != 0:
        loi_giai.loi_giai_mau = tim_tham_so_de_ham_so_don_dieu_tren_1_khoang_co_do_dai_k(hs_mau, bien_mau, ts_mau,
                                                                                         khoang_mau).xuat_html()

    # ----------------------------------LOI GIAI-----------------------------
    # Buoc 1 : Tim dao ham
    buoc_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_1.ten_loi_giai = 'Tìm đạo hàm của hàm số'

    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2 : Tim tham so de f' co 2 nghiem phan biet va quan he nghiem
    buoc_2 = huong_dan_giai.LoiGiai('Tìm {ts} để đạo hàm có 2 nghiệm phân biệt và quan hệ giữa 2 nghiệm'.format(
        ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so))))

    # Buoc 2.1: Tim tham so de f' co 2 nghiem phan biet
    buoc_2_1 = phuong_trinh_bac_2.tim_tham_so_de_phuong_trinh_hai_nghiem_phan_biet(buoc_1.dap_an, bien, tham_so)
    del buoc_2_1.cac_buoc_giai[2]
    buoc_2_1.ten_loi_giai = 'Tìm {ts} để đạo hàm có 2 nghiệm phân biệt'.format(
        ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)))

    buoc_2.them_thao_tac(buoc_2_1)
    # buoc 2.2: Tim quan he giua hai nghiem
    buoc_2_2 = phuong_trinh_bac_2.quan_he_2_nghiem_viet(buoc_1.dap_an, bien)
    buoc_2_2.ten_loi_giai = 'Áp dụng định lý Viet tìm quan hệ giữa hai nghiệm của đạo hàm'

    buoc_2.them_thao_tac(buoc_2_2)

    loi_giai.them_thao_tac(buoc_2)

    nghiem_1, nghiem_2 = sympy.symbols(str(bien) + '_1 ' + str(bien) + '_2')
    # buoc 3: phan tich dieu kien thanh dang viet
    buoc_3 = huong_dan_giai.LoiGiai('Phân tích điều kiện và đưa về dạng Vi-et')
    dieu_kien = bat_dang_thuc.bang(sympy.Abs(nghiem_1 - nghiem_2), do_dai_khoang)
    buoc_3.them_thao_tac('Để hàm số đơn điệu trên khoảng có độ dài {do_dai} thì {dk}'.format(
        do_dai=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(do_dai_khoang)),
        dk=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien))))

    buoc_3.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)))
    dieu_kien = bat_dang_thuc.bang((nghiem_1 + nghiem_2) ** 2 - 4 * nghiem_1 * nghiem_2, do_dai_khoang ** 2)

    buoc_3.them_thao_tac(xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(dieu_kien)))
    # chuyen ve
    dieu_kien = bat_dang_thuc.bang(dieu_kien.lhs - dieu_kien.rhs, 0)
    buoc_3.them_thao_tac(xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG + xu_ly_chuoi.tao_latex(dieu_kien)))

    buoc_3.dap_an = dieu_kien.lhs
    loi_giai.them_thao_tac(buoc_3)

    # Buoc 4: The nghiem,giai phuong trinh tim nghiem
    buoc_4 = huong_dan_giai.LoiGiai('Thế kết quả từ bước 2 vào bước 3 và giải phương trình tìm nghiệm')
    buoc_4.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)))
    buoc_4.them_thao_tac('Thế kết quả từ bước 2 ta được:')
    # The bien
    dieu_kien = phuong_trinh.the_bieu_thuc(dieu_kien, nghiem_1 + nghiem_2, buoc_2_2.dap_an[0])
    dieu_kien = phuong_trinh.the_bieu_thuc(dieu_kien, nghiem_1 * nghiem_2, buoc_2_2.dap_an[1])
    # buoc_4.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)))

    loi_giai_phuong_trinh = phuong_trinh.giai_phuong_trinh(dieu_kien.lhs, tham_so)
    buoc_4.cac_buoc_giai += loi_giai_phuong_trinh.cac_buoc_giai

    buoc_4.dap_an = loi_giai_phuong_trinh.dap_an
    loi_giai.them_thao_tac(buoc_4)

    # buoc 5 : tong hop ket qua
    buoc_5 = huong_dan_giai.LoiGiai('Tổng hợp kết quả và kết luận')
    buoc_5.them_thao_tac('Tổng hợp kết quả ta được:')
    thoa_man = []
    for nghiem in buoc_4.dap_an:
        if buoc_2_1.dap_an.contains(nghiem):
            thoa_man.append(nghiem)

    if thoa_man == []:
        buoc_5.them_thao_tac('Không có {ts} nào thỏa mãn điều kiện đề bài'.format(
            ts=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so))))
    else:
        buoc_5.them_thao_tac('Với {ts} thì hàm số {hs} đơn điệu trên khoảng có độ dài {do_dai}'.format(
            ts=xu_ly_chuoi.boc_mathjax('{tham_so}={nghiem}'.format(tham_so=xu_ly_chuoi.tao_latex(tham_so),
                                                                   nghiem=xu_ly_chuoi.tao_ngoac_nhon(thoa_man))),
            hs=xu_ly_chuoi.boc_mathjax("f({0})={1}".format(xu_ly_chuoi.tao_latex(bien), xu_ly_chuoi.tao_latex(ham_so))),
            do_dai=str(do_dai_khoang)))

    buoc_5.dap_an = thoa_man
    loi_giai.them_thao_tac(buoc_5)

    return loi_giai


if __name__ == '__main__':
    import sympy

    b = sympy.Symbol('x')
    ts = sympy.Symbol('m')


    def tim_tham_so_de_ham_so_dong_bien_tren_tap_xac_dinh_test():
        hs = sympy.sympify("x^3+3*x**2+m*x+m")
        tim_tham_so_de_ham_so_dong_bien_tren_tap_xac_dinh(hs, b, ts).xuat_html('loi_giai.html')


    def tim_tham_so_de_ham_so_nghich_bien_tren_tap_xac_dinh_test():
        hs = sympy.sympify("x^3+3*x**2+m*x+m")
        tim_tham_so_de_ham_so_nghich_bien_tren_tap_xac_dinh(hs, b, ts).xuat_html('loi_giai.html')


    def tim_tham_so_de_ham_so_don_dieu_tren_1_khoang_co_do_dai_k_test():
        hs = sympy.sympify("x^3+3*x^2+m*x+m")
        k = 1
        tim_tham_so_de_ham_so_don_dieu_tren_1_khoang_co_do_dai_k(hs, b, ts, k).xuat_html('loi_giai.html')


    # tim_tham_so_de_ham_so_dong_bien_tren_tap_xac_dinh_test()
    # tim_tham_so_de_ham_so_nghich_bien_tren_tap_xac_dinh_test()
    tim_tham_so_de_ham_so_don_dieu_tren_1_khoang_co_do_dai_k_test()
