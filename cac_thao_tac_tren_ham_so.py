from sympy import simplify, solve, diff, denom, limit, oo

# Rut gon ham so
def rut_gon(ham_so):
    return simplify(ham_so)


# Tim nghiem thuc cua ham so
def tim_nghiem_thuc(ham_so, bien):

    # Nghiem bao gom ca phuc va thuc
    nghiem = solve(ham_so, bien)

    # loc ra cac nghiem thuc
    nghiem_thuc = []
    for i in nghiem:
        if i.is_real:
            nghiem_thuc.append(i)
    return nghiem_thuc

# Dao ham cap 1
def tinh_dao_ham_cap_1(ham_so,bien):
    return diff(ham_so,bien)

# Dao ham cap 2
def tinh_dao_ham_cap_2(ham_so,bien):
    return diff(diff(ham_so,bien),bien)


def lay_mau_so(ham_so):
    return denom(ham_so)


def tim_gioi_han_tai_vo_cuc(ham_so, bien):
    am_vo_cuc = limit(ham_so, bien, -oo)
    duong_vo_cuc = limit(ham_so, bien, oo)
    return (am_vo_cuc, duong_vo_cuc)

def tim_gioi_han_hai_phia(ham_so,bien,diem):
    gioi_han_trai = limit(ham_so, bien, diem, '-')
    gioi_han_phai = limit(ham_so, bien, diem, '+')
    return gioi_han_trai,gioi_han_phai


# Thu nghiem
if __name__ == '__main__':
    x = Symbol('x')
    t = sympify("x^4 - 2*(x^2)-3")
    kq = rut_gon(t)
    print(kq)
