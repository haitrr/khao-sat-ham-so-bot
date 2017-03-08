import dao_ham
import gioi_han
import bang_bien_thien
import do_thi_ham_so
import xu_ly_chuoi as xlc
import cuc_tri
import tinh_xac_dinh
import phuong_trinh as pt
import diem_uon
import huong_dan_giai as hdg


def khao_sat_ham_so(ham_so):
    """
    Khao sat ham so va xuat loi giai
    :param ham_so: Sympy expression
    :return: string
    """
    # Xac dinh bien
    cac_bien = pt.lay_cac_bien(ham_so)
    if len(cac_bien) == 0 or len(cac_bien) > 1:
        raise ValueError("Ham so khong hop le")
    bien = cac_bien[0]

    de_bai = "Khảo sát hàm số : {0}".format(xlc.boc_mathjax(
        "f({0}) = {1}".format(xlc.tao_latex(bien), xlc.tao_latex(ham_so))))
    loi_giai = hdg.LoiGiai(de_bai)

    # Buoc 1 : Tap xac dinh
    buoc_1 = hdg.LoiGiai("Tìm tập xác định của hàm số")

    txd = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien)
    buoc_1.them_thao_tac(xlc.boc_mathjax("D=" + xlc.tao_latex(txd)))

    # Them ket qua
    buoc_1.dap_an = txd

    # Them vao loi giai
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2: Đạo hàm của hàm số
    buoc_2 = hdg.LoiGiai("Tính đạo hàm và tìm nghiệm của đạo hàm hàm số")
    # Tính đạo hàm
    buoc_2_1 = hdg.LoiGiai("Tính đạo hàm của hàm số")

    dao_ham_cap_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_2_1.them_thao_tac(xlc.boc_mathjax(
        "f'({0}) = ".format(xlc.tao_latex(bien)) + xlc.tao_latex(dao_ham_cap_1)))
    temp = pt.rut_gon(dao_ham_cap_1)
    if dao_ham_cap_1 != temp:
        dao_ham_cap_1 = temp
        buoc_2_1.them_thao_tac(xlc.boc_mathjax(
            "\Leftrightarrow f'({0}) = ".format(xlc.tao_latex(bien)) + xlc.tao_latex(
                dao_ham_cap_1)))

    # Them ket qua
    buoc_2_1.dap_an = dao_ham_cap_1
    buoc_2.them_thao_tac(buoc_2_1)

    # Tìm nghiệm của đạo hàm hàm số
    buoc_2_2 = hdg.LoiGiai("Tìm nghiệm của đạo hàm của hàm số: ")

    buoc_2_2.them_thao_tac(xlc.boc_mathjax("f'({0}) = 0".format(xlc.tao_latex(bien))))
    buoc_2_2.them_thao_tac(xlc.boc_mathjax("\Leftrightarrow " +
                                           xlc.tao_latex(dao_ham_cap_1) + "=0"))
    nghiem_dao_ham_cap_1 = pt.tim_nghiem_thuc(dao_ham_cap_1, bien)
    # In ra cac nghiem
    if len(nghiem_dao_ham_cap_1) == 0:
        cac_nghiem_latex = "Vô nghiệm."
        buoc_2_2.them_thao_tac(cac_nghiem_latex)
    else:
        cac_nghiem_latex = "{0} = ".format(xlc.tao_latex(bien))
        if len(nghiem_dao_ham_cap_1) > 1:
            cac_nghiem_latex += xlc.tao_ngoac_nhon(nghiem_dao_ham_cap_1)
        else:
            cac_nghiem_latex += xlc.tao_latex(nghiem_dao_ham_cap_1[0])
        buoc_2_2.them_thao_tac(xlc.boc_mathjax("\Leftrightarrow " + cac_nghiem_latex))
    # Them ket qua
    buoc_2_2.dap_an = nghiem_dao_ham_cap_1

    # Them vao loi giai
    buoc_2.them_thao_tac(buoc_2_2)
    loi_giai.them_thao_tac(buoc_2)

    # Buoc 3: Tim gioi han tai vo cuc
    buoc_3 = hdg.LoiGiai("Tìm giới hạn của hàm số tại vô cực ")

    gioi_han_vo_cuc = gioi_han.tim_gioi_han_tai_vo_cuc(ham_so, bien)

    buoc_3.them_thao_tac(xlc.boc_mathjax(
        "lim_{{{0}\\to-\infty}}{1}={2}".format(xlc.tao_latex(bien), xlc.tao_latex(ham_so),
                                               xlc.tao_latex(
                                                   gioi_han_vo_cuc[0]))))

    buoc_3.them_thao_tac(xlc.boc_mathjax(
        "lim_{{{0}\\to\infty}}{1}={2}".format(xlc.tao_latex(bien), xlc.tao_latex(ham_so),
                                              xlc.tao_latex(
                                                  gioi_han_vo_cuc[1]))))

    # Them ket qua
    buoc_3.dap_an = gioi_han_vo_cuc

    # Them vao loi giai
    loi_giai.them_thao_tac(buoc_3)

    # Buoc 4 : Ve bang bien thien
    buoc_4 = hdg.LoiGiai("Vẽ bảng biến thiên")

    # Luu bang bien thien vao file tam
    file_tam = bang_bien_thien.ve_bang_bien_thien(ham_so, bien)

    # Chen ma html
    buoc_4.them_thao_tac(xlc.tao_anh_html(file_tam))

    # Nhận xét hàm số
    buoc_4.them_thao_tac("Nhận xét :")

    # Cuc tieu
    cuc_tieu = cuc_tri.tim_diem_cuc_tieu(ham_so, bien)
    if len(cuc_tieu) == 0:
        buoc_4.them_thao_tac("Hàm số không có cực tiểu")
    else:
        if len(cuc_tieu) > 1:
            cac_diem = xlc.tao_ngoac_nhon(cuc_tieu)
        else:
            cac_diem = xlc.tao_latex(cuc_tieu[0])
        buoc_4.them_thao_tac("Hàm số đạt cực tiểu tại điểm : {0}".format(xlc.boc_mathjax(cac_diem)))

    # Cuc dai
    cuc_dai = cuc_tri.tim_diem_cuc_dai(ham_so, bien)
    if len(cuc_dai) == 0:
        buoc_4.them_thao_tac("Hàm số không có cực đại")
    else:
        if len(cuc_dai) > 1:
            cac_diem = xlc.tao_ngoac_nhon(cuc_dai)
        else:
            cac_diem = xlc.tao_latex(cuc_dai[0])
        buoc_4.them_thao_tac("Hàm số đạt cực đại tại điểm : {0}".format(xlc.boc_mathjax(cac_diem)))

    # Diem uon
    diem_uon_hs = diem_uon.tim_diem_uon(ham_so, bien)
    if len(diem_uon_hs) == 0:
        buoc_4.them_thao_tac("Hàm số không có điểm uốn")
    else:
        if len(diem_uon_hs) > 1:
            cac_diem = xlc.tao_ngoac_nhon(diem_uon_hs)
        else:
            cac_diem = xlc.tao_latex(diem_uon_hs[0])
        buoc_4.them_thao_tac("Hàm số có điểm uốn : {0}".format(
            xlc.boc_mathjax(cac_diem)))

    # Them vao loi giai
    buoc_4.dap_an = None
    loi_giai.them_thao_tac(buoc_4)

    # Buoc 5: Do thi ham so
    buoc_5 = hdg.LoiGiai("Vẽ đồ thị của hàm số")

    # Ve do thi ham so ra file tam
    file_tam = do_thi_ham_so.ve_do_thi(ham_so, bien)
    # Chen ma html
    buoc_5.them_thao_tac(xlc.tao_anh_html(file_tam))

    # Them loi giai
    buoc_5.dap_an = None
    loi_giai.them_thao_tac(buoc_5)

    return loi_giai


if __name__ == '__main__':
    import sympy

    hs = sympy.sympify("x^3+3*x^2-4", evaluate=False)
    b = sympy.Symbol('x')
    khao_sat_ham_so(
        hs).xuat_html("loi_giai.html")
