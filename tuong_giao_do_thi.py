import bat_dang_thuc
import dao_ham
import huong_dan_giai
import ky_hieu_latex
import phuong_trinh
import phuong_trinh_bac_2
import tap_hop
import xu_ly_chuoi
import dinh_nghia


# todo: test
def tim_toa_do_giao_diem_voi_duong_thang(ham_so, bien, duong_thang):
    loi_giai = huong_dan_giai.LoiGiai(
        'Tìm tọa độ giao điểm của đồ thị hàm số {0} với đường thẳng {1}'.
        format(
            xu_ly_chuoi.boc_mathjax("f({0})={1}".format(
                xu_ly_chuoi.tao_latex(bien), xu_ly_chuoi.tao_latex(ham_so))),
            xu_ly_chuoi.boc_mathjax("f({0})={1}".format(
                xu_ly_chuoi.tao_latex(bien), xu_ly_chuoi.tao_latex(
                    duong_thang)))))

    # -----------------------CAU HOI----------------------
    ch1 = huong_dan_giai.HoiDap("Để tìm giao điểm thì chúng ta cần làm gì?")
    ch1.cac_goi_y.append("Lập phương trình gì?")
    da = huong_dan_giai.DapAnCauHoi("Lập phương trình hoành độ giao điểm",
                                    ["hoanh do giao diem"])
    ch1.da_an.append(da)
    loi_giai.cac_cau_hoi.append(ch1)

    # --------------------------DINH NGHIA------------------
    loi_giai.cac_dinh_nghia.append(
        dinh_nghia.GIAO_DIEM_CUA_DO_THI_HAM_SO_VOI_DUONG_THANG)

    # ----------------------------MAU-----------------
    hs_mau = sympy.sympify("x**2")
    bien_mau = sympy.Symbol("x")
    dt_mau = sympy.sympify("2+x")

    if hs_mau - ham_so != 0:
        loi_giai.loi_giai_mau = tim_toa_do_giao_diem_voi_duong_thang(
            hs_mau, bien_mau, dt_mau).xuat_html()

    # --------------------------BAI GIAI--------------------

    # Buoc 1 lap phuong trinh hoanh do giao diem
    buoc_1 = huong_dan_giai.LoiGiai("Lập phương trình hoành độ giao điểm")
    buoc_1.them_thao_tac("Ta có phương trình hoành độ giao điểm :")

    pt_hoanh_do_giao_diem = bat_dang_thuc.bang(ham_so, duong_thang)

    # In ra pt hoanh do giao diem
    buoc_1.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(pt_hoanh_do_giao_diem)))

    pt_hoanh_do_giao_diem = phuong_trinh.rut_gon(
        bat_dang_thuc.bang(pt_hoanh_do_giao_diem.lhs -
                           pt_hoanh_do_giao_diem.rhs, 0))

    buoc_1.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                xu_ly_chuoi.tao_latex(pt_hoanh_do_giao_diem)))

    buoc_1.dap_an = pt_hoanh_do_giao_diem
    loi_giai.them_thao_tac(buoc_1)
    # Buoc 2: Giai pt hoanh do giao diem tim nghiem
    buoc_2 = huong_dan_giai.LoiGiai(
        "Tìm nghiệm của phương trình hoành độ giao điểm")

    # In ra pt hoanh do giao diem
    buoc_2.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(pt_hoanh_do_giao_diem)))

    # Chuyển vế phải sang vế trái
    pt_hoanh_do_giao_diem = bat_dang_thuc.bang(
        pt_hoanh_do_giao_diem.lhs - pt_hoanh_do_giao_diem.rhs, 0)

    # In ra pt hoanh do giao diem sau khi chuyen ve
    buoc_2.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                xu_ly_chuoi.tao_latex(pt_hoanh_do_giao_diem)))

    # Rut gon pt hoanh do giao diem
    pt_hoanh_do_giao_diem = phuong_trinh.phan_tich_thanh_nhan_tu(
        pt_hoanh_do_giao_diem)

    # In ra pt hoanh do giao diem
    buoc_2.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                xu_ly_chuoi.tao_latex(pt_hoanh_do_giao_diem)))

    # Giai phuong trinh
    nghiem = phuong_trinh.tim_nghiem_thuc(pt_hoanh_do_giao_diem, bien)
    if len(nghiem) == 0:
        buoc_2.them_thao_tac("Phương trình vô nghiệm")
    elif len(nghiem) == 1:
        buoc_2.them_thao_tac(
            xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                    xu_ly_chuoi.tao_latex(
                                        bat_dang_thuc.bang(bien, nghiem[0]))))
    else:
        buoc_2.them_thao_tac(
            xu_ly_chuoi.
            boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG + "{0}={1}".format(
                xu_ly_chuoi.tao_latex(bien), xu_ly_chuoi.tao_latex(nghiem))))

    # Luu dap an
    buoc_2.dap_an = nghiem
    loi_giai.them_thao_tac(buoc_2)

    if buoc_2.dap_an:
        # Buoc 3 tu cac nghiem xac dinh giao diem
        buoc_3 = huong_dan_giai.LoiGiai(
            "Từ các nghiệm xác định tọa độ các giao điểm")

        # Giai thich
        buoc_3.them_thao_tac(
            "Ta xác định giao điểm theo dạng ({0},{1})".format(
                xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(bien)),
                xu_ly_chuoi.boc_mathjax("f({0})".format(
                    xu_ly_chuoi.tao_latex(bien)))))

        # In ra cac diem
        cac_diem = [(hoanh, phuong_trinh.tao_ten_ham('f', hoanh))
                    for hoanh in nghiem]
        buoc_3.them_thao_tac(
            xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_ngoac_nhon(cac_diem)))

        cac_diem = [(hoanh, phuong_trinh.the_bien(ham_so, bien, hoanh))
                    for hoanh in nghiem]
        buoc_3.them_thao_tac(
            xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                    xu_ly_chuoi.tao_ngoac_nhon(cac_diem)))

        cac_diem = [(hoanh, phuong_trinh.rut_gon(d[1]))
                    for hoanh, d in zip(nghiem, cac_diem)]
        buoc_3.them_thao_tac(
            xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                    xu_ly_chuoi.tao_ngoac_nhon(cac_diem)))

        buoc_3.dap_an = cac_diem
        loi_giai.them_thao_tac(buoc_3)
    else:
        buoc_3 = None
    # buoc 4 : Ket luan
    buoc_4 = huong_dan_giai.LoiGiai('Kết luận')
    if not buoc_2.dap_an:
        buoc_4.them_thao_tac(
            'Vậy đồ thị hàm số {hs} không cắt đường thẳng {dt}'.format(
                hs=xu_ly_chuoi.boc_mathjax("f({0})={1}".format(
                    xu_ly_chuoi.tao_latex(bien), xu_ly_chuoi.tao_latex(
                        ham_so))),
                dt=xu_ly_chuoi.boc_mathjax("f({0})={1}".format(
                    xu_ly_chuoi.tao_latex(bien),
                    xu_ly_chuoi.tao_latex(duong_thang)))))
    else:
        buoc_4.them_thao_tac(
            'Vậy đồ thị hàm số {hs} cắt đường thẳng {dt} tại các điểm : {diem} '.
            format(
                hs=xu_ly_chuoi.boc_mathjax("f({0})={1}".format(
                    xu_ly_chuoi.tao_latex(bien), xu_ly_chuoi.tao_latex(
                        ham_so))),
                dt=xu_ly_chuoi.boc_mathjax("f({0})={1}".format(
                    xu_ly_chuoi.tao_latex(bien),
                    xu_ly_chuoi.tao_latex(duong_thang))),
                diem=xu_ly_chuoi.boc_mathjax(
                    xu_ly_chuoi.tao_ngoac_nhon(buoc_3.dap_an))))
    loi_giai.them_thao_tac(buoc_4)
    return loi_giai


