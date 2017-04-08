import sympy
from latex2sympy.process_latex import process_sympy
import phuong_trinh

sympy.init_printing(order='old',use_latex='mathjax')
x=sympy.Symbol('x')
m=sympy.Symbol('m')
hs = x**3-2*x**2-x+1
k = 3*x**2-4*x-1
print((hs/k))