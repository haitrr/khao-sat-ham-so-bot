import re

import regex
import sympy

import hang_so
from latex2sympy.process_latex import process_sympy


def boc_mathjax(chuoi_latex):
    return "\(" + chuoi_latex + "\)"


def boc_mpl(bieu_thuc):
    return "$" + sympy.latex(bieu_thuc) + "$"


def tao_latex(bieu_thuc):
    sympy.init_printing(order='old')
    return sympy.latex(bieu_thuc)


def tao_ngoac_nhon(cac_bieu_thuc):
    if len(cac_bieu_thuc) == 1:
        return sympy.latex(cac_bieu_thuc[0])
    ngoac_nhon = "\\begin{cases}"
    for bieu_thuc in cac_bieu_thuc:
        ngoac_nhon += sympy.latex(bieu_thuc) + " \\" + "\\ "
    ngoac_nhon += "\\end{cases}"
    return ngoac_nhon


mau_thay = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y'
}


def chuyen_thanh_khong_dau_thuong(tin_nhan):
    # todo tao doc
    if tin_nhan == "R":
        return tin_nhan
    kq = tin_nhan.lower()
    for mau, thay in mau_thay.items():
        kq = re.sub(mau, thay, kq)
        # deal with upper case
        kq = re.sub(mau.upper(), thay, kq)
    return kq


def chuyen_latex_thanh_sympy(bieu_thuc):
    # todo: tao doc
    if bieu_thuc == 'R':
        return sympy.S.Reals
    try:
        return xet_tap_hop(bieu_thuc)
    except:
        pass
    try:
        return xet_nhieu_bieu_thuc(bieu_thuc)
    except:
        pass
    while "\\left" in bieu_thuc:
        bieu_thuc = bieu_thuc.replace("\\left", "")
    while "\\right" in bieu_thuc:
        bieu_thuc = bieu_thuc.replace("\\right", "")
    return sympy.sympify(process_sympy(bieu_thuc))


def latex_thanh_sympy(bieu_thuc):
    # todo tao doc
    return sympy.sympify(process_sympy(bieu_thuc))


def tao_anh_html(file_tam):
    """
    Tao mot doan ma html de hien thi mot file anh trong thu muc tam
    :param file_tam: string
    :return: string
    """
    return "<img src=\"{0}\">".format(hang_so.THU_MUC_TAM + file_tam)


KHOP_TAP_BIEU_THUC = r'^\s?(?:([^;]+)\s?(?:\;\s?([^;]+)\s?)+)\s?$'
KHOP_TAP_HOP = r'^(?:(?:\s?\\left(\(|\))\s?([^,]+)\,\s?(.*?)\\right(\)|\])\s?(?:(\\cup|\\cap)\s?\\left(\(|\))\s?([^,]+)\,\s?(.*?)\\right(\)|\])\s?)*)|(\s?\\varnothing\s?))$'


def xet_tap_hop(tin_nhan):
    # todo tao doc
    khop = regex.match(KHOP_TAP_HOP, tin_nhan)
    if khop:
        if khop.groups()[-1] is not None:
            return sympy.EmptySet()
        else:
            tap_hop = tao_tap_hop(khop.groups()[0:4])
            if khop.groups()[4] is not None:
                toan_tu = khop.captures(5)
                du_lieu = list(
                    zip(
                        khop.captures(6),
                        khop.captures(7), khop.captures(8), khop.captures(9)))
                for i in range(len(toan_tu)):
                    # todo sua code cung
                    if toan_tu[i] == '\cup':
                        tap_hop = tap_hop.union(tao_tap_hop(du_lieu[i]))
                    else:
                        tap_hop = tap_hop.intersect(tao_tap_hop(du_lieu[i]))
            return tap_hop

    raise ValueError


def tao_du_lieu_hop_chon(tap_lua_chon, tua_de):
    # todo tao doc
    du_lieu = 'mo_hop_chon{' + tua_de + "}{"
    for lua_chon in tap_lua_chon:
        if isinstance(lua_chon, list):
            du_lieu += "(" + lua_chon[0] + "::"
            for lc in lua_chon[1:]:
                du_lieu += lc + "::"
            du_lieu = du_lieu[:-2] + ');'
        else:
            du_lieu += lua_chon + ';'
    du_lieu = du_lieu[:-1] + '}'
    return du_lieu


def tao_tap_hop(du_lieu):
    # todo tao doc
    trai = True
    phai = True
    if du_lieu[0] == '[':
        trai = False
    try:
        bat_dau = latex_thanh_sympy(du_lieu[1])
        ket_thuc = latex_thanh_sympy(du_lieu[2])
    except:
        raise ValueError
    if du_lieu[3] == ']':
        phai = False
    tap_hop = sympy.Interval(bat_dau, ket_thuc, trai, phai)
    return tap_hop


def xet_nhieu_bieu_thuc(tin_nhan):
    # todo tao doc
    khop = regex.match(KHOP_TAP_BIEU_THUC, tin_nhan)
    if khop:
        du_lieu = khop.captures(2)
        cac_bieu_thuc = list()
        cac_bieu_thuc.append(latex_thanh_sympy(khop.groups()[0]))
        for bt in du_lieu:
            cac_bieu_thuc.append(latex_thanh_sympy(bt))
        return cac_bieu_thuc
    else:
        raise ValueError


def tao_cau_lenh_cap_nhat_loi_giai(loi_giai):
    # todo tao doc
    # todo code cung , can sua lai duoi dang su dung hang so
    return "cap_nhat_loi_giai:::{lg}".format(lg=loi_giai)


if __name__ == '__main__':
    t = xet_tap_hop(
        '\left(2,3\\right)\cup\left(3,4\\right)\cup\left(8,16\\right)')
    print(xet_nhieu_bieu_thuc('1;2;3;-2'))
