import sympy
from matplotlib import pyplot
import matplotlib as mpl
from dao_ham import *
from tap_xac_dinh import *
from xu_ly_chuoi import *
from gioi_han import *


def ve_bang_bien_thien(ham_so, bien, ten_file):
    # Tinh toan cac gia tri can thiet
    dao_ham_cap_1 = sympy.simplify(sympy.diff(ham_so, bien))
    nghiem_dao_ham_cap_1 = tim_nghiem_thuc(dao_ham_cap_1, bien)
    dao_ham_cap_1_kxd = khong_xac_dinh(dao_ham_cap_1, bien)
    ham_so_kxd = khong_xac_dinh(ham_so, bien)
    cac_gia_tri_can_dien_vao_x = list(
        set(nghiem_dao_ham_cap_1 + dao_ham_cap_1_kxd + ham_so_kxd))
    cac_gia_tri_can_dien_vao_x.sort()
    cac_gia_tri_can_dien_vao_x = [-sympy.oo] + \
        cac_gia_tri_can_dien_vao_x + [sympy.oo]

    # Tinh chinh bang
    mpl.rc("text", usetex=True)
    fig = pyplot.figure()
    bang_bien_thien = fig.add_subplot(111)
    bang_bien_thien.xaxis.set_visible(False)
    bang_bien_thien.yaxis.set_visible(False)
    co_font = 20
    chieu_rong_cot_ngan = co_font * 2
    chieu_rong_bang = 800
    chieu_cao_bang = 200
    pyplot.gca().set_aspect('equal', adjustable='box')

    # Ve khung cua bang bien thien
    bang_bien_thien.plot([0, chieu_rong_bang], [
                         chieu_cao_bang / 5 * 4, chieu_cao_bang / 5 * 4], 'k-', lw=2)
    bang_bien_thien.plot([0, chieu_rong_bang], [
                         chieu_cao_bang / 5 * 3, chieu_cao_bang / 5 * 3], 'k-', lw=2)
    bang_bien_thien.plot([chieu_rong_cot_ngan, chieu_rong_cot_ngan], [
                         0, chieu_cao_bang], 'k-', lw=2)
    mpl.rcParams.update(
        {'font.size': co_font * (fig.get_size_inches()[1] * fig.dpi) / chieu_rong_bang})
    bang_bien_thien.text(chieu_rong_cot_ngan / 2, chieu_cao_bang / 5 * 4.5,
                         r"$x$", verticalalignment='center', horizontalalignment='center')
    bang_bien_thien.text(chieu_rong_cot_ngan / 2, chieu_cao_bang /
                         5 * 3.5, r"$y'$", verticalalignment='center', horizontalalignment='center')
    bang_bien_thien.text(chieu_rong_cot_ngan / 2, chieu_cao_bang /
                         5 * 1.5, r"$y$", verticalalignment='center', horizontalalignment='center')

    # Tinh khoang cach giua cac gia tri
    phong_hai_dau = co_font * 2
    khoang_cach = int((chieu_rong_bang - chieu_rong_cot_ngan -
                       phong_hai_dau * 2) / (len(cac_gia_tri_can_dien_vao_x) - 1))

    # Dien vao hang x va hang y'
    for i in range(len(cac_gia_tri_can_dien_vao_x)):
        bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i, chieu_cao_bang / 5 * 4.5,
                             boc_latex_mpl(cac_gia_tri_can_dien_vao_x[i]), verticalalignment='center', horizontalalignment='center')
        if i != 0 and i != len(cac_gia_tri_can_dien_vao_x) - 1:
            if cac_gia_tri_can_dien_vao_x[i] in dao_ham_cap_1_kxd:
                bang_bien_thien.plot([chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i - 2, chieu_rong_cot_ngan + phong_hai_dau +
                                      khoang_cach * i - 2], [chieu_cao_bang / 5 * 4, chieu_cao_bang / 5 * 3])
                bang_bien_thien.plot([chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i + 2, chieu_rong_cot_ngan + phong_hai_dau +
                                      khoang_cach * i + 2], [chieu_cao_bang / 5 * 4, chieu_cao_bang / 5 * 3])
            else:
                bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i, chieu_cao_bang /
                                     5 * 3.5, boc_latex_mpl("0"), verticalalignment='center', horizontalalignment='center')

    # Gioi han cua ham so tai vo cuc
    gioi_han_vo_cuc = tim_gioi_han_tai_vo_cuc(ham_so, bien)
    # Cac gia tri cua y can dien vao bang
    gia_tri_ham_so = []
    for gia_tri in cac_gia_tri_can_dien_vao_x:

        # Neu ham so khong xac dinh thi tim gioi han hai phia
        if gia_tri in ham_so_kxd:
            gia_tri_ham_so.append(tim_gioi_han_hai_phia(ham_so, bien, gia_tri))

        # Neu khong thi tim gia tri
        else:
            if gia_tri == -sympy.oo:
                gia_tri_ham_so.append(gioi_han_vo_cuc[0])
            elif gia_tri == sympy.oo:
                gia_tri_ham_so.append(gioi_han_vo_cuc[1])
            else:
                gia_tri_ham_so.append(ham_so.subs(bien, gia_tri))

    cac_dau_can_dien = []
    for i in range(len(gia_tri_ham_so) - 1):
        kq = ""
        if isinstance(gia_tri_ham_so[i], tuple):
            gia_tri = gia_tri_ham_so[i][1]
            kq += "s"
        else:
            gia_tri = gia_tri_ham_so[i]
        if isinstance(gia_tri_ham_so[i + 1], tuple):
            gia_tri_so_sanh = gia_tri_ham_so[i + 1][0]
            kq += "e"
        else:
            gia_tri_so_sanh = gia_tri_ham_so[i + 1]
        if gia_tri < gia_tri_so_sanh:
            cac_dau_can_dien.append(kq + "+")
        else:
            cac_dau_can_dien.append(kq + "-")

    phong_kxd = co_font * 1.5
    # Dien vao dong y
    for i in range(len(cac_dau_can_dien)):
        if cac_dau_can_dien[i][-1] == '+':
            if 's' in cac_dau_can_dien[i]:
                bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i + phong_kxd, chieu_cao_bang /
                                     5 * 0.5, boc_latex_mpl(gia_tri_ham_so[i][1]), verticalalignment='center', horizontalalignment='center')
            else:
                bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i, chieu_cao_bang / 5 *
                                     0.5, boc_latex_mpl(gia_tri_ham_so[i]), verticalalignment='center', horizontalalignment='center')
            if 'e' in cac_dau_can_dien[i]:
                bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * (i + 1) - phong_kxd, chieu_cao_bang /
                                     5 * 2.5, boc_latex_mpl(gia_tri_ham_so[i + 1][0]), verticalalignment='center', horizontalalignment='center')
        else:
            if 's' in cac_dau_can_dien[i]:
                bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i + phong_kxd, chieu_cao_bang /
                                     5 * 2.5, boc_latex_mpl(gia_tri_ham_so[i][1]), verticalalignment='center', horizontalalignment='center')
            else:
                bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i, chieu_cao_bang / 5 *
                                     2.5, boc_latex_mpl(gia_tri_ham_so[i]), verticalalignment='center', horizontalalignment='center')
            if 'e' in cac_dau_can_dien[i]:
                bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * (i + 1) - phong_kxd, chieu_cao_bang /
                                     5 * 0.5, boc_latex_mpl(gia_tri_ham_so[i + 1][0]), verticalalignment='center', horizontalalignment='center')

    # Dien cac dau + va - vao dong y'
    for i in range(len(cac_dau_can_dien)):
        if cac_dau_can_dien[i][-1] == '+':
            bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * (i + 0.5), chieu_cao_bang /
                                 5 * 3.5, boc_latex_mpl("+"), verticalalignment='center', horizontalalignment='center')
        else:
            bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * (i + 0.5), chieu_cao_bang /
                                 5 * 3.5, boc_latex_mpl("-"), verticalalignment='center', horizontalalignment='center')

    # Ve cac mui ten len xuong
    cong_them = phong_kxd

    for i in range(len(cac_dau_can_dien)):
        vi_tri = i
        while(vi_tri != len(cac_dau_can_dien)-1 and cac_dau_can_dien[vi_tri][-1]==cac_dau_can_dien[vi_tri+1][-1]):
            if 's' in cac_dau_can_dien[vi_tri+1]:
                break
            else:
                vi_tri=vi_tri+1
        if 's' in cac_dau_can_dien[i]:
            x1 = chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i + phong_kxd * 2
            bang_bien_thien.plot([chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i - 2, chieu_rong_cot_ngan + phong_hai_dau +
                                  khoang_cach * i - 2], [chieu_cao_bang / 5 * 3, 0])
            bang_bien_thien.plot([chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i + 2, chieu_rong_cot_ngan + phong_hai_dau +
                                  khoang_cach * i + 2], [chieu_cao_bang / 5 * 3, 0])
        else:
            x1 = chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * i + phong_kxd
        if 'e' in cac_dau_can_dien[vi_tri]:
            x2 = chieu_rong_cot_ngan + phong_hai_dau + \
                khoang_cach * (vi_tri + 1) - phong_kxd * 2
        else:
            x2 = chieu_rong_cot_ngan + phong_hai_dau + \
                khoang_cach * (vi_tri + 1) - phong_kxd
        if cac_dau_can_dien[i][-1] == '+':
            bang_bien_thien.arrow(x1, chieu_cao_bang / 5, x2 - x1, chieu_cao_bang /
                                  5, head_width=co_font / 3, head_length=co_font / 2)
        else:
            bang_bien_thien.arrow(x1, chieu_cao_bang / 5 * 2, x2 - x1, -
                                  chieu_cao_bang / 5, head_width=co_font / 3, head_length=co_font / 2)

    # Dien gia tri y cuoi cung ( gia tri cua y o duong vo cung)
    if cac_dau_can_dien[-1][-1] == '-':
        bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * (len(cac_gia_tri_can_dien_vao_x) - 1),
                             chieu_cao_bang / 5 * 0.5, boc_latex_mpl(gia_tri_ham_so[-1]), verticalalignment='center', horizontalalignment='center')
    else:
        bang_bien_thien.text(chieu_rong_cot_ngan + phong_hai_dau + khoang_cach * (len(cac_gia_tri_can_dien_vao_x) - 1),
                             chieu_cao_bang / 5 * 2.5, boc_latex_mpl(gia_tri_ham_so[-1]), verticalalignment='center', horizontalalignment='center')
    fig.savefig(ten_file, bbox_inches='tight', pad_inches=0.0)
    pyplot.close(fig)