# todo: test
def tim_tham_so_de_ham_so_cat_truc_hoanh_tai_1_diem_duy_nhat(ham_so, bien,
                                                             tham_so):
    # Tao loi giai
    loi_giai = huong_dan_giai.LoiGiai(
        "Tim {0} để đồ thị hàm số {1} cắt trục hoành tại một điểm duy nhất".
        format(
            xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
            xu_ly_chuoi.boc_mathjax("f({0})={1}".format(
                xu_ly_chuoi.tao_latex(bien), xu_ly_chuoi.tao_latex(ham_so)))))
    # ------------------------------------CAU HOI-------------------------
    ch1 = huong_dan_giai.HoiDap("Bài toán này có mấy trường hợp ?")
    da1 = huong_dan_giai.DapAnCauHoi("Hai", [('hai', '2')])
    ch1.dap_an.append(da1)
    loi_giai.cac_cau_hoi.append(ch1)

    ch2 = huong_dan_giai.HoiDap(
        "Trong trường hợp hàm số có hai cực trị thì hai cực trị phải như thế nào?"
    )
    ch2.cac_goi_y.append("Nằm ở hai phía của trục ...?")
    da2 = huong_dan_giai.DapAnCauHoi("Năm ở hai phía trục hoành",
                                     [('2', 'hai'), "truc hoanh"])
    ch2.dap_an.append(da2)
    loi_giai.cac_cau_hoi.append(ch2)
    # --------------------------------------DINH NGHIA----------------------
    loi_giai.cac_dinh_nghia.append(
        dinh_nghia.DE_DO_THI_HAM_SO_CAT_TRUC_HOANH_TAI_MOT_DIEM_DUY_NHAT)

    # ----------------------------------------MAU---------------------------
    hs_mau = sympy.sympify("x^3+3*x^2+m*x+m-2")
    bien_mau = sympy.Symbol('x')
    ts_mau = sympy.Symbol('m')

    if hs_mau - ham_so != 0:
        loi_giai.loi_giai_mau = tim_tham_so_de_ham_so_cat_truc_hoanh_tai_1_diem_duy_nhat(
            hs_mau, bien_mau, ts_mau).xuat_html()
    # ------------------------------------------BAI GIAI---------------------
    # Buoc 1: Tinh dao ham cua ham so
    buoc_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_1.ten_loi_giai = "Tính đạo hàm của hàm số"
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2
    buoc_2 = phuong_trinh_bac_2.tim_tham_so_de_phuong_trinh_co_nghiem_kep_hoac_vo_nghiem(
        buoc_1.dap_an, bien, tham_so)
    buoc_2.ten_loi_giai = "Xét trường hợp 1: Hàm số không có cực trị hay " + xu_ly_chuoi.boc_mathjax(
        "f'({0})=0".format(xu_ly_chuoi.tao_latex(
            bien))) + " có nghiệm kép hoặc vô nghiệm"

    loi_giai.them_thao_tac(buoc_2)

    # Buoc 3
    # Truong hop 2
    buoc_3 = huong_dan_giai.LoiGiai(
        "Xét trường hợp 2: Hàm số có hai cực trị ở cùng phía của trục hoành")

    # Buoc 3.1 tim tham so de f'(x)=0 co hai nghiem phan biet
    buoc_3_1 = phuong_trinh_bac_2.tim_tham_so_de_phuong_trinh_hai_nghiem_phan_biet(
        buoc_1.dap_an, bien, tham_so)
    buoc_3_1.ten_loi_giai = "Tìm {0} để {1} có hai nghiệm phân biệt".format(
        xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(tham_so)),
        xu_ly_chuoi.boc_mathjax(
            "f'({0})=0".format(xu_ly_chuoi.tao_latex(bien))))

    # Them buoc 3.1 vao buoc 3
    buoc_3.them_thao_tac(buoc_3_1)
    # Buoc 3.2 hai nghiem nam o hai phia cua truc hoanh
    nghiem_1, nghiem_2 = sympy.symbols(str(bien) + '_1 ' + str(bien) + '_2')

    buoc_3_2 = huong_dan_giai.LoiGiai(
        "Tìm nghiệm của bất đẳng thức {0}".format(
            xu_ly_chuoi.boc_mathjax("f({0})*f({1})>0".format(
                xu_ly_chuoi.tao_latex(nghiem_1),
                xu_ly_chuoi.tao_latex(nghiem_2)))))

    # In ra dieu kien
    xu_ly_chuoi.boc_mathjax("f({0})*f({1})>0".format(
        xu_ly_chuoi.tao_latex(nghiem_1), xu_ly_chuoi.tao_latex(nghiem_2)))

    # Thay cac nghiem vao
    f_nghiem_1 = phuong_trinh.the_bien(ham_so, bien, nghiem_1)
    f_nghiem_2 = phuong_trinh.the_bien(ham_so, bien, nghiem_2)

    dieu_kien = bat_dang_thuc.lon_hon(f_nghiem_1 * f_nghiem_2, 0)

    # In ra dieu kien sau khi thay nghiem
    buoc_3_2.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                xu_ly_chuoi.tao_latex(dieu_kien)))

    # Thay bien vao
    dieu_kien = phuong_trinh.the_bien(dieu_kien, nghiem_1,
                                      buoc_3_1.cac_buoc_giai[2].dap_an[0])
    dieu_kien = phuong_trinh.the_bien(dieu_kien, nghiem_2,
                                      buoc_3_1.cac_buoc_giai[2].dap_an[1])

    # In ra dieu kien sau khi thay bien
    buoc_3_2.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                xu_ly_chuoi.tao_latex(dieu_kien)))

    # Rut gon
    dieu_kien = phuong_trinh.phan_tich_thanh_nhan_tu(dieu_kien)

    # In ra
    buoc_3_2.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                xu_ly_chuoi.tao_latex(dieu_kien)))

    # Giải set
    nghiem = bat_dang_thuc.giai_bat_dang_thuc_set(dieu_kien, tham_so)

    buoc_3_2.them_thao_tac("Giải hệ bất đẳng thức ta được {0}".format(
        xu_ly_chuoi.boc_mathjax("{0} \in {1}".format(
            xu_ly_chuoi.tao_latex(tham_so), xu_ly_chuoi.tao_latex(nghiem)))))

    buoc_3_2.dap_an = nghiem
    buoc_3.them_thao_tac(buoc_3_2)

    # Buoc 3.3 tong hop ket qua
    buoc_3_3 = huong_dan_giai.LoiGiai("Tổng hợp kết quả của hai bước trước")

    # Tong hop ket qua
    tong_hop_nghiem_buoc_3 = tap_hop.tim_giao(buoc_3_2.dap_an, buoc_3_1.dap_an)

    # In ra
    buoc_3_3.them_thao_tac(
        "Tổng hợp kết quả của hai bước trước ta được {0}".format(
            xu_ly_chuoi.boc_mathjax("{0} \in {1}".format(
                xu_ly_chuoi.tao_latex(tham_so),
                xu_ly_chuoi.tao_latex(tong_hop_nghiem_buoc_3)))))

    # Luu dap an
    buoc_3_3.dap_an = tong_hop_nghiem_buoc_3
    buoc_3.dap_an = tong_hop_nghiem_buoc_3

    # Them buoc 3.3 vao buoc 3
    buoc_3.them_thao_tac(buoc_3_3)

    # Them buoc 3 vao loi giai
    loi_giai.them_thao_tac(buoc_3)

    # Buoc 4 tong hop ket qua cua buoc 2 va buoc 3
    buoc_4 = huong_dan_giai.LoiGiai("Tổng hợp kết quả và kết luận")
    tong_hop = tap_hop.tim_hop(buoc_2.dap_an, buoc_3.dap_an)

    # In ra kq
    buoc_4.them_thao_tac(
        "Tổng hợp kết quả của hai trường hợp ta được {0}".format(
            xu_ly_chuoi.boc_mathjax("{0} \in {1}".format(
                xu_ly_chuoi.tao_latex(tham_so), xu_ly_chuoi.tao_latex(
                    tong_hop)))))

    buoc_4.them_thao_tac(
        "Vậy với {ts} thì đồ thị hàm số cắt trục hoành tại một điểm duy nhất.".
        format(ts=xu_ly_chuoi.boc_mathjax("{0} \in {1}".format(
            xu_ly_chuoi.tao_latex(tham_so), xu_ly_chuoi.tao_latex(tong_hop)))))
    # Luu ket qua
    buoc_4.dap_an = tong_hop

    # Them buoc 4 vao loi giai
    loi_giai.dap_an = tong_hop
    loi_giai.them_thao_tac(buoc_4)
    return loi_giai


