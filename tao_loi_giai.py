from khao_sat_ham_so import *
from io import StringIO

def xuat_html(loi_giai, file=None):

    # Moi file hoac tao file khi chua co 
    # Phai dung utf-8 hien thi tieng viet


    output= StringIO()
    # Header cua file phai import mathjax de hien thi bieu thuc
    output.write("<!doctype html><html><head><meta charset=\"UTF-8\"><title>Lời giải của bài toán</title><script type=\"text/javascript\" src=\"http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML\"></script></head><body>")

    # In moi buoc giai ra
    for buoc in range(len(loi_giai)):

        # Ten buoc
        output.write("<b>Bước " + str(buoc + 1) +
                            ":</b>" + loi_giai[buoc][0] + "<br>")
        # In ra cac thao tac
        for thao_tac in range(1, len(loi_giai[buoc])):
            output.write(loi_giai[buoc][thao_tac] + "<br>")

    # Dong the
    output.write("</body></html>")
    if file:
        file_loi_giai_html = open(file, "w", encoding='utf8')
        file_loi_giai_html.write(output.getvalue())
    loi_giai_html = output.getvalue()
    # Dong file
    output.close()
    return loi_giai_html


if __name__ == 'main':
    import time
    import sympy
    x = sympy.Symbol('x')
    t = sympy.sympify("-2*x^4 +4*(x^2)+6")
    #t = sympy.sympify("(x^2 + x-2)/(x+3)")
    #t = sympy.sympify("(1)/(x^2-2)")
    n = time.time()
    loi_giai = khao_sat_ham_so(t, x)
    print(time.time() - n)
    n = time.time()
    loi_giai = khao_sat_ham_so(t, x)
    print(time.time() - n)
    xuat_html(loi_giai, "loi_giai.html")
