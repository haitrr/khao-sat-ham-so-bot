import dao_ham
import gioi_han
import bang_bien_thien
import do_thi_ham_so
import xu_ly_chuoi
import cuc_tri
import hang_so
import tinh_xac_dinh
import phuong_trinh
import diem_uon


def khao_sat_ham_so(ham_so, bien):
    loi_giai = []
    buoc_1 = list()
    # Tap xac dinh
    buoc_1.append("Tập xác định của hàm số")
    txd = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien)
    buoc_1.append(xu_ly_chuoi.boc_latex_mathjax("D=" + xu_ly_chuoi.tao_chuoi_latex(txd)))
    loi_giai.append(buoc_1)

    buoc_2 = list()
    # Chieu bien thien
    buoc_2.append("Xét chiều biến thiên của hàm số")
    # Tim nghiem dao ham
    buoc_2.append("Đạo hàm của hàm số :")

    dao_ham_cap_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_2.append(xu_ly_chuoi.boc_latex_mathjax(
        "y'(x) = " + xu_ly_chuoi.tao_chuoi_latex(dao_ham_cap_1)))
    temp = phuong_trinh.rut_gon(dao_ham_cap_1)
    if dao_ham_cap_1 != temp:
        dao_ham_cap_1 = temp
        buoc_2.append(xu_ly_chuoi.boc_latex_mathjax(
            "\Leftrightarrow y'(x) = " + xu_ly_chuoi.tao_chuoi_latex(dao_ham_cap_1)))

    buoc_2.append("Nghiệm của đạo hàm của hàm số: ")
    buoc_2.append(xu_ly_chuoi.boc_latex_mathjax("y'(x) = 0"))
    buoc_2.append(xu_ly_chuoi.boc_latex_mathjax("\Leftrightarrow " +
                                                xu_ly_chuoi.tao_chuoi_latex(dao_ham_cap_1) + "=0"))
    nghiem_dao_ham_cap_1 = phuong_trinh.tim_nghiem_thuc(dao_ham_cap_1, bien)

    # In ra cac nghiem
    if len(nghiem_dao_ham_cap_1) == 0:
        cac_nghiem_latex = "Vô nghiệm."
        buoc_2.append(cac_nghiem_latex)
    else:
        cac_nghiem_latex = "x = "
        if len(nghiem_dao_ham_cap_1) > 1:
            cac_nghiem_latex += xu_ly_chuoi.tao_ngoac_nhon_latex(nghiem_dao_ham_cap_1)
        else:
            cac_nghiem_latex += xu_ly_chuoi.tao_chuoi_latex(nghiem_dao_ham_cap_1[0])
        buoc_2.append(xu_ly_chuoi.boc_latex_mathjax("\Leftrightarrow " + cac_nghiem_latex))
    # Tim gioi han tai vo cuc
    gioi_han_vo_cuc = gioi_han.tim_gioi_han_tai_vo_cuc(ham_so, bien)

    buoc_2.append("Giới hạn của hàm số: ")

    buoc_2.append(xu_ly_chuoi.boc_latex_mathjax(
        "lim_{x\\to-\infty}" + xu_ly_chuoi.tao_chuoi_latex(ham_so) + "=" + xu_ly_chuoi.tao_chuoi_latex(
            gioi_han_vo_cuc[0])))

    buoc_2.append(xu_ly_chuoi.boc_latex_mathjax(
        "lim_{x\\to\infty}" + xu_ly_chuoi.tao_chuoi_latex(ham_so) + "=" + xu_ly_chuoi.tao_chuoi_latex(
            gioi_han_vo_cuc[1])))
    loi_giai.append(buoc_2)

    # Ve bang bien thien
    buoc_3 = list()
    buoc_3.append("Vẽ bảng biến thiên")
    # Luu bang bien thien vao file
    file_tam = bang_bien_thien.ve_bang_bien_thien(ham_so, bien)

    # Chen ma html
    buoc_3.append("<img src=\"" + hang_so.THU_MUC_TAM + file_tam + "\">")

    loi_giai.append(buoc_3)
    # Tim cuc tri cua ham so
    buoc_4 = list()
    buoc_4.append("Cực trị của hàm số")

    # Cuc tieu
    cuc_tieu = cuc_tri.diem_cuc_tieu(ham_so, bien)
    if len(cuc_tieu) == 0:
        buoc_4.append("Hàm số không có cực tiểu")
    else:
        if len(cuc_tieu) > 1:
            cac_diem = xu_ly_chuoi.tao_ngoac_nhon_latex(cuc_tieu)
        else:
            cac_diem = xu_ly_chuoi.tao_chuoi_latex(cuc_tieu[0])
        buoc_4.append("Hàm số đạt cực tiểu tại điểm : " +
                      xu_ly_chuoi.boc_latex_mathjax(cac_diem))

    # Cuc dai
    cuc_dai = cuc_tri.diem_cuc_dai(ham_so, bien)
    if len(cuc_dai) == 0:
        buoc_4.append("Hàm số không có cực đại")
    else:
        if len(cuc_dai) > 1:
            cac_diem = xu_ly_chuoi.tao_ngoac_nhon_latex(cuc_dai)
        else:
            cac_diem = xu_ly_chuoi.tao_chuoi_latex(cuc_dai[0])
        buoc_4.append("Hàm số đạt cực đại tại điểm : " +
                      xu_ly_chuoi.boc_latex_mathjax(cac_diem))

    # Diem uon
    diem_uon_hs = diem_uon.tim_diem_uon(ham_so, bien)
    if len(diem_uon_hs) == 0:
        buoc_4.append("Hàm số không có điểm uốn")
    else:
        if len(diem_uon_hs) > 1:
            cac_diem = xu_ly_chuoi.tao_ngoac_nhon_latex(diem_uon_hs)
        else:
            cac_diem = xu_ly_chuoi.tao_chuoi_latex(diem_uon_hs[0])
        buoc_4.append("Hàm số có điểm uốn : " +
                      xu_ly_chuoi.boc_latex_mathjax(cac_diem))
    loi_giai.append(buoc_4)

    buoc_5 = list()
    buoc_5.append("Đồ thị của hàm số")

    # Ve do thi ham so ra file tam
    file_tam = do_thi_ham_so.ve_do_thi(ham_so, bien)
    # Chen ma html
    buoc_5.append("<img src=\"" + hang_so.THU_MUC_TAM + file_tam + "\">")

    loi_giai.append(buoc_5)

    return loi_giai


if __name__ == '__main__':
    import sympy

    hs = sympy.sympify("x^2")
    b = sympy.Symbol('x')
    khao_sat_ham_so(hs, b)
