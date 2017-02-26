import dao_ham
import phuong_trinh
import tinh_xac_dinh


def diem_cuc_tieu(ham_so, bien):
    dao_ham_cap_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    dao_ham_cap_2 = dao_ham.tinh_dao_ham_cap_2(ham_so, bien)
    nghiem_dao_ham_cap_1 = phuong_trinh.tim_nghiem_thuc(dao_ham_cap_1, bien)
    txd = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien)
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
    dao_ham_cap_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien)
    dao_ham_cap_2 = dao_ham.tinh_dao_ham_cap_2(ham_so, bien)
    nghiem_dao_ham_cap_1 = phuong_trinh.tim_nghiem_thuc(dao_ham_cap_1, bien)
    txd = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien)
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