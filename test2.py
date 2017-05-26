import sympy
from latex2sympy.process_latex import process_sympy
import phuong_trinh
import re
import xu_ly_chuoi

pt = xu_ly_chuoi.chuyen_latex_thanh_sympy("\\log_2\\left(4\\cdot x\\right)-\\log_{\\frac{x}{2}}")
print(pt)
