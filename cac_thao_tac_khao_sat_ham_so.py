import sympy as sp
import matplotlib as mpl
from PIL import Image, ImageDraw, ImageFont
from matplotlib import pyplot
import numpy as np
from cac_thao_tac_tren_ham_so import *
from bat_dang_thuc import *
import io
from xu_ly_anh import *

ham_da_thuc = ["ham_bac_ba", "ham_bac_bon"]


def loai_ham_so(ham_so, bien):

    # Dang thu , chua biet
    return "ham_phan_thuc"
    return "ham_bac_ba"


def khong_xac_dinh(ham_so, bien):

    # Ham da thuc,xac dinh tren R
    if loai_ham_so(ham_so, bien) in ham_da_thuc:
        return []

    # Ham phan thuc khong xac dinh khi mau bang 0
    else:
        if loai_ham_so(ham_so, bien) == "ham_phan_thuc":
            mau_so = lay_mau_so(ham_so)
            return tim_nghiem_thuc(mau_so, bien)
    pass


def tap_xac_dinh(ham_so, bien):
    loai_ham = loai_ham_so(ham_so, bien)

    # Ham da thuc tap xac dinh la R
    if loai_ham in ham_da_thuc:
        return sp.S.Reals

    # Ham phan thuc mau khong xac dinh
    elif loai_ham == "ham_phan_thuc":
        dieu_kien = []
        mau_so = lay_mau_so(ham_so)
        khong_xac_dinh = tim_nghiem_thuc(mau_so, bien)
        for i in khong_xac_dinh:
            dieu_kien.append(sp.Unequality(bien, i))
        tap_xac_dinh = giai_he_bat_dang_thuc(dieu_kien, bien)
        return tap_xac_dinh
    else:
        return "Loi"


def diem_cuc_dai(ham_so, bien):
    dao_ham_cap_1 = sp.diff(ham_so, bien)
    dao_ham_cap_2 = sp.diff(dao_ham_cap_1, bien)
    nghiem_dao_ham_cap_1 = tim_nghiem_thuc(dao_ham_cap_1, bien)
    txd = tap_xac_dinh(ham_so, bien)
    nghiem_cuc_dai = []
    for nghiem in nghiem_dao_ham_cap_1:
        if txd.contains(nghiem) is False:
            continue
        else:
            if dao_ham_cap_2.subs(bien, nghiem) < 0:
                nghiem_cuc_dai.append(nghiem)
    dcd = []
    for nghiem in nghiem_cuc_dai:
        dcd.append((nghiem, ham_so.subs(bien, nghiem)))
    return dcd


def diem_cuc_tieu(ham_so, bien):
    dao_ham_cap_1 = sp.diff(ham_so, bien)
    dao_ham_cap_2 = sp.diff(dao_ham_cap_1, bien)
    nghiem_dao_ham_cap_1 = tim_nghiem_thuc(dao_ham_cap_1, bien)
    txd = tap_xac_dinh(ham_so, bien)
    nghiem_cuc_tieu = []
    for nghiem in nghiem_dao_ham_cap_1:
        if txd.contains(nghiem) is False:
            continue
        else:
            if dao_ham_cap_2.subs(bien, nghiem) > 0:
                nghiem_cuc_tieu.append(nghiem)
    dct = []
    for nghiem in nghiem_cuc_tieu:
        dct.append((nghiem, ham_so.subs(bien, nghiem)))
    return dct


def diem_cuc_tri(ham_so, bien):
    return((diem_cuc_dai(ham_so, bien), diem_cuc_tieu(ham_so, bien)))


def diem_uon(ham_so, bien):
    dao_ham_cap_1 = sp.diff(ham_so, bien)
    dao_ham_cap_2 = sp.diff(dao_ham_cap_1, bien)
    nghiem_dao_ham_cap_2 = tim_nghiem_thuc(dao_ham_cap_2, bien)
    txd = tap_xac_dinh(ham_so, bien)
    nghiem_diem_uon = []
    for nghiem in nghiem_dao_ham_cap_2:
        if txd.contains(nghiem) is False:
            continue
        else:
            nghiem_diem_uon.append(nghiem)
    du = []
    for nghiem in nghiem_diem_uon:
        du.append((nghiem, ham_so.subs(bien, nghiem)))
    return du


