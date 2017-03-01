import sympy

# Rut gon ham so
def rut_gon(ham_so):
    return sympy.simplify(ham_so)


# Tim nghiem thuc cua ham so
def tim_nghiem_thuc(ham_so, bien):

    # Nghiem bao gom ca phuc va thuc
    nghiem = sympy.solve(ham_so, bien)

    # loc ra cac nghiem thuc
    nghiem_thuc = []
    for i in nghiem:
        if i.is_real:
            if str(i).find("CRootOf") != -1:
                nghiem_thuc.append(sympy.N(i))
            nghiem_thuc.append(i)
    return nghiem_thuc


def lay_mau_so(ham_so):
    return sympy.denom(ham_so)


ham_da_thuc = ["ham_bac_ba", "ham_bac_bon"]


def loai_ham_so(ham_so, bien):

    # Dang thu , chua biet
    if sympy.denom(ham_so) !=1:
        return "ham_phan_thuc"
    return "ham_bac_ba"


def gop_da_thuc(da_thuc,bien):
    return sympy.collect(da_thuc,bien)


def the_bien(bieu_thuc,bien,gia_tri):
    with sympy.evaluate(False):
        bieu_thuc = bieu_thuc.replace(bien, gia_tri)
    return bieu_thuc

def phan_tich_thanh_nhan_tu(bieu_thuc):
    return sympy.factor(bieu_thuc)


def lay_he_so(da_thuc,bien,so_mu):
    return da_thuc.coeff(bien,so_mu)

def nhan_vao(da_thuc):
    return sympy.expand(da_thuc)

# Thu nghiem
if __name__ == '__main__':
    x = sympy.Symbol('x')
    t = sympy.sympify("x^4 - 2*(x^2)-3+m^2-2*m")
