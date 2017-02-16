import sympy
# Dao ham cap 1


def tinh_dao_ham_cap_1(ham_so, bien):
    return sympy.diff(ham_so, bien)

# Dao ham cap 2


def tinh_dao_ham_cap_2(ham_so, bien):
    return sympy.diff(tinh_dao_ham_cap_1(ham_so, bien), bien)
