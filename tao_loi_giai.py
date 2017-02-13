import sympy as sp
from cac_thao_tac_khao_sat_ham_so import *
import latex2mathml.converter


def xuat_bieu_thuc_mathml(file, bieu_thuc):
    file.write("<math>")
    file.write(latex2mathml.converter.convert(sp.latex(bieu_thuc)))
    file.write("</math>")


def xuat_bieu_thuc_mathml_tu_latex(file, chuoi_latex):
    file.write("<math>")
    file.write(latex2mathml.converter.convert(chuoi_latex))
    file.write("</math>")

def xuong_dong(file):
    file.write("<br>")


def khao_sat_ham_so(ham_so, bien):
    file_loi_giai = open("loi_giai.html", "w", encoding='utf8')
    sp.init_printing()
    file_loi_giai.write("<!doctype html><html><head><meta charset=\"UTF-8\"><title>MathML Examples</title><script type=\"text/javascript\" src=\"http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML\"></script></head><body>")

    # Tap xac dinh
    file_loi_giai.write("<b>Bước 1: Tập xác định của hàm số</b>")
    xuong_dong(file_loi_giai)

    # Tim tap xac dinh
    txd = tap_xac_dinh(ham_so, bien)
    if sp.S.Reals.is_subset(txd):
        file_loi_giai.write("D = R")
    else:
        file_loi_giai.write("D = ")
        print(latex(txd))
        xuat_bieu_thuc_mathml(file_loi_giai, txd)
    xuong_dong(file_loi_giai)

    # Chieu bien thien
    file_loi_giai.write("<b>Bước 2: Xét chiều biến thiên của hàm số</b>")
    xuong_dong(file_loi_giai)

    # Tim nghiem dao ham
    file_loi_giai.write("Đạo hàm của hàm số :")

    dao_ham_cap_1 = tinh_dao_ham_cap_1(ham_so, bien)
    xuat_bieu_thuc_mathml_tu_latex(file_loi_giai, "y'(x) = "+ sp.latex(dao_ham_cap_1))

    xuong_dong(file_loi_giai)

    file_loi_giai.write("Nghiệm của đạo hàm của hàm số: ")
    xuat_bieu_thuc_mathml_tu_latex(file_loi_giai,"y'(x) = 0")
    xuong_dong(file_loi_giai)
    xuat_bieu_thuc_mathml_tu_latex(file_loi_giai, sp.latex(dao_ham_cap_1)+"=0")
    nghiem_dao_ham_cap_1 = tim_nghiem_thuc(dao_ham_cap_1, bien)
    xuong_dong(file_loi_giai)

    # In ra cac nghiem
    for nghiem in nghiem_dao_ham_cap_1:
        xuat_bieu_thuc_mathml_tu_latex(file_loi_giai, "x = "+sp.latex(nghiem))
        file_loi_giai.write(" ,")
    xuong_dong(file_loi_giai)

    # Tim gioi han tai vo cuc
    gioi_han = tim_gioi_han_tai_vo_cuc(ham_so,bien)
    file_loi_giai.write("Giới hạn của hàm số: ")
    xuong_dong(file_loi_giai)
    xuat_bieu_thuc_mathml_tu_latex(file_loi_giai,"lim_{x\\to-\infty}"+sp.latex(ham_so)+"="+sp.latex(gioi_han[0]))
    xuong_dong(file_loi_giai)
    xuat_bieu_thuc_mathml_tu_latex(
    file_loi_giai, "lim_{x\\to\infty}" + sp.latex(ham_so) + "=" + sp.latex(gioi_han[1]))
    xuong_dong(file_loi_giai)

    file_loi_giai.write("<b>Bước 3: Vẽ bảng biến thiên</b>")
    xuong_dong(file_loi_giai)
    ve_bang_bien_thien(ham_so,bien,"temp.png")
    file_loi_giai.write("<img src=\"./temp.png\">")
    xuong_dong(file_loi_giai)

    file_loi_giai.write("<b>Bước 4: Cực trị của hàm số</b>")


    file_loi_giai.write("</body></html>")
    file_loi_giai.close()


x = sp.Symbol('x')
t = sp.sympify("x^4 - 2*(x^2)-3")
#t = sp.sympify("1/x")
khao_sat_ham_so(t, x)
