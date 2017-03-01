import phuong_trinh
import dao_ham
import xu_ly_chuoi
import bat_dang_thuc
import phuong_trinh_bac_2


def tim_tham_so_de_ham_so_cat_truc_hoanh_tai_1_diem_duy_nhat(ham_so, bien):
    # Lay tham so
    cac_bien = list(ham_so.free_symbols)
    cac_bien.remove(bien)
    tham_so = cac_bien[0]

    loi_giai = list()

    # Buoc 1: Tinh dao ham cua ham so
    loi_giai.append("Tính đạo hàm của hàm số")
    dao_ham_cap_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(
        "f'({0})=".format(xu_ly_chuoi.tao_latex(bien)) + xu_ly_chuoi.tao_latex(dao_ham_cap_1)))

    # Buoc 2
    # Truong hop 1
    loi_giai.append(
        "Trường hợp 1: Hàm số không có cực trị hay " + xu_ly_chuoi.boc_mathjax(
            "f'({0})=0".format(xu_ly_chuoi.tao_latex(bien))) + " vô nghiệm")
    loi_giai += phuong_trinh_bac_2.tim_tham_so_de_phuong_trinh_co_nghiem_kep_hoac_vo_nghiem(dao_ham_cap_1, bien)

    # Truong hop 2
    loi_giai.append(
        "Trường hợp 2: Hàm số có hai cực trị ở cùng phía của trục hoành")

    # Co hai nghiem phan biet
    loi_giai.append("Để hàm số có hai cực trị " + xu_ly_chuoi.boc_mathjax(
        "f'({0})=0".format(xu_ly_chuoi.tao_latex(bien))) + " có hai nghiệm phân biệt")

    loi_giai_2_nghiem_pb, nghiem = tim_tham_so_de_ham_so_cat_truc_hoanh_tai_1_diem_duy_nhat(dao_ham_cap_1, bien)
    loi_giai += loi_giai_2_nghiem_pb

    # Hai nghiem phai cung dau
    loi_giai.append("Để hai cực trị nằm ở hai phía của trục hoành " + xu_ly_chuoi.boc_mathjax(
        "f({0})f({1})>0".format(xu_ly_chuoi.tao_latex(bat_dang_thuc.lay_ve_trai(nghiem[0])),
                                xu_ly_chuoi.tao_latex(bat_dang_thuc.lay_ve_trai(nghiem[1])))))
    nghiem[0] = bat_dang_thuc.lay_ve_phai(nghiem[0])
    nghiem[1] = bat_dang_thuc.lay_ve_phai(nghiem[1])

    # The 2 nghiem vao
    dieu_kien = bat_dang_thuc.lon_hon(
        phuong_trinh.the_bien(ham_so, bien, nghiem[0]) * phuong_trinh.the_bien(ham_so, bien, nghiem[1]), 0)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)))

    # Rut gon
    dieu_kien = phuong_trinh.phan_tich_thanh_nhan_tu(dieu_kien)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)))

    # Giai thuong
    dieu_kien_temp = bat_dang_thuc.giai_bat_dang_thuc(dieu_kien, tham_so)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien_temp)))

    # Giải set
    dieu_kien = bat_dang_thuc.giai_bat_dang_thuc_set(dieu_kien, tham_so)
    loi_giai.append(xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(dieu_kien)))

    return loi_giai


if __name__ == "__main__":
    import tao_loi_giai
    import sympy

    hs = sympy.sympify("x^3 +m*x+2")
    b = sympy.Symbol('x')
    tao_loi_giai.xuat_html(tim_tham_so_de_ham_so_cat_truc_hoanh_tai_1_diem_duy_nhat(
        hs, b), "loi_giai.html")
