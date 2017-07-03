"""
Cac dang toan ve gia tri lon nhat va nho nhat cua ham so
"""

import huong_dan_giai
import xu_ly_chuoi
import phuong_trinh
import dao_ham
import tinh_xac_dinh
import gioi_han
import cuc_tri
import bang_bien_thien


def tim_gia_tri_lon_nhat_va_nho_nhat_cua_ham_so(ham_so, bien):
    """
    Tim gia tri lon nhat va nho nhat cua ham so
    :param ham_so: 
    :param bien: 
    :return: 
    """
    ham_so_f = phuong_trinh.tao_ham('f', ham_so, bien)
    loi_giai = huong_dan_giai.LoiGiai(
        "Tìm giá trị lớn nhất và nhỏ nhất của hàm số {hs}".format(
            hs=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_so_f))))
    # -----------------Cau hoi -----------
    ch_1 = huong_dan_giai.HoiDap(
        "Muốn biết giá trị lớn nhất, nhở nhất của hàm số bạn cần làm gì?")
    da_1 = huong_dan_giai.DapAnCauHoi("Lập bảng biên thiên",
                                      ["bang bien thien"])

    ch_1.dap_an.append(da_1)
    loi_giai.cac_cau_hoi.append(ch_1)

    # --------------------Bai giai ---------------------
    # Buoc 1: Tim tap xac dinh
    buoc_1 = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien)
    buoc_1.ten_loi_giai = 'Tìm tập xác định'

    # Buoc 2: Tim đạo hàm của hàm số
    buoc_2 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_2.ten_loi_giai = 'Tìm đạo hàm của hàm số'

    # Buoc 3 : Tim nghiem cua dao ham
    buoc_3 = phuong_trinh.giai_phuong_trinh(buoc_2.dap_an, bien)
    buoc_3.ten_loi_giai = 'Tìm nghiệm của đạo hàm'

    # 1 nghiem
    lon_nhat = [-9999, None]
    nho_nhat = [9999, None]
    if len(buoc_3.dap_an) == 1:
        # B4: Ve bang bien thien
        buoc_4 = bang_bien_thien.lap_bang_bien_thien(ham_so, bien)
        buoc_4.ten_loi_giai = 'Lập bảng biến thiên của hàm số'
        cd = cuc_tri.tim_diem_cuc_dai(ham_so, bien)
        if cd:
            lon_nhat[1] = [buoc_3.dap_an[0]]
            lon_nhat[0] = cd[0][1]
        ct = cuc_tri.tim_diem_cuc_tieu(ham_so, bien)
        if ct:
            nho_nhat[1] = [buoc_3.dap_an[0]]
            nho_nhat[0] = ct[0][1]
    else:
        # B4: Tim gia tri cua ham so tai cac nghiem tim duoc
        buoc_4 = huong_dan_giai.LoiGiai(
            'Tìm giá trị hàm số tại các nghiệm tìm được')
        buoc_4.dap_an = list()
        for nghiem in buoc_3.dap_an:
            thay = phuong_trinh.thay_bien(ham_so, bien, nghiem)
            buoc_4.cac_buoc_giai += thay.cac_buoc_giai
            buoc_4.dap_an.append(thay.dap_an)
            if thay.dap_an > lon_nhat[0]:
                lon_nhat = [thay.dap_an, [nghiem]]
                continue
            if thay.dap_an < nho_nhat[0]:
                nho_nhat = [thay.dap_an, [nghiem]]
                continue
            if thay.dap_an == lon_nhat[0]:
                lon_nhat[1].append(nghiem)
            if thay.dap_an == nho_nhat[0]:
                nho_nhat[1].append(nghiem)
    # B5: Ket luan
    buoc_5 = huong_dan_giai.LoiGiai('Kết luận')
    buoc_5.them_thao_tac('Vậy ta có:')
    if nho_nhat[1] is None:
        buoc_5.them_thao_tac('Hàm số không có giá trị nhỏ nhất')
    else:
        t1 = [phuong_trinh.tao_ten_ham('f', b) for b in nho_nhat[1]]
        t2 = ""
        for t in t1:
            t2 += xu_ly_chuoi.tao_latex(t) + ' = '
        t2 += xu_ly_chuoi.tao_latex(nho_nhat[0])
        buoc_5.them_thao_tac('Giá trị nhỏ nhất của hàm số là {nn}'.format(
            nn=xu_ly_chuoi.boc_mathjax('min\ {f} = {gt}'.format(
                f=xu_ly_chuoi.tao_latex(phuong_trinh.tao_ten_ham('f', bien)),
                gt=t2))))
    if lon_nhat[1] is None:
        buoc_5.them_thao_tac('Hàm số không có giá trị lớn nhất')
    else:
        t1 = [phuong_trinh.tao_ten_ham('f', b) for b in lon_nhat[1]]
        t2 = ""
        for t in t1:
            t2 += xu_ly_chuoi.tao_latex(t) + ' = '
        t2 += xu_ly_chuoi.tao_latex(lon_nhat[0])
        buoc_5.them_thao_tac('Giá trị lớn nhất của hàm số là {nn}'.format(
            nn=xu_ly_chuoi.boc_mathjax('max\ {f} = {gt}'.format(
                f=xu_ly_chuoi.tao_latex(phuong_trinh.tao_ten_ham('f', bien)),
                gt=t2))))

    loi_giai.them_thao_tac(buoc_1)
    loi_giai.them_thao_tac(buoc_2)
    loi_giai.them_thao_tac(buoc_3)
    loi_giai.them_thao_tac(buoc_4)
    loi_giai.them_thao_tac(buoc_5)
    return loi_giai


