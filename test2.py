import sympy
from latex2sympy.process_latex import process_sympy
import phuong_trinh

sympy.init_printing(order='old',use_latex='mathjax')
x=sympy.Symbol('x')
m=sympy.Symbol('m')

hs = -4*m*x +m
print(sympy.oo==sympy.oo)
print(hs.subs(m*x,m))
print(sympy.Interval(m,x,True))
print(phuong_trinh.so_sanh(sympy.oo,sympy.oo))