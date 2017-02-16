import sympy
from cuc_tri import *
from diem_uon import *
from giao_diem_voi_truc import *
from xu_ly_chuoi import *
from matplotlib import pyplot
import matplotlib as mpl
import numpy

def ve_do_thi(ham_so, bien,xuat_file):
    dcd = diem_cuc_dai(ham_so, bien)
    dct = diem_cuc_tieu(ham_so, bien)
    du = diem_uon(ham_so, bien)
    gdth = giao_diem_voi_truc_hoanh(ham_so, bien)
    gdtt = giao_diem_voi_truc_tung(ham_so, bien)
    # print([dcd,dct,du,gdth,gdtt])
    cac_diem_can_ve_x = []
    cac_diem_can_ve_y = []
    cac_diem_can_ve = dcd + dct + du + gdth + gdtt
    # print(cac_diem_can_ve)
    # return
    cac_diem_can_ve = list(set(cac_diem_can_ve))
    for diem in cac_diem_can_ve:
        cac_diem_can_ve_x.append(diem[0])
        cac_diem_can_ve_y.append(diem[1])

    lam_x = sympy.lambdify(bien, ham_so, ["numpy"])
    # x_vals = numpy.arange(min(cac_diem_can_ve_x)-5,
    # max(cac_diem_can_ve_y)+5,0.1)
    x_vals = numpy.linspace(numpy.float64(-abs(max(cac_diem_can_ve_x)) *2),
                         numpy.float64(abs(max(cac_diem_can_ve_x)) *2), 500)
    y_vals = lam_x(x_vals)

    fig = pyplot.figure()

    do_thi = fig.add_subplot(111)
    do_thi.plot(x_vals, y_vals)
    # do_thi.tick_params(axis='x', labelsize=5)
    # do_thi.tick_params(axis='y', labelsize=5)

    if cac_diem_can_ve:
        do_thi.plot(cac_diem_can_ve_x, cac_diem_can_ve_y, "ro")
        for diem in cac_diem_can_ve:
            if diem[1] != 0 and diem[0] != 0:
                do_thi.plot((diem[0], diem[0]), (0, diem[1]), '--')
                do_thi.plot((diem[0], 0), (diem[1], diem[1]), '--')

# using 'spines', new in Matplotlib 1.0
    do_thi.spines['left'].set_position('zero')
    do_thi.spines['right'].set_color('none')
    do_thi.spines['bottom'].set_position('zero')
    do_thi.spines['top'].set_color('none')
    #do_thi.spines['left'].set_smart_bounds(True)
    #do_thi.spines['bottom'].set_smart_bounds(True)
    do_thi.xaxis.set_ticks_position('bottom')
    do_thi.yaxis.set_ticks_position('left')
    cac_diem_can_ve_x = list(set(cac_diem_can_ve_x))
    cac_diem_can_ve_y = list(set(cac_diem_can_ve_y))
    cac_diem_can_danh_dau_x = [
        boc_latex_mpl(i) for i in cac_diem_can_ve_x]
    cac_diem_can_danh_dau_y = [
        boc_latex_mpl(i) for i in cac_diem_can_ve_y]
    # pyplot.xticks(list(pyplot.xticks()[0]) + cac_diem_can_danh_dau_x)
    # pyplot.yticks(list(pyplot.yticks()[0]) + cac_diem_can_danh_dau_y)
    # pyplot.xticks(cac_diem_can_danh_dau_x)
    # pyplot.yticks(cac_diem_can_danh_dau_y)
    mpl.rc("text", usetex=True)
    pyplot.xticks(cac_diem_can_ve_x, cac_diem_can_danh_dau_x)
    pyplot.yticks(cac_diem_can_ve_y, cac_diem_can_danh_dau_y)
    # for gia_tri in cac_diem_can_ve_y:
    #    pyplot.yticks([float(gia_tri)], [str(gia_tri)])
    #gioi_han_y = 10
    pyplot.ylim(numpy.float64(-abs(max(cac_diem_can_ve_y)) *2),
                numpy.float64(abs(max(cac_diem_can_ve_y))*2))
    # pyplot.ylim(- 10, 5)
    #pyplot.show()
    pyplot.savefig(xuat_file,bbox_inches='tight', pad_inches=0.0)
    # pyplot.show()




if __name__ == '__main__':
    x = sympy.Symbol('x')
    t = sympy.sympify("-2*x^4 +4*(x^2)+6")
    ve_do_thi(t,x,None)
