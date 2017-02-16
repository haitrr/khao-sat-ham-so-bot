from dao_ham import *
from gioi_han import *
from bang_bien_thien import *
from do_thi_ham_so import *
from xu_ly_chuoi import *
from cuc_tri import *
from bieu_thuc import *


def khao_sat_ham_so(ham_so, bien):

    loi_giai = []
    buoc_1 = []
    # Tap xac dinh
    buoc_1.append("Tập xác định của hàm số")
    txd = tap_xac_dinh(ham_so, bien)
    buoc_1.append(boc_latex_mathjax("D =" + tao_chuoi_latex(txd)))
    loi_giai.append(buoc_1)

    buoc_2 = []
    # Chieu bien thien
    buoc_2.append("Xét chiều biến thiên của hàm số")
    # Tim nghiem dao ham
    buoc_2.append("Đạo hàm của hàm số :")

    dao_ham_cap_1 = tinh_dao_ham_cap_1(ham_so, bien)
    buoc_2.append(boc_latex_mathjax(
        "y'(x) = " + tao_chuoi_latex(dao_ham_cap_1)))
    temp = rut_gon(dao_ham_cap_1)
    if(dao_ham_cap_1 != temp):
        dao_ham_cap_1 = temp
        buoc_2.append(boc_latex_mathjax(
            "\Leftrightarrow y'(x) = " + tao_chuoi_latex(dao_ham_cap_1)))

    buoc_2.append("Nghiệm của đạo hàm của hàm số: ")
    buoc_2.append(boc_latex_mathjax("y'(x) = 0"))
    buoc_2.append(boc_latex_mathjax("\Leftrightarrow " +
                                    tao_chuoi_latex(dao_ham_cap_1) + "=0"))
    nghiem_dao_ham_cap_1 = tim_nghiem_thuc(dao_ham_cap_1, bien)

    # In ra cac nghiem
    cac_nghiem_latex = "x = "
    if len(nghiem_dao_ham_cap_1) > 1:
        cac_nghiem_latex += tao_ngoac_nhon_latex(nghiem_dao_ham_cap_1)
    else:
        cac_nghiem_latex += tao_chuoi_latex(nghiem_dao_ham_cap_1[0])
    buoc_2.append(boc_latex_mathjax("\Leftrightarrow " + cac_nghiem_latex))
    # Tim gioi han tai vo cuc
    gioi_han = tim_gioi_han_tai_vo_cuc(ham_so, bien)

    buoc_2.append("Giới hạn của hàm số: ")

    buoc_2.append(boc_latex_mathjax(
        "lim_{x\\to-\infty}" + tao_chuoi_latex(ham_so) + "=" + tao_chuoi_latex(gioi_han[0])))

    buoc_2.append(boc_latex_mathjax(
        "lim_{x\\to\infty}" + tao_chuoi_latex(ham_so) + "=" + tao_chuoi_latex(gioi_han[1])))
    loi_giai.append(buoc_2)

    # Ve bang bien thien
    buoc_3 = []
    buoc_3.append("Vẽ bảng biến thiên")
    # Luu bang bien thien vao file
    ve_bang_bien_thien(ham_so, bien, "bang_bien_thien.png")

    # Chen ma html
    buoc_3.append("<img src=\"./bang_bien_thien.png\">")

    loi_giai.append(buoc_3)
    # Tim cuc tri cua ham so
    buoc_4 = []
    buoc_4.append("Cực trị của hàm số")

    # Cuc tieu
    cuc_tieu = diem_cuc_tieu(ham_so, bien)
    if len(cuc_tieu) == 0:
        buoc_4.append("Hàm số không có cực tiểu")
    else:
        if len(cuc_tieu) > 1:
            cac_diem = tao_ngoac_nhon_latex(cuc_tieu)
        else:
            cac_diem = tao_chuoi_latex(cuc_tieu[0])
        buoc_4.append("Hàm số đạt cực tiểu tại điểm : " +
                      boc_latex_mathjax(cac_diem))

    # Cuc dai
    cuc_dai = diem_cuc_dai(ham_so, bien)
    if len(cuc_dai) == 0:
        buoc_4.append("Hàm số không có cực đại")
    else:
        if len(cuc_dai) > 1:
            cac_diem = tao_ngoac_nhon_latex(cuc_dai)
        else:
            cac_diem = tao_chuoi_latex(cuc_dai[0])
        buoc_4.append("Hàm số đạt cực đại tại điểm : " +
                      boc_latex_mathjax(cac_diem))
    loi_giai.append(buoc_4)

    buoc_5 = []
    buoc_5.append("Đồ thị của hàm số")
    ve_do_thi(ham_so, bien, "do_thi.png")
    # Chen ma html
    buoc_5.append("<img src=\"./do_thi.png\">")

    loi_giai.append(buoc_5)

    return loi_giai