#todo: hoan thanh
def viet_phuong_trinh_tiep_voi_do_thi_ham_so_tai_mot_diem(ham_so, bien, diem):
    """
    Viet phuong trinh tiep tuyen voi do thi ham so tai mot diem
    :param ham_so: ham so
    :param bien: bien 
    :param diem: hoanh do cua diem
    :return: 
    """
    ham_f = phuong_trinh.tao_ham('f', ham_so, bien)
    loi_giai = huong_dan_giai.LoiGiai(
        "Viết phương trình tiếp tuyến với đồ thì hàm số {hs} tại điểm {d}".
        format(
            hs=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_f)),
            d=xu_ly_chuoi.boc_mathjax(
                xu_ly_chuoi.tao_latex(bat_dang_thuc.bang(bien, diem)))))
    fx = phuong_trinh.tao_ten_ham("f", diem)
    # Buoc 1 : Xac dinh f(x0)
    buoc_1 = phuong_trinh.thay_bien(ham_so, bien, diem)
    buoc_1.ten_loi_giai = 'Xác định {f0}'.format(
        f0=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(fx)))

    # Buoc 2: Tinh dao ham cua ham so
    buoc_2 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_2.ten_loi_giai = 'Tìm đạo hàm của hàm số'

    f = phuong_trinh.tao_ten_ham("f'", diem)
    # Buoc 3 : Tim y'(x0)
    buoc_3 = phuong_trinh.thay_bien(buoc_2.dap_an, bien, diem)
    buoc_3.ten_loi_giai = "Tính {f0}".format(
        f0=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(f)))

    # Buoc 4: Phuong trinh tiep tuyen: y=y'(x0)(x-x0)+y0
    pt = f * (bien - diem) + fx
    buoc_4 = huong_dan_giai.LoiGiai(
        "Phương trình tiếp tuyến cần tìm có dạng {p}".format(
            p=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(pt))))

    buoc_4.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(pt)))
    pt = phuong_trinh.the_bien(pt, fx, buoc_1.dap_an)
    pt = phuong_trinh.the_bien(pt, f, buoc_3.dap_an)
    buoc_4.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                xu_ly_chuoi.tao_latex(pt)))
    pt = phuong_trinh.rut_gon(pt)
    buoc_4.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                xu_ly_chuoi.tao_latex(pt)))
    buoc_4.dap_an = pt

    # Buoc 5 : Ket luan
    buoc_5 = huong_dan_giai.LoiGiai("Kết luận")
    buoc_5.them_thao_tac('Vậy phương trình tiếp tuyến cần tìm là {pt}'.format(
        pt=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(buoc_4.dap_an))))

    loi_giai.them_thao_tac(buoc_1)
    loi_giai.them_thao_tac(buoc_2)
    loi_giai.them_thao_tac(buoc_3)
    loi_giai.them_thao_tac(buoc_4)
    loi_giai.them_thao_tac(buoc_5)
    return loi_giai


