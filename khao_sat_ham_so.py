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

def khao_sat_ham_so(ham_so, bien):
    """
    Khao sat ham so va xuat loi giai
    :param ham_so: Sympy expression
    :return: string
    """

    de_bai = "Khảo sát hàm số : {0}".format(xu_ly_chuoi.boc_mathjax(
        "f({0}) = {1}".format(xu_ly_chuoi.tao_latex(bien), xu_ly_chuoi.tao_latex(ham_so))))
    loi_giai = huong_dan_giai.LoiGiai(de_bai)

    # -------------------------------CAU HOI------------------------------
    cau_hoi_1 = huong_dan_giai.HoiDap("Khảo sát hàm số gồm bao nhiêu bước?")
    dap_an_cau_1 = huong_dan_giai.DapAnCauHoi("5 bước", [("5", "nam")])
    cau_hoi_1.dap_an.append(dap_an_cau_1)
    loi_giai.cac_cau_hoi.append(cau_hoi_1)

    cau_hoi_2 = huong_dan_giai.HoiDap("Đầu tiên chúng ta cần làm gì ?")
    dap_an_cau_2 = huong_dan_giai.DapAnCauHoi("Tìm tập xác định của hàm số", ["xac dinh"])
    cau_hoi_2.dap_an.append(dap_an_cau_2)
    loi_giai.cac_cau_hoi.append(cau_hoi_2)

    # ----------------------------------BAI TOAN MAU--------------------
    ham_so_mau = sympy.sympify("x**3+3*(x**2)-4")
    bien_mau = sympy.Symbol('x')

    if ham_so_mau - ham_so != 0:
        loi_giai.loi_giai_mau = khao_sat_ham_so(ham_so_mau, bien_mau).xuat_html()

    # ---------------------------------BAI GIAI-------------------------
    # Buoc 1 : Tap xac dinh
    buoc_1 = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien)
    buoc_1.ten_loi_giai = 'Tìm tập xác định của hàm số'

    # Them vao loi giai
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2: Đạo hàm của hàm số
    buoc_2 = huong_dan_giai.LoiGiai("Tính đạo hàm và tìm nghiệm của đạo hàm hàm số")
    # Tính đạo hàm
    buoc_2_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_2_1.ten_loi_giai = "Tính đạo hàm của hàm số"
    dao_ham_cap_1 = buoc_2_1.dap_an
    buoc_2.them_thao_tac(buoc_2_1)

    # Tìm nghiệm của đạo hàm hàm số
    buoc_2_2 = phuong_trinh.giai_phuong_trinh(dao_ham_cap_1, bien)
    buoc_2_2.ten_loi_giai = "Tìm nghiệm của phương phương trình đạo hàm"

    # Them vao loi giai
    buoc_2.them_thao_tac(buoc_2_2)
    loi_giai.them_thao_tac(buoc_2)

    # Buoc 3: Tim gioi han tai vo cuc
    buoc_3 = huong_dan_giai.LoiGiai("Tìm giới hạn của hàm số tại vô cực ")

    gioi_han_vo_cuc = gioi_han.tim_gioi_han_tai_vo_cuc(ham_so, bien)

    buoc_3.them_thao_tac(xu_ly_chuoi.boc_mathjax(
        "lim_{{{0}\\to-\infty}}{1}={2}".format(xu_ly_chuoi.tao_latex(bien), xu_ly_chuoi.tao_latex(ham_so),
                                               xu_ly_chuoi.tao_latex(
                                                   gioi_han_vo_cuc[0]))))

    buoc_3.them_thao_tac(xu_ly_chuoi.boc_mathjax(
        "lim_{{{0}\\to\infty}}{1}={2}".format(xu_ly_chuoi.tao_latex(bien), xu_ly_chuoi.tao_latex(ham_so),
                                              xu_ly_chuoi.tao_latex(
                                                  gioi_han_vo_cuc[1]))))

    # Them ket qua
    buoc_3.dap_an = gioi_han_vo_cuc

    # Them vao loi giai
    loi_giai.them_thao_tac(buoc_3)

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
        buoc_4.them_thao_tac("Hàm số đạt cực tiểu tại điểm : {0}".format(xu_ly_chuoi.boc_mathjax(cac_diem)))

    # Cuc dai
    cuc_dai = cuc_tri.tim_diem_cuc_dai(ham_so, bien)
    if len(cuc_dai) == 0:
        buoc_4.them_thao_tac("Hàm số không có cực đại")
    else:
        if len(cuc_dai) > 1:
            cac_diem = xu_ly_chuoi.tao_ngoac_nhon(cuc_dai)
        else:
            cac_diem = xu_ly_chuoi.tao_latex(cuc_dai[0])
        buoc_4.them_thao_tac("Hàm số đạt cực đại tại điểm : {0}".format(xu_ly_chuoi.boc_mathjax(cac_diem)))

    # Diem uon
    diem_uon_hs = diem_uon.tim_diem_uon(ham_so, bien)
    if len(diem_uon_hs) == 0:
        buoc_4.them_thao_tac("Hàm số không có điểm uốn")
    else:
        if len(diem_uon_hs) > 1:
            cac_diem = xu_ly_chuoi.tao_ngoac_nhon(diem_uon_hs)
        else:
            cac_diem = xu_ly_chuoi.tao_latex(diem_uon_hs[0])
        buoc_4.them_thao_tac("Hàm số có điểm uốn : {0}".format(
            xu_ly_chuoi.boc_mathjax(cac_diem)))

    # Them vao loi giai
    buoc_4.dap_an = None
    loi_giai.them_thao_tac(buoc_4)

    # Buoc 5: Do thi ham so
    buoc_5 = huong_dan_giai.LoiGiai("Vẽ đồ thị của hàm số")

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

    hs = sympy.sympify("x^3+3*x^2-4", evaluate=False)
    b = sympy.Symbol('x')
    khao_sat_ham_so(
        hs, b).xuat_html("loi_giai.html")
