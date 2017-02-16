def xuat_html(loi_giai, file):
    file_loi_giai = open(file, "w", encoding='utf8')
    file_loi_giai.write("<!doctype html><html><head><meta charset=\"UTF-8\"><title>Lời giải của bài toán</title><script type=\"text/javascript\" src=\"http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML\"></script></head><body>")
    for buoc in range(len(loi_giai)):
        file_loi_giai.write("<b>Bước " + str(buoc + 1) +
                            ":</b>" + loi_giai[buoc][0] + "<br>")
        for thao_tac in range(1, len(loi_giai[buoc])):
            file_loi_giai.write(loi_giai[buoc][thao_tac] + "<br>")
    file_loi_giai.write("</body></html>")


import time
import sympy
from khao_sat_ham_so import *
x = sympy.Symbol('x')
t = sympy.sympify("-2*x^4 +4*(x^2)+6")
#t = sympy.sympify("(1)/(x^2-2)")
n = time.time()
loi_giai = khao_sat_ham_so(t, x)
print(time.time() - n)
n = time.time()
loi_giai = khao_sat_ham_so(t, x)
print(time.time() - n)
xuat_html(loi_giai, "loi_giai.html")
