from bieu_thuc import *


def giao_diem_voi_truc_hoanh(ham_so, bien):
    nghiem_giao_diem = tim_nghiem_thuc(ham_so, bien)
    giao_diem = []
    for nghiem in nghiem_giao_diem:
        if nghiem.is_infinite:
            continue
        giao_diem.append((nghiem, 0))
    return giao_diem


def giao_diem_voi_truc_tung(ham_so, bien):
    giao_diem = ham_so.subs(bien, 0)
    if giao_diem.is_infinite:
        return []
    return [(0, giao_diem)]