def ve_bang_bien_thien(ham_so, bien,ten_file):
    dao_ham_cap_1 = sp.diff(ham_so, bien)
    nghiem_dao_ham_cap_1 = tim_nghiem_thuc(dao_ham_cap_1, bien)
    dao_ham_cap_1_kxd = khong_xac_dinh(dao_ham_cap_1, bien)
    ham_so_kxd = khong_xac_dinh(ham_so, bien)
    cac_gia_tri_can_dien_vao_x = list(
        set(nghiem_dao_ham_cap_1 + dao_ham_cap_1_kxd + ham_so_kxd))
    cac_gia_tri_can_dien_vao_x.sort()
    cac_gia_tri_can_dien_vao_x = [-sp.oo] + \
        cac_gia_tri_can_dien_vao_x + [sp.oo]

    # Ve khung cua bang bien thien
    co_font = 20
    chieu_rong_cot_ngan = co_font * 2
    chieu_rong_bang = 600
    chieu_cao_bang = 200
    mau_but = 0

    fnt = ImageFont.truetype("./arial.ttf", co_font)
    bang_bien_thien = Image.new(
        "RGB", (chieu_rong_bang, chieu_cao_bang), "white")
    draw = ImageDraw.Draw(bang_bien_thien)
    draw.line((0, chieu_cao_bang / 5, chieu_rong_bang -
               1, chieu_cao_bang / 5), fill=mau_but)
    draw.line((0, chieu_cao_bang / 5 * 2, chieu_rong_bang -
               1, chieu_cao_bang / 5 * 2), fill=mau_but)
    draw.line((chieu_rong_cot_ngan, 0, chieu_rong_cot_ngan,
               chieu_cao_bang - 1), fill=mau_but)
    draw.text((co_font / 2, co_font / 2), 'x', fill=mau_but, font=fnt)
    draw.text((co_font / 2, co_font / 2 + chieu_cao_bang / 5),
              'y', fill=mau_but, font=fnt)
    draw.text((co_font / 2, co_font / 2 + chieu_cao_bang / 5 * 4),
              "y'", fill=mau_but, font=fnt)
    khoang_cach = int((chieu_rong_bang - chieu_rong_cot_ngan -
                       co_font) / (len(cac_gia_tri_can_dien_vao_x) - 1))

    # Dien vao hang x va hang y'
    for i in range(len(cac_gia_tri_can_dien_vao_x)):
        anh_cua_bieu_thuc = ve_bieu_thuc_toan_ra_anh(
            cac_gia_tri_can_dien_vao_x[i])
        bang_bien_thien.paste(anh_cua_bieu_thuc, (int(
            chieu_rong_cot_ngan + khoang_cach * i), int(co_font / 2)))
        if i != 0 and i != len(cac_gia_tri_can_dien_vao_x) - 1:
            if cac_gia_tri_can_dien_vao_x[i] in dao_ham_cap_1_kxd:
                draw.line((chieu_rong_cot_ngan + khoang_cach * i - 2, chieu_cao_bang / 5, chieu_rong_cot_ngan +
                           khoang_cach * i - 2, chieu_cao_bang / 5 * 2), fill=mau_but)
                draw.line((chieu_rong_cot_ngan + khoang_cach * i + 2, chieu_cao_bang / 5, chieu_rong_cot_ngan +
                           khoang_cach * i + 2, chieu_cao_bang / 5 * 2), fill=mau_but)
            else:
                draw.text((chieu_rong_cot_ngan + khoang_cach * i, co_font / 2 + chieu_cao_bang / 5),
                          str(0), fill=mau_but, font=fnt)


    # Gioi han cua ham so tai vo cuc 
    gioi_han_vo_cuc = tim_gioi_han_tai_vo_cuc(ham_so,bien)
    # Cac gia tri cua y can dien vao bang
    gia_tri_ham_so = []
    for gia_tri in cac_gia_tri_can_dien_vao_x:

        # Neu ham so khong xac dinh thi tim gioi han hai phia
        if gia_tri in ham_so_kxd:
            gia_tri_ham_so.append(tim_gioi_han_hai_phia(ham_so, bien, gia_tri))

        # Neu khong thi tim gia tri
        else:
            if gia_tri == -sp.oo:
                gia_tri_ham_so.append(gioi_han_vo_cuc[0])
            elif gia_tri == sp.oo:
                gia_tri_ham_so.append(gioi_han_vo_cuc[1])
            else:
                gia_tri_ham_so.append(ham_so.subs(bien, gia_tri))

    # Dien vao dong y
    for i in range(len(gia_tri_ham_so) - 1):
        if isinstance(gia_tri_ham_so[i], tuple):
            if isinstance(gia_tri_ham_so[i - 1], tuple):
                gia_tri_so_sanh = gia_tri_ham_so[i - 1][1]
            else:
                gia_tri_so_sanh = gia_tri_ham_so[i - 1]
            if gia_tri_ham_so[i][0] > gia_tri_so_sanh:
                bang_bien_thien.paste(ve_bieu_thuc_toan_ra_anh(gia_tri_ham_so[i][0]), (int(
                    chieu_rong_cot_ngan + khoang_cach * i - co_font * 1.5), int(co_font / 2 + chieu_cao_bang / 5 * 2)))
            else:
                bang_bien_thien.paste(ve_bieu_thuc_toan_ra_anh(gia_tri_ham_so[i][0]), (int(
                    chieu_rong_cot_ngan + khoang_cach * i - co_font * 1.5), int(co_font / 2 + chieu_cao_bang / 5 * 4)))
            if isinstance(gia_tri_ham_so[i + 1], tuple):
                gia_tri_so_sanh = gia_tri_ham_so[i + 1][0]
            else:
                gia_tri_so_sanh = gia_tri_ham_so[i + 1]
            if gia_tri_ham_so[i][1] > gia_tri_so_sanh:
                bang_bien_thien.paste(ve_bieu_thuc_toan_ra_anh(gia_tri_ham_so[i][1]), (int(
                    chieu_rong_cot_ngan + khoang_cach * i + co_font / 2), int(co_font / 2 + chieu_cao_bang / 5 * 2)))
            else:
                bang_bien_thien.paste(ve_bieu_thuc_toan_ra_anh(gia_tri_ham_so[i][1]), (int(
                    chieu_rong_cot_ngan + khoang_cach * i + co_font / 2), int(co_font / 2 + chieu_cao_bang / 5 * 4)))
        else:
            if isinstance(gia_tri_ham_so[i + 1], tuple):
                gia_tri_so_sanh = gia_tri_ham_so[i + 1][0]
            else:
                gia_tri_so_sanh = gia_tri_ham_so[i + 1]
            if gia_tri_ham_so[i] < gia_tri_so_sanh:
                bang_bien_thien.paste(ve_bieu_thuc_toan_ra_anh(gia_tri_ham_so[i]), (int(
                    chieu_rong_cot_ngan + khoang_cach * i), int(co_font / 2 + chieu_cao_bang / 5 * 4)))
            else:
                bang_bien_thien.paste(ve_bieu_thuc_toan_ra_anh(gia_tri_ham_so[i]), (int(
                    chieu_rong_cot_ngan + khoang_cach * i), int(co_font / 2 + chieu_cao_bang / 5 * 2)))

    # Dien cac dau + va - vao dong y'
    for i in range(len(gia_tri_ham_so) - 1):
        if isinstance(gia_tri_ham_so[i], tuple):
            gia_tri = gia_tri_ham_so[i][1]
        else:
            gia_tri = gia_tri_ham_so[i]
        if isinstance(gia_tri_ham_so[i + 1], tuple):
            gia_tri_so_sanh = gia_tri_ham_so[i + 1][0]
        else:
            gia_tri_so_sanh = gia_tri_ham_so[i + 1]

        if gia_tri < gia_tri_so_sanh:
            draw.text((chieu_rong_cot_ngan + khoang_cach * (i + 1 / 2), co_font / 2 + chieu_cao_bang / 5),
                      "+", fill=mau_but, font=fnt)
        else:
            draw.text((chieu_rong_cot_ngan + khoang_cach * (i + 1 / 2), co_font / 2 + chieu_cao_bang / 5),
                      "-", fill=mau_but, font=fnt)

    # Ve cac mui ten len xuong
    for i in range(len(gia_tri_ham_so) - 1):
        if isinstance(gia_tri_ham_so[i], tuple):
            gia_tri = gia_tri_ham_so[i][1]
            draw.line((chieu_rong_cot_ngan + khoang_cach * i - 2, chieu_cao_bang / 5 * 2, chieu_rong_cot_ngan +
                       khoang_cach * i - 2, chieu_cao_bang - 1), fill=mau_but)
            draw.line((chieu_rong_cot_ngan + khoang_cach * i + 2, chieu_cao_bang / 5 * 2, chieu_rong_cot_ngan +
                       khoang_cach * i + 2, chieu_cao_bang - 1), fill=mau_but)
        else:
            gia_tri = gia_tri_ham_so[i]
        if isinstance(gia_tri_ham_so[i + 1], tuple):
            gia_tri_so_sanh = gia_tri_ham_so[i + 1][0]
        else:
            gia_tri_so_sanh = gia_tri_ham_so[i + 1]
        if isinstance(gia_tri_ham_so[i], tuple):
            x1 = chieu_rong_cot_ngan + khoang_cach * i + co_font * 1.5
        else:
            x1 = chieu_rong_cot_ngan + khoang_cach * i + co_font

        if isinstance(gia_tri_ham_so[i + 1], tuple):
            x2 = chieu_rong_cot_ngan + khoang_cach * (i + 1) - co_font * 1.5
        else:
            x2 = chieu_rong_cot_ngan + khoang_cach * (i + 1)

        if gia_tri < gia_tri_so_sanh:
            draw.line((x1, co_font / 2 + chieu_cao_bang / 5 * 4, x2,
                       co_font / 2 + chieu_cao_bang / 5 * 2 + co_font), fill=mau_but)
        else:
            draw.line((x1, co_font / 2 + chieu_cao_bang / 5 * 2 + co_font,
                       x2, co_font / 2 + chieu_cao_bang / 5 * 4), fill=mau_but)

    # Dien gia tri y cuoi cung ( gia tri cua y o duong vo cung)
    if isinstance(gia_tri_ham_so[-2], tuple):
        gia_tri_so_sanh = gia_tri_ham_so[-2][1]
    else:
        gia_tri_so_sanh = gia_tri_ham_so[-2]
    if gia_tri_ham_so[-1] < gia_tri_so_sanh:
        bang_bien_thien.paste(ve_bieu_thuc_toan_ra_anh(gia_tri_ham_so[-1]), (int(
            chieu_rong_cot_ngan + khoang_cach * (len(cac_gia_tri_can_dien_vao_x) - 1)), int(co_font / 2 + chieu_cao_bang / 5 * 4)))
    else:
        bang_bien_thien.paste(ve_bieu_thuc_toan_ra_anh(gia_tri_ham_so[-1]), (int(
            chieu_rong_cot_ngan + khoang_cach * (len(cac_gia_tri_can_dien_vao_x) - 1)), int(co_font / 2 + chieu_cao_bang / 5 * 2)))
    bang_bien_thien.save(ten_file)


