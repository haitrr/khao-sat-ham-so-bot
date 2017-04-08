import sympy
import phuong_trinh
import huong_dan_giai
import xu_ly_chuoi
import hang_so


# Dao ham cap 1
def tinh_dao_ham_cap_1(ham_so, bien):
    ham_f = phuong_trinh.tao_ham('f',ham_so,bien)
    loi_giai = huong_dan_giai.LoiGiai("Tính đạo hàm của hàm số {ham_so}".format(ham_so=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_f))))
    dao_ham = sympy.diff(ham_so, bien)
    dao_ham_f = phuong_trinh.tao_ham("f'",dao_ham,bien)
    loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax("{dao_ham}=({ham})'".format(dao_ham=dao_ham_f.lhs,ham=xu_ly_chuoi.tao_latex(ham_so))))
    loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG+xu_ly_chuoi.tao_latex(dao_ham_f)))
    loi_giai.dap_an=dao_ham
    return loi_giai

def tinh_dao_ham_cap_2(dao_ham_cap_1, bien):
    ham_f = phuong_trinh.tao_ham('f',dao_ham_cap_1,bien)
    loi_giai = huong_dan_giai.LoiGiai("Tính đạo hàm của hàm số {ham_so}".format(ham_so=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_f))))
    dao_ham = sympy.diff(dao_ham_cap_1, bien)
    dao_ham_f = phuong_trinh.tao_ham("f''",dao_ham,bien)
    loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax("{dao_ham}=({ham})'".format(dao_ham=dao_ham_f.lhs,ham=xu_ly_chuoi.tao_latex(dao_ham_cap_1))))
    loi_giai.them_thao_tac(xu_ly_chuoi.boc_mathjax(hang_so.DAU_TUONG_DUONG+xu_ly_chuoi.tao_latex(dao_ham_f)))
    loi_giai.dap_an=dao_ham
    return loi_giai