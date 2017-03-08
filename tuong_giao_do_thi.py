import phuong_trinh as pt
import dao_ham as dh
import xu_ly_chuoi as xlc
import bat_dang_thuc as bdt
import phuong_trinh_bac_2
import huong_dan_giai as hdg
import hang_so
import tap_hop


def tim_toa_do_giao_diem_voi_duong_thang(ham_so, bien, duong_thang, bien_dt):
    loi_giai = hdg.LoiGiai('Tìm tọa độ giao điểm của đồ thị hàm số {0} với đường thẳng {1}'.format(
        xlc.boc_mathjax("f({0})={1}".format(xlc.tao_latex(bien), xlc.tao_latex(ham_so))),
        xlc.boc_mathjax("f({0})={1}".format(xlc.tao_latex(bien_dt), xlc.tao_latex(duong_thang)))))
    # Thay nghiem cua duong thang bang nghiem cua ham so
    duong_thang=pt.the_bien(duong_thang,bien_dt,bien)

    # Buoc 1 lap phuong trinh hoanh do giao diem
    buoc_1= hdg.LoiGiai("Lập phương trình hoành độ giao điểm")
    buoc_1.them_thao_tac("Ta có phương trình hoành độ giao điểm :")

    pt_hoanh_do_giao_diem = bdt.bang(ham_so,duong_thang)

    # In ra pt hoanh do giao diem
    buoc_1.them_thao_tac(xlc.boc_mathjax(xlc.tao_latex(pt_hoanh_do_giao_diem)))

    buoc_1.dap_an=pt_hoanh_do_giao_diem
    loi_giai.them_thao_tac(buoc_1)
    # Buoc 2: Giai pt hoanh do giao diem tim nghiem
    buoc_2 = hdg.LoiGiai("Tìm nghiệm của phương trình hoành độ giao điểm")

    # In ra pt hoanh do giao diem
    buoc_2.them_thao_tac(xlc.boc_mathjax(xlc.tao_latex(pt_hoanh_do_giao_diem)))

    # Chuyển vế phải sang vế trái
    pt_hoanh_do_giao_diem=bdt.bang(pt_hoanh_do_giao_diem.lhs-pt_hoanh_do_giao_diem.rhs,0)

    # In ra pt hoanh do giao diem sau khi chuyen ve
    buoc_2.them_thao_tac(xlc.boc_mathjax(hang_so.DAU_TUONG_DUONG+xlc.tao_latex(pt_hoanh_do_giao_diem)))

    # Rut gon pt hoanh do giao diem
    pt_hoanh_do_giao_diem=pt.phan_tich_thanh_nhan_tu(pt_hoanh_do_giao_diem)

    # In ra pt hoanh do giao diem
    buoc_2.them_thao_tac(xlc.boc_mathjax(hang_so.DAU_TUONG_DUONG+xlc.tao_latex(pt_hoanh_do_giao_diem)))


    # Giai phuong trinh
    nghiem = pt.tim_nghiem_thuc(pt_hoanh_do_giao_diem,bien)
    if len(nghiem)==0:
        buoc_2.them_thao_tac("Phương trình vô nghiệm")
    elif len(nghiem)==1:
        buoc_2.them_thao_tac(xlc.boc_mathjax(hang_so.DAU_TUONG_DUONG+xlc.tao_latex(bdt.bang(bien,nghiem[0]))))
    else:
        buoc_2.them_thao_tac(
            xlc.boc_mathjax(hang_so.DAU_TUONG_DUONG + "{0}={1}".format(xlc.tao_latex(bien),xlc.tao_latex(nghiem))))

    # Luu dap an
    buoc_2.dap_an=nghiem
    loi_giai.them_thao_tac(buoc_2)

    # Buoc 3 tu cac nghiem xac dinh giao diem
    buoc_3 = hdg.LoiGiai("Từ các nghiệm xác định tọa độ các giao điểm")

    # Giai thich
    buoc_3.them_thao_tac("Từ các nghiệm của phương trình hoành độ giao điểm ta xác định giao điểm ({0},{1})".format(xlc.boc_mathjax(xlc.tao_latex(bien)),xlc.boc_mathjax("f({0})".format(xlc.tao_latex(bien)))))

    # In ra cac diem
    cac_diem = [(hoanh,ham_so.subs(bien,hoanh)) for hoanh in nghiem]
    buoc_3.them_thao_tac(xlc.boc_mathjax(xlc.tao_ngoac_nhon(cac_diem)))

    loi_giai.them_thao_tac(buoc_3)
    return loi_giai

