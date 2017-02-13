import sympy

class ham_so:
    def __init__(ham):
        self.ham = ham
        self.dao_ham_cap_1 = sympy.diff(ham)
        self.dao_ham_cap_2 = sympy.diff(self.dao_ham_cap_2)
