import sympy

def boc_latex_mathjax(chuoi_latex):
    return "\(" + chuoi_latex + "\)"

def boc_latex_mpl(bieu_thuc):
    return "$" + sympy.latex(bieu_thuc) + "$"

def tao_chuoi_latex(bieu_thuc):
    return sympy.latex(bieu_thuc)

def tao_ngoac_nhon_latex(cac_bieu_thuc):
    ngoac_nhon = "\\begin{cases}"
    for bieu_thuc in cac_bieu_thuc:
        ngoac_nhon += sympy.latex(bieu_thuc) + " \\"+"\\ "
    ngoac_nhon += "\\end{cases}"
    return ngoac_nhon
