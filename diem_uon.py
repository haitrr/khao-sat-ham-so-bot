from dao_ham import *
from bieu_thuc import *
from tap_xac_dinh import *

def diem_uon(ham_so, bien):
    dao_ham_cap_1 = tinh_dao_ham_cap_1(ham_so, bien)
    dao_ham_cap_2 = tinh_dao_ham_cap_2(dao_ham_cap_1, bien)
    nghiem_dao_ham_cap_2 = tim_nghiem_thuc(dao_ham_cap_2, bien)
    txd = tap_xac_dinh(ham_so, bien)
    nghiem_diem_uon = []
    for nghiem in nghiem_dao_ham_cap_2:
        if txd.contains(nghiem) is False:
            continue
        else:
            nghiem_diem_uon.append(nghiem)
    du = []
    for nghiem in nghiem_diem_uon:
        du.append((nghiem, ham_so.subs(bien, nghiem)))
    return du