def tim_tham_so_de_ham_so_cat_truc_hoanh_tai_1_diem_duy_nhat(ham_so, bien, tham_so):
    # Tao loi giai
    loi_giai = hdg.LoiGiai("Tim {0} để đồ thị hàm số {1} cắt trục hoành tại một điểm duy nhất".format(
        xlc.boc_mathjax(xlc.tao_latex(tham_so)),
        xlc.boc_mathjax("f({0})={1}".format(xlc.tao_latex(bien), xlc.tao_latex(ham_so)))))

    # Buoc 1: Tinh dao ham cua ham so
    buoc_1 = hdg.LoiGiai("Tính đạo hàm của hàm số")

    dao_ham_cap_1 = dh.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_1.them_thao_tac(xlc.boc_mathjax(
        "f'({0})=".format(xlc.tao_latex(bien)) + xlc.tao_latex(dao_ham_cap_1)))

    buoc_1.dap_an = dao_ham_cap_1
    loi_giai.them_thao_tac(buoc_1)

    # Buoc 2
    buoc_2 = phuong_trinh_bac_2.tim_tham_so_de_phuong_trinh_co_nghiem_kep_hoac_vo_nghiem(buoc_1.dap_an, bien, tham_so)
    buoc_2.ten_loi_giai = "Xét trường hợp 1: Hàm số không có cực trị hay " + xlc.boc_mathjax(
        "f'({0})=0".format(xlc.tao_latex(bien))) + " có nghiệm kép hoặc vô nghiệm"

    loi_giai.them_thao_tac(buoc_2)

    # Buoc 3
    # Truong hop 2
    buoc_3 = hdg.LoiGiai("Xét trường hợp 2: Hàm số có hai cực trị ở cùng phía của trục hoành")

    # Buoc 3.1 tim tham so de f'(x)=0 co hai nghiem phan biet
    buoc_3_1 = phuong_trinh_bac_2.tim_tham_so_de_phuong_trinh_hai_nghiem_phan_biet(buoc_1.dap_an, bien, tham_so)
    buoc_3_1.ten_loi_giai = "Tìm {0} để {1} có hai nghiệm phân biệt".format(xlc.boc_mathjax(xlc.tao_latex(tham_so)),
                                                                            xlc.boc_mathjax("f'({0})=0".format(
                                                                                xlc.tao_latex(bien))))

    # Them buoc 3.1 vao buoc 3
    buoc_3.them_thao_tac(buoc_3_1)
    # Buoc 3.2 hai nghiem nam o hai phia cua truc hoanh
    nghiem_1, nghiem_2 = sympy.symbols(str(bien) + '_1 ' + str(bien) + '_2')

    buoc_3_2 = hdg.LoiGiai("Tìm nghiệm của bất đẳng thức {0}".format(
        xlc.boc_mathjax("f({0})*f({1})>0".format(xlc.tao_latex(nghiem_1), xlc.tao_latex(nghiem_2)))))

    # In ra dieu kien
    xlc.boc_mathjax("f({0})*f({1})>0".format(xlc.tao_latex(nghiem_1), xlc.tao_latex(nghiem_2)))

    # Thay cac nghiem vao
    f_nghiem_1 = pt.the_bien(ham_so, bien, nghiem_1)
    f_nghiem_2 = pt.the_bien(ham_so, bien, nghiem_2)

    dieu_kien = bdt.lon_hon(f_nghiem_1 * f_nghiem_2, 0)

    # In ra dieu kien sau khi thay nghiem
    buoc_3_2.them_thao_tac(xlc.boc_mathjax(hang_so.DAU_TUONG_DUONG + xlc.tao_latex(dieu_kien)))

    # Thay bien vao
    dieu_kien = pt.the_bien(dieu_kien, nghiem_1, buoc_3_1.cac_buoc_giai[2].dap_an[0])
    dieu_kien = pt.the_bien(dieu_kien, nghiem_2, buoc_3_1.cac_buoc_giai[2].dap_an[1])

    # In ra dieu kien sau khi thay bien
    buoc_3_2.them_thao_tac(xlc.boc_mathjax(hang_so.DAU_TUONG_DUONG + xlc.tao_latex(dieu_kien)))

    # Rut gon
    dieu_kien = pt.phan_tich_thanh_nhan_tu(dieu_kien)

    # In ra
    buoc_3_2.them_thao_tac(xlc.boc_mathjax(hang_so.DAU_TUONG_DUONG + xlc.tao_latex(dieu_kien)))

    # Giải set
    nghiem = bdt.giai_bat_dang_thuc_set(dieu_kien, tham_so)

    buoc_3_2.them_thao_tac("Giải hệ bất đẳng thức ta được {0}".format(
        xlc.boc_mathjax("{0} \in {1}".format(xlc.tao_latex(tham_so), xlc.tao_latex(nghiem)))))

    buoc_3_2.dap_an = nghiem
    buoc_3.them_thao_tac(buoc_3_2)

    # Buoc 3.3 tong hop ket qua
    buoc_3_3 = hdg.LoiGiai("Tổng hợp kết quả của hai bước trước")

    # Tong hop ket qua
    tong_hop_nghiem_buoc_3 = tap_hop.tim_giao(buoc_3_2.dap_an, buoc_3_1.dap_an)

    # In ra
    buoc_3_3.them_thao_tac("Tổng hợp kết quả của hai bước trước ta được {0}".format(
        xlc.boc_mathjax("{0} \in {1}".format(xlc.tao_latex(tham_so), xlc.tao_latex(tong_hop_nghiem_buoc_3)))))

    # Luu dap an
    buoc_3_3.dap_an = tong_hop_nghiem_buoc_3
    buoc_3.dap_an = tong_hop_nghiem_buoc_3

    # Them buoc 3.3 vao buoc 3
    buoc_3.them_thao_tac(buoc_3_3)

    # Them buoc 3 vao loi giai
    loi_giai.them_thao_tac(buoc_3)

    # Buoc 4 tong hop ket qua cua buoc 2 va buoc 3
    buoc_4 = hdg.LoiGiai("Tổng hợp kết quả của hai trường hợp")
    tong_hop = tap_hop.tim_hop(buoc_2.dap_an, buoc_3.dap_an)

    # In ra kq
    buoc_4.them_thao_tac("Tổng hợp kết quả của hai trường hợp ta được {0}".format(
        xlc.boc_mathjax("{0} \in {1}".format(xlc.tao_latex(tham_so), xlc.tao_latex(tong_hop)))))

    # Luu ket qua
    buoc_4.dap_an = tong_hop

    # Them buoc 4 vao loi giai
    loi_giai.dap_an = tong_hop
    loi_giai.them_thao_tac(buoc_4)
    return loi_giai


if __name__ == "__main__":
    import tao_loi_giai
    import sympy

    hs = sympy.sympify("x^3 -3*x**2+2")
    d = sympy.sympify("2-2*x")
    b = sympy.Symbol('x')
    tham_so = sympy.Symbol('m')
    tim_toa_do_giao_diem_voi_duong_thang(
        hs, b,d,b).xuat_html("loi_giai.html")
