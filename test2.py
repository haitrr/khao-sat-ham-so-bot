import sympy
from latex2sympy.process_latex import process_sympy
#import phuong_trinh
import re

sympy.init_printing(order='old',use_latex='mathjax')
x=sympy.Symbol('x')
m=sympy.Symbol('m')
print(sympy.latex((2*0**2+0*3+3)/1))
t = r"\b{tk}\b".format(tk="is")
print(re.search(t,'i l is'))