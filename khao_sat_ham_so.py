import bang_bien_thien
import cuc_tri
import dao_ham
import diem_uon
import do_thi_ham_so
import gioi_han
import huong_dan_giai
import phuong_trinh
import tinh_xac_dinh
import xu_ly_chuoi
import sympy
import ky_hieu_latex


def khao_sat_ham_so(ham_so, bien):
    """
    Khao sat ham so va xuat loi giai
    :param ham_so: Sympy expression
    :return: string
    """

    de_bai = "Khảo sát hàm số : {0}".format(
        xu_ly_chuoi.boc_mathjax("f({0}) = {1}".format(
            xu_ly_chuoi.tao_latex(bien), xu_ly_chuoi.tao_latex(ham_so))))
    loi_giai = huong_dan_giai.LoiGiai(de_bai)

    # -------------------------------CAU HOI------------------------------
    cau_hoi_1 = huong_dan_giai.HoiDap("Khảo sát hàm số gồm bao nhiêu bước?")
    dap_an_cau_1 = huong_dan_giai.DapAnCauHoi("5 bước", [("5", "nam")])
    cau_hoi_1.dap_an.append(dap_an_cau_1)
    loi_giai.cac_cau_hoi.append(cau_hoi_1)

    cau_hoi_2 = huong_dan_giai.HoiDap("Đầu tiên chúng ta cần làm gì ?")
    dap_an_cau_2 = huong_dan_giai.DapAnCauHoi("Tìm tập xác định của hàm số",
                                              ["xac dinh"])
    cau_hoi_2.dap_an.append(dap_an_cau_2)
    loi_giai.cac_cau_hoi.append(cau_hoi_2)

    # ----------------------------------BAI TOAN MAU--------------------
    ham_so_mau = sympy.sympify("x**3+3*(x**2)-4")
    bien_mau = sympy.Symbol('x')

    if ham_so_mau - ham_so != 0:
        loi_giai.loi_giai_mau = khao_sat_ham_so(ham_so_mau,
                                                bien_mau).xuat_html()

    # ---------------------------------BAI GIAI-------------------------
    # Buoc 1 : Tap xac dinh
    buoc_1 = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien)
    buoc_1.ten_loi_giai = 'Tìm tập xác định của hàm số'

    # Them vao loi giai
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2: Xet su bien thien
    xet_su_bt = huong_dan_giai.LoiGiai("Xét sự biến thiên của hàm số")
    # Buoc 2: Đạo hàm của hàm số
    buoc_2 = huong_dan_giai.LoiGiai(
        "Xét chiều biến thiên của hàm số")
    # Tính đạo hàm
    buoc_2_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_2_1.ten_loi_giai = "Tính đạo hàm của hàm số"
    dao_ham_cap_1 = buoc_2_1.dap_an
    buoc_2.them_thao_tac(buoc_2_1)

    # Tìm nghiệm của đạo hàm hàm số
    buoc_2_2 = phuong_trinh.giai_phuong_trinh(dao_ham_cap_1, bien)
    buoc_2_2.ten_loi_giai = "Tìm nghiệm của phương phương trình đạo hàm"

    # todo Khoang dong bien, nghich bien
    buoc_2_3 = huong_dan_giai.LoiGiai("Khoảng đồng biến,nghịch biến của hàm số")
    buoc_2_3_1 = huong_dan_giai.LoiGiai("Khoảng đồng biến")
    
    buoc_2_3_2 = huong_dan_giai.LoiGiai("Khoảng nghịch biến")

    # Them vao loi giai
    buoc_2.dap_an = buoc_2_2.dap_an
    buoc_2.them_thao_tac(buoc_2_2)
    xet_su_bt.them_thao_tac(buoc_2)
    #loi_giai.them_thao_tac(buoc_2)

    # Buoc 3: Tim gioi han tai vo cuc
    buoc_3 = huong_dan_giai.LoiGiai("Tìm giới hạn của hàm số tại vô cực ")

    gioi_han_vo_cuc = gioi_han.tim_gioi_han_tai_vo_cuc(ham_so, bien)

    buoc_3.them_thao_tac(
        xu_ly_chuoi.boc_mathjax("lim_{{{0}\\to-\infty}}{1}={2}".format(
            xu_ly_chuoi.tao_latex(bien),
            xu_ly_chuoi.tao_latex(ham_so),
            xu_ly_chuoi.tao_latex(gioi_han_vo_cuc[0]))))
    buoc_3.them_thao_tac(
        xu_ly_chuoi.boc_mathjax("lim_{{{0}\\to\infty}}{1}={2}".format(
            xu_ly_chuoi.tao_latex(bien),
            xu_ly_chuoi.tao_latex(ham_so),
            xu_ly_chuoi.tao_latex(gioi_han_vo_cuc[1]))))

    # Them ket qua
    buoc_3.dap_an = gioi_han_vo_cuc

    # Them vao loi giai
    #loi_giai.them_thao_tac(buoc_3)
    xet_su_bt.them_thao_tac(buoc_3)

    # Buoc 4 : Ve bang bien thien
    buoc_4 = huong_dan_giai.LoiGiai("Vẽ bảng biến thiên")

    # Luu bang bien thien vao file tam
    file_tam = bang_bien_thien.ve_bang_bien_thien(ham_so, bien)

    # Chen ma html
    buoc_4.them_thao_tac(xu_ly_chuoi.tao_anh_html(file_tam))

    # Nhận xét hàm số
    buoc_4.them_thao_tac("Nhận xét :")

    # Cuc tieu
    cuc_tieu = cuc_tri.tim_diem_cuc_tieu(ham_so, bien)
    if len(cuc_tieu) == 0:
        buoc_4.them_thao_tac("Hàm số không có cực tiểu")
    else:
        if len(cuc_tieu) > 1:
            cac_diem = xu_ly_chuoi.tao_ngoac_nhon(cuc_tieu)
        else:
            cac_diem = xu_ly_chuoi.tao_latex(cuc_tieu[0])
        buoc_4.them_thao_tac("Hàm số đạt cực tiểu tại điểm : {0}".format(
            xu_ly_chuoi.boc_mathjax(cac_diem)))

    # Cuc dai
    cuc_dai = cuc_tri.tim_diem_cuc_dai(ham_so, bien)
    if len(cuc_dai) == 0:
        buoc_4.them_thao_tac("Hàm số không có cực đại")
    else:
        if len(cuc_dai) > 1:
            cac_diem = xu_ly_chuoi.tao_ngoac_nhon(cuc_dai)
        else:
            cac_diem = xu_ly_chuoi.tao_latex(cuc_dai[0])
        buoc_4.them_thao_tac("Hàm số đạt cực đại tại điểm : {0}".format(
            xu_ly_chuoi.boc_mathjax(cac_diem)))

    # Diem uon
    diem_uon_hs = diem_uon.tim_diem_uon(ham_so, bien)
    if len(diem_uon_hs) == 0:
        #buoc_4.them_thao_tac("Hàm số không có điểm uốn")
        pass
    else:
        if len(diem_uon_hs) > 1:
            cac_diem = xu_ly_chuoi.tao_ngoac_nhon(diem_uon_hs)
        else:
            cac_diem = xu_ly_chuoi.tao_latex(diem_uon_hs[0])
        buoc_4.them_thao_tac("Hàm số có điểm uốn : {0}".format(
            xu_ly_chuoi.boc_mathjax(cac_diem)))

    # Them vao loi giai
    buoc_4.dap_an = None
    xet_su_bt.them_thao_tac(buoc_4)
    loi_giai.them_thao_tac(xet_su_bt)

    # Buoc 5: Do thi ham so
    buoc_5 = huong_dan_giai.LoiGiai("Vẽ đồ thị của hàm số")
    # TODO: Tìm giao điểm với trục tung
    gdtt = phuong_trinh.thay_bien(ham_so, bien, 0).dap_an
    if gdtt:
        buoc_5.them_thao_tac("Giao điểm của đồ thị hàm số với trục tung:")
        buoc_5.them_thao_tac(xu_ly_chuoi.boc_mathjax("{b} = 0 {sr} {hs} = {ds}".format(
            b=xu_ly_chuoi.tao_latex(bien),
            sr=ky_hieu_latex.SUY_RA,
            hs=phuong_trinh.tao_ten_ham('f', bien),
            ds=xu_ly_chuoi.tao_latex(gdtt)
        )))
    # todo: Tìm giao điểm với trục hoành
    gdth = phuong_trinh.giai_phuong_trinh(ham_so, bien).dap_an
    if gdth:
        buoc_5.them_thao_tac("Giao điểm của đồ thị hàm số với trục hoành:")
        buoc_5.them_thao_tac(xu_ly_chuoi.boc_mathjax("{hs} = 0 {sr} {b} = {ds}".format(
            b=xu_ly_chuoi.tao_latex(bien),
            sr=ky_hieu_latex.SUY_RA,
            hs=phuong_trinh.tao_ten_ham('f', bien),
            ds=xu_ly_chuoi.tao_ngoac_nhon(gdth)
        )))
    # todo: Tìm tiệm cận ngang
    if gioi_han_vo_cuc[1]!= sympy.oo and gioi_han_vo_cuc[1]!=-sympy.oo:
        buoc_5.them_thao_tac("Ta có " +
                             xu_ly_chuoi.boc_mathjax("lim_{{{0}\\to\infty}}{1}={2}".format(
                                 xu_ly_chuoi.tao_latex(bien),
                                 xu_ly_chuoi.tao_latex(ham_so),
                                 xu_ly_chuoi.tao_latex(gioi_han_vo_cuc[1]))))
        buoc_5.them_thao_tac(
            "Vậy {} là tiệm cận ngang của đồ thị hàm số".format(xu_ly_chuoi.boc_mathjax("{hs} = {n}".format(
                hs=phuong_trinh.tao_ten_ham('f', bien),
                n=xu_ly_chuoi.tao_latex(gioi_han_vo_cuc[1])
            ))))
    # todo: tìm tiệm cận dọc
    t = tinh_xac_dinh.tim_khong_xac_dinh(ham_so, bien)
    tcd = None
    k = None
    if t:
        for i in t:
            k = gioi_han.tim_gioi_han_duong(ham_so, bien, i)
            if k == sympy.oo or k == -sympy.oo:
                tcd = i
                break
    if tcd:
        buoc_5.them_thao_tac("Ta có " +
                             xu_ly_chuoi.boc_mathjax("lim_{{{0}\\to{d}}}{1}={2}".format(
                                 xu_ly_chuoi.tao_latex(bien),
                                 xu_ly_chuoi.tao_latex(ham_so),
                                 xu_ly_chuoi.tao_latex(k),
                                 d=xu_ly_chuoi.tao_latex(tcd) + "^{+}")))
        buoc_5.them_thao_tac(
            "Vậy {} là tiệm cận đứng của đồ thị hàm số".format(xu_ly_chuoi.boc_mathjax("{b} = {n}".format(
                b=xu_ly_chuoi.tao_latex(bien),
                n=xu_ly_chuoi.tao_latex(i)
            ))))
    # Ve do thi ham so ra file tam
    file_tam = do_thi_ham_so.ve_do_thi(ham_so, bien)
    # Chen ma html
    buoc_5.them_thao_tac(xu_ly_chuoi.tao_anh_html(file_tam))

    # Them loi giai
    buoc_5.dap_an = None
    loi_giai.them_thao_tac(buoc_5)

    return loi_giai


if __name__ == '__main__':
    import sympy

    #
    # hs = sympy.sympify("-x^3+3*x+2", evaluate=False)
    b = sympy.Symbol('x')
    hs = sympy.sympify("(x+4)/(3*x-8)")
    khao_sat_ham_so(hs, b).xuat_html("loi_giai.html")
