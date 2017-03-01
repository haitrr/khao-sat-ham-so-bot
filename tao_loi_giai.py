import io


def xuat_html(loi_giai, file=None):
    """
    Xuat loi giai ra dang html de hien thi tren web
    :param loi_giai: list
    :param file: string
    :return: string
    """

    # Moi file hoac tao file khi chua co

    output = io.StringIO()
    # In ra de bai
    output.write(loi_giai[0])

    # In moi buoc giai ra
    for buoc in range(1,len(loi_giai)):
        # In ra ten buoc
        output.write("<b>Bước {0} : {1}<b><br>".format(buoc,loi_giai[buoc][0]))

        # In ra cac thao tac
        for thao_tac in loi_giai[buoc][1:-1]:
            if isinstance(thao_tac,list):
                output.write(xuat_html(thao_tac)+"<br>")
            else:
                output.write(thao_tac+"<br>")


    if file:
        # Moi file hoac tao file khi chua co
        # Phai dung utf-8 hien thi tieng viet
        file_loi_giai_html = open(file, "w", encoding='utf8')
        # Header cua file phai import mathjax de hien thi bieu thuc
        file_loi_giai_html.write(
            "<!doctype html><html><head><meta charset=\"UTF-8\"><title>Lời giải của bài toán</title><script type=\"text/javascript\" src=\"http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML\"></script></head><body>")
        # Dong the
        file_loi_giai_html.write(output.getvalue())
        file_loi_giai_html.write("</body></html>")
    loi_giai_html = output.getvalue()
    # Dong file
    output.close()
    return loi_giai_html


if __name__ == '__main__':
    import time
    import sympy
    import khao_sat_ham_so
    x = sympy.Symbol('x')
    t = sympy.sympify("-2*x^4 +4*(x^2)+6")
    #t = sympy.sympify("(x^2 + x-2)/(x+3)")
    #t = sympy.sympify("(1)/(x^2-2)")
    n = time.time()
    loi_giai = khao_sat_ham_so.khao_sat_ham_so(t, x)
    print(time.time() - n)
    n = time.time()
    loi_giai = khao_sat_ham_so.khao_sat_ham_so(t, x)
    print(time.time() - n)
    xuat_html(loi_giai, "loi_giai.html")