def tim_gia_tri_lon_nhat_va_nho_nhat_cua_ham_so_trong_mot_khoang_cho_truoc(
        ham_so, bien, khoang):
    """
    Tim gia tri lon nhat va nho nhat cua ham so tren mot khoang/doan cho truoc
    :param ham_so: 
    :param bien: 
    :param khoang: 
    :return: 
    """
    ham_so_f = phuong_trinh.tao_ham('f', ham_so, bien)
    loi_giai = huong_dan_giai.LoiGiai(
        "Tìm giá trị lớn nhất và nhỏ nhất của hàm số {hs}".format(
            hs=xu_ly_chuoi.boc_mathjax(xu_ly_chuoi.tao_latex(ham_so_f))))

    # Buoc 1: Tim tap xac dinh
    buoc_1 = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien)
    buoc_1.ten_loi_giai = 'Tìm tập xác định'

    # Buoc 2: Tim đạo hàm của hàm số
    buoc_2 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    buoc_2.ten_loi_giai = 'Tìm đạo hàm của hàm số'

    # Buoc 3 : Tim nghiem cua dao ham
    buoc_3 = phuong_trinh.giai_phuong_trinh(buoc_2.dap_an, bien)
    buoc_3.ten_loi_giai = 'Tìm nghiệm của đạo hàm'

    # B4 Ve bang bien thien
    buoc_4 = bang_bien_thien.lap_bang_bien_thien(ham_so, bien, khoang)

    # Kiem tra cac nghiem cua dao ham nam trong khoang
    nghiem_trong_khoang = list()
    for nghiem in buoc_3.dap_an:
        if khoang.contains(nghiem):
            nghiem_trong_khoang.append(nghiem)

    # Xet xem khoang co dau bi chan nao khong
    if not khoang.right_open:
        nghiem_trong_khoang.append(khoang.right)
    if not khoang.left_open:
        nghiem_trong_khoang.append(khoang.left)

    lon_nhat = [-9999, None]
    nho_nhat = [9999, None]

    # Tim gia tri lon nhat,nho nhat
    for nghiem in nghiem_trong_khoang:
        thay = phuong_trinh.thay_bien(ham_so, bien, nghiem)
        if thay.dap_an > lon_nhat[0]:
            lon_nhat = [thay.dap_an, [nghiem]]
            continue
        if thay.dap_an < nho_nhat[0]:
            nho_nhat = [thay.dap_an, [nghiem]]
            continue
        if thay.dap_an == lon_nhat[0]:
            lon_nhat[1].append(nghiem)
        if thay.dap_an == nho_nhat[0]:
            nho_nhat[1].append(nghiem)
    # B5: Ket luan
    buoc_5 = huong_dan_giai.LoiGiai('Kết luận')
    buoc_5.them_thao_tac('Vậy ta có:')
    if nho_nhat[1] is None:
        buoc_5.them_thao_tac('Hàm số không có giá trị nhỏ nhất')
    else:
        t1 = [phuong_trinh.tao_ten_ham('f', b) for b in nho_nhat[1]]
        t2 = ""
        for t in t1:
            t2 += xu_ly_chuoi.tao_latex(t) + ' = '
        t2 += xu_ly_chuoi.tao_latex(nho_nhat[0])
        buoc_5.them_thao_tac('Giá trị nhỏ nhất của hàm số là {nn}'.format(
            nn=xu_ly_chuoi.boc_mathjax('min\ {f} = {gt}'.format(
                f=xu_ly_chuoi.tao_latex(phuong_trinh.tao_ten_ham('f', bien)),
                gt=t2))))
    if lon_nhat[1] is None:
        buoc_5.them_thao_tac('Hàm số không có giá trị lớn nhất')
    else:
        t1 = [phuong_trinh.tao_ten_ham('f', b) for b in lon_nhat[1]]
        t2 = ""
        for t in t1:
            t2 += xu_ly_chuoi.tao_latex(t) + ' = '
        t2 += xu_ly_chuoi.tao_latex(lon_nhat[0])
        buoc_5.them_thao_tac('Giá trị lớn nhất của hàm số là {nn}'.format(
            nn=xu_ly_chuoi.boc_mathjax('max\ {f} = {gt}'.format(
                f=xu_ly_chuoi.tao_latex(phuong_trinh.tao_ten_ham('f', bien)),
                gt=t2))))

    loi_giai.them_thao_tac(buoc_1)
    loi_giai.them_thao_tac(buoc_2)
    loi_giai.them_thao_tac(buoc_3)
    loi_giai.them_thao_tac(buoc_4)
    loi_giai.them_thao_tac(buoc_5)
    return loi_giai


# Thu nghiem
if __name__ == "__main__":
    import sympy

    x = sympy.Symbol('x')
    m = sympy.Symbol('m')

    def tim_gia_tri_lon_nhat_va_nho_nhat_cua_ham_so_test():
        #hs = x**4+2*x**2-1
        #hs = x**3-3*x**2+1
        hs = 4 / (1 + x**2)
        tim_gia_tri_lon_nhat_va_nho_nhat_cua_ham_so(
            hs, x).xuat_html("loi_giai.html")

    def tim_gia_tri_lon_nhat_va_nho_nhat_cua_ham_so_trong_khoang_cho_truoc_test(
    ):
        hs = (2 * x**2 + 3 * x + 3) / (x + 1)
        k = sympy.Interval(0, 2)
        tim_gia_tri_lon_nhat_va_nho_nhat_cua_ham_so_trong_mot_khoang_cho_truoc(
            hs, x, k).xuat_html("loi_giai.html")

    tim_gia_tri_lon_nhat_va_nho_nhat_cua_ham_so_trong_khoang_cho_truoc_test()