#todo:hoan thanh
def viet_phuong_trinh_tiep_tuyen_voi_do_thi_co_he_so_goc(ham_so, bien,
                                                         he_so_goc):
    """
    Viet phuong trinh tiep tuyen voi do thi ham so co he so goc biet truoc
    Truong hop f'=hsg vo nghiem : Chua giai quyet
    Tat ca loai ham so
    :param ham_so: 
    :param bien: 
    :param he_so_goc: 
    :return: 
    """
    ham_f = phuong_trinh.tao_ham('f', ham_so, bien)
    loi_giai = huong_dan_giai.LoiGiai(
        "Viết phương trình tiếp tuyến với đồ thị hàm số {hs} có hệ số góc là {hsg}".
        format(
            hs=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_f)),
            hsg=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(he_so_goc))))

    # Buoc 1 : Tinh dao ham
    buoc_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_1.ten_loi_giai = 'Tính đạo hàm của hàm số'

    dao_ham_f = phuong_trinh.tao_ten_ham("f'", bien)
    pt = bat_dang_thuc.bang(dao_ham_f, he_so_goc)

    # Buoc 2: Giai pt f'=k
    buoc_2 = huong_dan_giai.LoiGiai('Giải phương trình {pt} tìm nghiệm'.format(
        pt=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(pt))))
    buoc_2.them_thao_tac(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(pt)))
    pt = bat_dang_thuc.bang(buoc_1.dap_an, he_so_goc)
    buoc_2.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                xu_ly_chuoi.tao_latex(pt)))
    pt = bat_dang_thuc.bang(buoc_1.dap_an - he_so_goc, 0)
    buoc_2.them_thao_tac(
        xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                xu_ly_chuoi.tao_latex(pt)))
    giai_pt = phuong_trinh.giai_phuong_trinh(pt.lhs, bien)
    buoc_2.cac_buoc_giai += giai_pt.cac_buoc_giai[1:]
    buoc_2.dap_an = giai_pt.dap_an

    # Buoc 3 : Xac dinh tiep diem
    buoc_3 = huong_dan_giai.LoiGiai(
        'Thế các nghiệm tìm được vào ham số, xác định tiếp điểm')
    buoc_3.dap_an = list()
    for nghiem in buoc_2.dap_an:
        thay_b = phuong_trinh.thay_bien(ham_so, bien, nghiem)
        buoc_3.cac_buoc_giai += thay_b.cac_buoc_giai
        buoc_3.them_thao_tac(
            'Vậy ta được tiếp điểm {td}'.format(td=xu_ly_chuoi.boc_mathjax(
                xu_ly_chuoi.tao_latex((nghiem, thay_b.dap_an)))))
        buoc_3.dap_an.append((nghiem, thay_b.dap_an))

    # Buoc 4: Lap phuong trinh tiep tuyen
    buoc_4 = huong_dan_giai.LoiGiai(
        'Lập phương trình tiếp tuyến dựa trên các tiếp điểm')
    x_td = sympy.Symbol(str(bien) + '_td')
    y_td = phuong_trinh.tao_ten_ham('f', x_td)
    with sympy.evaluate(False):
        pt = he_so_goc * (bien - x_td) + y_td
    buoc_4.them_thao_tac('Phương trình tiếp tuyến có dạng {pt}'.format(
        pt=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(pt))))
    buoc_4.dap_an = []
    for td in buoc_3.dap_an:
        pttt = phuong_trinh.thay_bien(pt, [y_td, x_td], [td[1], td[0]])
        buoc_4.cac_buoc_giai += pttt.cac_buoc_giai
        buoc_4.dap_an.append(pttt.dap_an)

    # Buoc 5: Ket luan
    buoc_5 = huong_dan_giai.LoiGiai('Kết luận')
    buoc_5.them_thao_tac(
        'Vậy phương trình tiếp tuyến với đồ thị hàm số có hệ số góc {hsg} là {tt}'.
        format(
            hsg=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(he_so_goc)),
            tt=xu_ly_chuoi.boc_mathjax(
                xu_ly_chuoi.tao_ngoac_nhon(buoc_4.dap_an))))

    loi_giai.them_thao_tac(buoc_1)
    loi_giai.them_thao_tac(buoc_2)
    loi_giai.them_thao_tac(buoc_3)
    loi_giai.them_thao_tac(buoc_4)
    loi_giai.them_thao_tac(buoc_5)
    loi_giai.dap_an = buoc_4.dap_an
    return loi_giai


