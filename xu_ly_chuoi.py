import sympy
from latex2sympy.process_latex import process_sympy
import re
import hang_so


def boc_mathjax(chuoi_latex):
    return "\(" + chuoi_latex + "\)"


def boc_mpl(bieu_thuc):
    return "$" + sympy.latex(bieu_thuc) + "$"


def tao_latex(bieu_thuc):
    return sympy.latex(bieu_thuc)


def tao_ngoac_nhon(cac_bieu_thuc):
    if len(cac_bieu_thuc)==1:
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
    kq = tin_nhan.lower()
    for mau, thay in mau_thay.items():
        kq = re.sub(mau, thay, kq)
        # deal with upper case
        kq = re.sub(mau.upper(), thay, kq)
    return kq


def chuyen_latex_thanh_sympy(bieu_thuc):
    return sympy.sympify(process_sympy(bieu_thuc))

def tao_anh_html(file_tam):
    """
    Tao mot doan ma html de hien thi mot file anh trong thu muc tam
    :param file_tam: string
    :return: string
    """
    return "<img src=\"{0}\">".format(hang_so.THU_MUC_TAM + file_tam)