def giao_diem_voi_truc_hoanh(ham_so, bien):
    nghiem_giao_diem = tim_nghiem_thuc(ham_so, bien)
    giao_diem = []
    for nghiem in nghiem_giao_diem:
        if nghiem.is_infinite:
            continue
        giao_diem.append((nghiem, 0))
    return giao_diem


def giao_diem_voi_truc_tung(ham_so, bien):
    giao_diem = ham_so.subs(bien, 0)
    if giao_diem.is_infinite:
        return []
    return [(0, giao_diem)]


def ve_do_thi(ham_so, bien):
    dcd = diem_cuc_dai(ham_so, bien)
    dct = diem_cuc_tieu(ham_so, bien)
    du = diem_uon(ham_so, bien)
    gdth = giao_diem_voi_truc_hoanh(ham_so, bien)
    gdtt = giao_diem_voi_truc_tung(ham_so, bien)
    # print([dcd,dct,du,gdth,gdtt])
    cac_diem_can_ve_x = []
    cac_diem_can_ve_y = []
    cac_diem_can_ve = dcd + dct + du + gdth + gdtt
    # print(cac_diem_can_ve)
    # return
    cac_diem_can_ve = list(set(cac_diem_can_ve))
    for diem in cac_diem_can_ve:
        cac_diem_can_ve_x.append(diem[0])
        cac_diem_can_ve_y.append(diem[1])

    lam_x = sp.lambdify(bien, ham_so, ["numpy"])
    # x_vals = np.arange(min(cac_diem_can_ve_x)-5,
    # max(cac_diem_can_ve_y)+5,0.1)
    x_vals = np.linspace(np.float64(min(cac_diem_can_ve_x) - 3),
                         np.float64(max(cac_diem_can_ve_y) + 3), 100)
    y_vals = lam_x(x_vals)

    fig = pyplot.figure()

    do_thi = fig.add_subplot(111)
    do_thi.plot(x_vals, y_vals)
    # do_thi.tick_params(axis='x', labelsize=5)
    # do_thi.tick_params(axis='y', labelsize=5)

    if cac_diem_can_ve:
        do_thi.plot(cac_diem_can_ve_x, cac_diem_can_ve_y, "ro")
        for diem in cac_diem_can_ve:
            if diem[1] != 0 and diem[0] != 0:
                do_thi.plot((diem[0], diem[0]), (0, diem[1]), '--')
                do_thi.plot((diem[0], 0), (diem[1], diem[1]), '--')

