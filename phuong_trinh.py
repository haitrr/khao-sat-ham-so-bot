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


# Thu nghiem
if __name__ == '__main__':
    x = sympy.Symbol('x')
    t = sympy.sympify("x^4 - 2*(x^2)-3")
    kq = rut_gon(t)
    print(kq)