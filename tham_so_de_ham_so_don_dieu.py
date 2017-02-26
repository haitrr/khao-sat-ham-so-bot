import xu_ly_chuoi
import dao_ham


def tim_tham_so_de_ham_so_dong_bien_tren_tap_xac_dinh(ham_so, bien):
    loi_giai = list()

    buoc_1 = list()
    dao_ham_cap_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_1.append("Đạo hàm của hàm số")
    buoc_1.append(xu_ly_chuoi.boc_latex_mathjax(
        "y'=" + xu_ly_chuoi.tao_chuoi_latex(dao_ham_cap_1)))
    loi_giai.append(buoc_1)

    buoc_2 = list()
    buoc_2.append("Để hàm số đồng biến trên D thì " +
                  xu_ly_chuoi.boc_latex_mathjax(
                      "y'\geqslant0,\\forall " + xu_ly_chuoi.tao_chuoi_latex(bien) + " \in D"))
    loi_giai.append(buoc_2)


    return loi_giai


if __name__ == '__main__':
    import tao_loi_giai
    import sympy

    hs = sympy.sympify("x^2-m")
    b = sympy.Symbol('x')
    tao_loi_giai.xuat_html(tim_tham_so_de_ham_so_dong_bien_tren_tap_xac_dinh(
        hs, b), "loi_giai.html")