# using 'spines', new in Matplotlib 1.0
    do_thi.spines['left'].set_position('zero')
    do_thi.spines['right'].set_color('none')
    do_thi.spines['bottom'].set_position('zero')
    do_thi.spines['top'].set_color('none')
    do_thi.spines['left'].set_smart_bounds(True)
    do_thi.spines['bottom'].set_smart_bounds(True)
    do_thi.xaxis.set_ticks_position('bottom')
    do_thi.yaxis.set_ticks_position('left')
    cac_diem_can_ve_x = list(set(cac_diem_can_ve_x))
    cac_diem_can_ve_y = list(set(cac_diem_can_ve_y))
    cac_diem_can_danh_dau_x = [
        "$" + str(sp.latex(i)) + "$" for i in cac_diem_can_ve_x]
    cac_diem_can_danh_dau_y = [
        "$" + str(sp.latex(i)) + "$" for i in cac_diem_can_ve_y]
    # pyplot.xticks(list(pyplot.xticks()[0]) + cac_diem_can_danh_dau_x)
    # pyplot.yticks(list(pyplot.yticks()[0]) + cac_diem_can_danh_dau_y)
    # pyplot.xticks(cac_diem_can_danh_dau_x)
    # pyplot.yticks(cac_diem_can_danh_dau_y)
    mpl.rc("text", usetex=True)
    pyplot.xticks(cac_diem_can_ve_x, cac_diem_can_danh_dau_x)
    pyplot.yticks(cac_diem_can_ve_y, cac_diem_can_danh_dau_y)
    # for gia_tri in cac_diem_can_ve_y:
    #    pyplot.yticks([float(gia_tri)], [str(gia_tri)])
    pyplot.ylim(np.float64(min(cac_diem_can_ve_y) - 3),
                np.float64(max(cac_diem_can_ve_y) + 3))
    # pyplot.ylim(- 10, 5)
    #pyplot.savefig("./a.png")
    #pyplot.show()
if __name__ == '__main__':
    x = sp.Symbol('x')
    t = sp.sympify("( 4) / ( x^2 - 2 )")
    # print(t.subs(x,5))
    # print(giao_diem_voi_truc_hoanh(t, x))
    # ve_do_thi(t, x)
    # print(sp.diff(sp.diff(t,x),x))
    #ve_do_thi(t, x)
    # print(tap_xac_dinh(t,x))
    # ve_bieu_thuc_toan_ra_anh(t)
    ve_bang_bien_thien(t,x)
    #ve_bang_bien_thien(t,x)
