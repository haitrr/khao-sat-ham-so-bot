import sympy

x,m = sympy.symbols('x m')
bt=[]
bt.append(sympy.Eq(m,x))
bt.append(sympy.Eq(m,m,evalue=False))
print(sympy.latex(bt))