import dao_ham
import tinh_xac_dinh
import xu_ly_chuoi
import bat_dang_thuc
import phuong_trinh
import sympy
import phuong_trinh_bac_2


def tim_tham_so_de_ham_so_dong_bien_tren_tap_xac_dinh(ham_so, bien):
    loi_giai = list()

    loi_giai.append("Tập xác định của hàm số")
    tap_xac_dinh = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien)
    loi_giai.append(xu_ly_chuoi.boc_mathjax("D=" + xu_ly_chuoi.tao_latex(tap_xac_dinh)))


    dao_ham_cap_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    loi_giai.append("Đạo hàm của hàm số")
    loi_giai.append(xu_ly_chuoi.boc_mathjax(
        "f'(x)=" + xu_ly_chuoi.tao_latex(dao_ham_cap_1)))
    dao_ham_cap_1_rut_gon = phuong_trinh.rut_gon(dao_ham_cap_1)
    if dao_ham_cap_1_rut_gon!=dao_ham_cap_1:
        loi_giai.append(
            xu_ly_chuoi.boc_mathjax("\Leftrightarrow " + xu_ly_chuoi.tao_latex(dao_ham_cap_1)))


    loi_giai.append("Để hàm số đồng biến trên D thì " +
                    xu_ly_chuoi.boc_mathjax(
                      "f'(x)\geq0,\\forall " + xu_ly_chuoi.tao_latex(bien) + " \in D"))
    loi_giai+=phuong_trinh_bac_2.tim_tham_so_de_ham_so_lon_hon_hoac_bang_0(dao_ham_cap_1_rut_gon,bien)
    return loi_giai

def tim_tham_so_de_ham_so_nghich_bien_tren_tap_xac_dinh(ham_so, bien):
    loi_giai = list()

    loi_giai.append("Tập xác định của hàm số")
    tap_xac_dinh = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien)
    loi_giai.append(xu_ly_chuoi.boc_mathjax("D=" + xu_ly_chuoi.tao_latex(tap_xac_dinh)))


    dao_ham_cap_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    loi_giai.append("Đạo hàm của hàm số")
    loi_giai.append(xu_ly_chuoi.boc_mathjax(
        "f'(x)=" + xu_ly_chuoi.tao_latex(dao_ham_cap_1)))
    dao_ham_cap_1_rut_gon = phuong_trinh.rut_gon(dao_ham_cap_1)
    if dao_ham_cap_1_rut_gon!=dao_ham_cap_1:
        loi_giai.append(
            xu_ly_chuoi.boc_mathjax("\Leftrightarrow " + xu_ly_chuoi.tao_latex(dao_ham_cap_1)))


    loi_giai.append("Để hàm số nghịch biến trên D thì " +
                    xu_ly_chuoi.boc_mathjax(
                      "f'(x)\leq0,\\forall " + xu_ly_chuoi.tao_latex(bien) + " \in D"))
    loi_giai+=phuong_trinh_bac_2.tim_tham_so_de_ham_so_nho_hon_hoac_bang_0(dao_ham_cap_1_rut_gon,bien)
    return loi_giai

if __name__ == '__main__':
    import tao_loi_giai
    import sympy

    hs = sympy.sympify("x^3+(m-1)*x^2+(m^2-4)*x+9")
    b = sympy.Symbol('x')
    tao_loi_giai.xuat_html(tim_tham_so_de_ham_so_dong_bien_tren_tap_xac_dinh(
        hs, b), "loi_giai.html")
