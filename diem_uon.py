import dao_ham
import phuong_trinh
import tinh_xac_dinh

def tim_diem_uon(ham_so, bien):
    dao_ham_cap_1 = dao_ham.tinh_dao_ham_cap_1(ham_so, bien).dap_an
    dao_ham_cap_2 = dao_ham.tinh_dao_ham_cap_1(dao_ham_cap_1, bien).dap_an
    nghiem_dao_ham_cap_2 = phuong_trinh.tim_nghiem_thuc(dao_ham_cap_2, bien)
    txd = tinh_xac_dinh.tim_tap_xac_dinh(ham_so, bien).dap_an
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