#todo:hoan thanh
def viet_phuong_trinh_tiep_tuyen_voi_do_thi_ham_so_di_qua_mot_diem(ham_so,
                                                                   bien, diem):
    """
    Tim tiep tuyen voi do thi ham so di qua mot diem cho truoc
    Chua xu ly : Truong hop pt giao diem khong co nghiem
    :param ham_so: 
    :param bien: 
    :param diem: 
    :return: 
    """
    ham_f = phuong_trinh.tao_ham('f', ham_so, bien)
    loi_giai = huong_dan_giai.LoiGiai(
        'Viết phương trình tiếp tuyến với đồ thị hàm số {hs} đi qua điểm {d}'.
        format(
            hs=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_so)),
            d=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(diem))))

    # Buoc 1: tim dao ham cua ham so
    buoc_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_1.ten_loi_giai = 'Tìm đạo hàm của hàm số'

    # Buoc 2: Tim hoanh do cua tiep diem
    buoc_2 = huong_dan_giai.LoiGiai('Tìm hoành độ tiếp điểm')
    dao_ham_f = phuong_trinh.tao_ten_ham("f'", bien)
    pt = dao_ham_f * (bien - diem[0]) + diem[1]

    buoc_2.them_thao_tac('Tiếp tuyến đi qua điểm {d} nên có dạng {p}'.format(
        d=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(diem)),
        p=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(pt))))
    pt = bat_dang_thuc.bang(ham_f.lhs, dao_ham_f * (bien - diem[0]) + diem[1])
    buoc_2.them_thao_tac(
        'Vậy hoành độ của tiếp điểm là nghiệm của phương trình sau {p}'.format(
            d=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(diem)),
            p=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(pt))))
    # Thay bien vao
    tb = phuong_trinh.thay_bien(pt, [ham_f.lhs, dao_ham_f],
                                [ham_so, buoc_1.dap_an])

    # Giai phuong trinh
    buoc_2.cac_buoc_giai += tb.cac_buoc_giai

    giai_pt = phuong_trinh.giai_phuong_trinh(tb.dap_an, bien)
    buoc_2.cac_buoc_giai += giai_pt.cac_buoc_giai
    buoc_2.dap_an = giai_pt.dap_an

    # B3: Thay hoanh do vao tinh tung do cua giao diem
    buoc_3 = huong_dan_giai.LoiGiai(
        'Thay hoành độ vào hàm số tìm tung độ của tiếp điểm')
    tiep_diem = []
    buoc_3.dap_an = []
    for n in buoc_2.dap_an:
        thay_b = phuong_trinh.thay_bien(ham_so, bien, n)
        buoc_3.cac_buoc_giai += thay_b.cac_buoc_giai
        buoc_3.them_thao_tac(
            'Vậy ta được tiếp điểm {td}'.format(td=xu_ly_chuoi.boc_mathjax(
                xu_ly_chuoi.tao_latex((n, thay_b.dap_an)))))
        tiep_diem.append([n, thay_b.dap_an])
        buoc_3.dap_an.append(thay_b.dap_an)
    # B4: Lap phuong trinh tiep tuyen
    buoc_4 = huong_dan_giai.LoiGiai(
        'Lập phương trình tiếp tuyến tương ứng với các tiếp điểm')
    buoc_4.dap_an = list()
    for td in tiep_diem:
        buoc_4.them_thao_tac(
            'Tiếp tuyến với đồ thị hàm số tại điểm {d} có dạng:'.format(
                d=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(td))))
        dao_ham_f_td = phuong_trinh.tao_ten_ham("f'", td[0])
        pttt = dao_ham_f_td * (bien - td[0]) - td[1]
        buoc_4.them_thao_tac(
            xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(pttt)))

        pttt = phuong_trinh.the_bien(buoc_1.dap_an, bien, td[0]) * (
            bien - td[0]) - td[1]
        buoc_4.them_thao_tac(
            xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                    xu_ly_chuoi.tao_latex(pttt)))

        pttt = phuong_trinh.tach_ra(pttt)
        buoc_4.them_thao_tac(
            xu_ly_chuoi.boc_mathjax(ky_hieu_latex.DAU_TUONG_DUONG +
                                    xu_ly_chuoi.tao_latex(pttt)))
        buoc_4.dap_an.append(pttt)

    # Buoc 5 : Ket luan
    buoc_5 = huong_dan_giai.LoiGiai("Kết luận")
    if len(buoc_4.dap_an) == 0:
        buoc_5.them_thao_tac(
            'Vậy không có tiếp tuyến thỏa mãn điều kiện đề bài')
    elif len(buoc_4.dap_an) == 1:
        buoc_5.them_thao_tac(
            'Vậy tiếp tuyến với đồ thị hàm số đi qua điểm {d} là {tt}'.format(
                d=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(diem)),
                tt=xu_ly_chuoi.boc_mathjax(
                    xu_ly_chuoi.tao_latex(buoc_4.dap_an[0]))))
    else:
        buoc_5.them_thao_tac(
            'Vậy các tiếp tuyến với đồ thị hàm số đi qua điểm {d} là {tt}'.
            format(
                d=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(diem)),
                tt=xu_ly_chuoi.boc_mathjax(
                    xu_ly_chuoi.tao_ngoac_nhon(buoc_4.dap_an))))

    loi_giai.them_thao_tac(buoc_1)
    loi_giai.them_thao_tac(buoc_2)
    loi_giai.them_thao_tac(buoc_3)
    loi_giai.them_thao_tac(buoc_4)
    loi_giai.them_thao_tac(buoc_5)
    return loi_giai


