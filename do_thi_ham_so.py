import os
import tempfile
import matplotlib as mpl
import numpy
import sympy
from matplotlib import pyplot
import cuc_tri
import diem_uon
import giao_diem_voi_truc
import hang_so
import xu_ly_chuoi


def ve_do_thi(ham_so, bien):
    # Chinh co font cua chu trong do thi
    mpl.rcParams.update(
        {'font.size': 8})

    # Tim cac diem can thiet
    dcd = cuc_tri.tim_diem_cuc_dai(ham_so, bien)
    dct = cuc_tri.tim_diem_cuc_tieu(ham_so, bien)
    du = diem_uon.tim_diem_uon(ham_so, bien)
    gdth = giao_diem_voi_truc.giao_diem_voi_truc_hoanh(ham_so, bien)
    gdtt = giao_diem_voi_truc.giao_diem_voi_truc_tung(ham_so, bien)
    cac_diem_can_ve_x = []
    cac_diem_can_ve_y = []
    cac_diem_can_ve = dcd + dct + du + gdth + gdtt
    cac_diem_can_ve = list(set(cac_diem_can_ve))
    for diem in cac_diem_can_ve:
        cac_diem_can_ve_x.append(diem[0])
        cac_diem_can_ve_y.append(diem[1])

    # Tinh toan gioi han cua do thi
    gioi_han_x = [min(cac_diem_can_ve_x), max(cac_diem_can_ve_x)]
    gioi_han_y = [min(cac_diem_can_ve_y), max(cac_diem_can_ve_y)]

    gioi_han_x[0] -= abs(gioi_han_x[0])
    gioi_han_x[1] += abs(gioi_han_x[1])
    gioi_han_y[0] -= abs(gioi_han_y[0])
    gioi_han_y[1] += abs(gioi_han_y[1])

    if gioi_han_x[0] == 0:
        gioi_han_x[0] = -3
    if gioi_han_x[1] == 0:
        gioi_han_x[1] = 3
    if gioi_han_y[0] == 0:
        gioi_han_y[0] = -3
    if gioi_han_y[1] == 0:
        gioi_han_y[1] = 3

    # Ve do thi cua ham so
    lam_x = sympy.lambdify(bien, ham_so, ["numpy"])
    x_vals = numpy.linspace(float(gioi_han_x[0]),
                            float(gioi_han_x[1]), 500)
    y_vals = lam_x(x_vals)

    fig = pyplot.figure()

    do_thi = fig.add_subplot(111)
    do_thi.plot(x_vals, y_vals)

    # Danh dau cac diem dac biet tren do thi
    if cac_diem_can_ve:

        # Danh dau diem
        do_thi.plot(cac_diem_can_ve_x, cac_diem_can_ve_y, "ro")
        for diem in cac_diem_can_ve:
            if diem[1] != 0 and diem[0] != 0:
                # Ve duong tu hai truc den diem do
                do_thi.plot((diem[0], diem[0]), (0, diem[1]), '--')
                do_thi.plot((diem[0], 0), (diem[1], diem[1]), '--')

    # Dua 2 truc cat nhau o diem O(0,0)
    do_thi.spines['left'].set_position('zero')
    do_thi.spines['right'].set_color('none')
    do_thi.spines['bottom'].set_position('zero')
    do_thi.spines['top'].set_color('none')
    do_thi.xaxis.set_ticks_position('bottom')
    do_thi.yaxis.set_ticks_position('left')

    # Danh dau cac stick tren cac truc
    cac_diem_can_ve_x = list(set(cac_diem_can_ve_x))
    cac_diem_can_ve_y = list(set(cac_diem_can_ve_y))
    cac_diem_can_danh_dau_x = [
        xu_ly_chuoi.boc_mpl(i) for i in cac_diem_can_ve_x]
    cac_diem_can_danh_dau_y = [
        xu_ly_chuoi.boc_mpl(i) for i in cac_diem_can_ve_y]

    cac_diem_can_ve_x_float = [float(i) for i in cac_diem_can_ve_x]
    cac_diem_can_ve_y_float = [float(i) for i in cac_diem_can_ve_y]
    mpl.rc("text", usetex=True)
    pyplot.xticks(cac_diem_can_ve_x_float, cac_diem_can_danh_dau_x)
    pyplot.yticks(cac_diem_can_ve_y_float, cac_diem_can_danh_dau_y)

    pyplot.ylim(numpy.float64(gioi_han_y[0]),
                numpy.float64(gioi_han_y[1]))

    # Luu vao file tam
    file_tam = tempfile.NamedTemporaryFile(
        suffix=".png", prefix="dt", delete=False, dir=hang_so.THU_MUC_TAM)
    fig.savefig(file_tam, bbox_inches='tight', pad_inches=0.1, format='png')

    # Dong hinh lai
    pyplot.close(fig)

    # Tra ve ten file
    return os.path.basename(file_tam.name)


if __name__ == '__main__':
    x = sympy.Symbol('x')
    t = sympy.sympify("x^2 +2*x+5")
    print(ve_do_thi(t, x))
