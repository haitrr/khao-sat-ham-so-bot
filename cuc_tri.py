from dao_ham import *
from bieu_thuc import *
from tap_xac_dinh import *

def diem_cuc_tieu(ham_so, bien):
    dao_ham_cap_1 = tinh_dao_ham_cap_1(ham_so, bien)
    dao_ham_cap_2 = tinh_dao_ham_cap_2(ham_so, bien)
    nghiem_dao_ham_cap_1 = tim_nghiem_thuc(dao_ham_cap_1, bien)
    txd = tap_xac_dinh(ham_so, bien)
    nghiem_cuc_tieu = []
    for nghiem in nghiem_dao_ham_cap_1:
        if txd.contains(nghiem) is False:
            continue
        else:
            if dao_ham_cap_2.subs(bien, nghiem) > 0:
                nghiem_cuc_tieu.append(nghiem)
    dct = []
    for nghiem in nghiem_cuc_tieu:
        dct.append((nghiem, ham_so.subs(bien, nghiem)))
    return dct


def diem_cuc_dai(ham_so, bien):
    dao_ham_cap_1 = tinh_dao_ham_cap_1(ham_so, bien)
    dao_ham_cap_2 = tinh_dao_ham_cap_2(ham_so, bien)
    nghiem_dao_ham_cap_1 = tim_nghiem_thuc(dao_ham_cap_1, bien)
    txd = tap_xac_dinh(ham_so, bien)
    nghiem_cuc_dai = []
    for nghiem in nghiem_dao_ham_cap_1:
        if txd.contains(nghiem) is False:
            continue
        else:
            if dao_ham_cap_2.subs(bien, nghiem) < 0:
                nghiem_cuc_dai.append(nghiem)
    dcd = []
    for nghiem in nghiem_cuc_dai:
        dcd.append((nghiem, ham_so.subs(bien, nghiem)))
    return dcd