if __name__ == "__main__":
    import sympy

    b = sympy.Symbol('x')
    ts = sympy.Symbol('m')

    def tim_tham_so_de_ham_so_cat_truc_hoanh_tai_1_diem_duy_nhat_test():
        hs = sympy.sympify("x^3 +3*x**2+m*x+m-2")
        tim_tham_so_de_ham_so_cat_truc_hoanh_tai_1_diem_duy_nhat(
            hs, b, ts).xuat_html("loi_giai.html")

    def tim_toa_do_giao_diem_voi_duong_thang_test():
        d = sympy.sympify("x+2")
        hs = sympy.sympify("x**2")
        tim_toa_do_giao_diem_voi_duong_thang(hs, b,
                                             d).xuat_html("loi_giai.html")

    def viet_phuong_trinh_tiep_voi_do_thi_ham_so_tai_mot_diem_test():
        hs = sympy.sympify("x**3-2*x+1")
        d = 2
        viet_phuong_trinh_tiep_voi_do_thi_ham_so_tai_mot_diem(
            hs, b, d).xuat_html("loi_giai.html")

    def viet_phuong_trinh_tiep_tuyen_voi_do_thi_co_he_so_goc_test():
        hs = sympy.sympify("(2*x)/(x-1)")
        hsg = -2
        viet_phuong_trinh_tiep_tuyen_voi_do_thi_co_he_so_goc(
            hs, b, hsg).xuat_html("loi_giai.html")

    def viet_phuong_trinh_tiep_tuyen_voi_do_thi_ham_so_di_qua_mot_diem_test():
        hs = sympy.sympify("x**3-3*x+1")
        diem = (1, -1)
        viet_phuong_trinh_tiep_tuyen_voi_do_thi_ham_so_di_qua_mot_diem(
            hs, b, diem).xuat_html("loi_giai.html")

    # tim_toa_do_giao_diem_voi_duong_thang_test()
    # viet_phuong_trinh_tiep_voi_do_thi_ham_so_tai_mot_diem_test()
    # tim_tham_so_de_ham_so_cat_truc_hoanh_tai_1_diem_duy_nhat_test()
    #viet_phuong_trinh_tiep_tuyen_voi_do_thi_co_he_so_goc_test()
    viet_phuong_trinh_tiep_tuyen_voi_do_thi_ham_so_di_qua_mot_diem_test()
