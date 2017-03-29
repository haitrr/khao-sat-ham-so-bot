# -*- coding: utf-8 -*-
import re
import khao_sat_ham_so
import xu_ly_chuoi
import khao_sat_ham_so
import sympy
import chatterbot
import phuong_trinh
import nguoi_dung
import tinh_don_dieu
import copy

chatbot = chatterbot.ChatBot(
    'Bot',
    trainer='chatterbot.trainers.ListTrainer'
)


chat_lung_tung = [
    'chào',
    'chào bạn',
    'bạn khỏe không',
    'khỏe như trâu :)',
    'bạn tên gì',
    'tên mình là gì mình cũng không biết',
    'mày là ai',
    'tui là một con bot',
    'anh yêu em',
    'tui cũng vậy :v',
    'tui thích bạn',
    'tui không thích bạn :('
]

chatbot.train(chat_lung_tung)

cac_cau_lenh = [
    [
        '^khao sat ham so$',
        khao_sat_ham_so.khao_sat_ham_so,
        [('ham_so', 'hàm số'), ('bien', 'biến của hàm số')]
    ],
[
        '^tim tham so de ham so don dieu tren mot khoang co do dai cho truoc$',
        tinh_don_dieu.tim_tham_so_de_ham_so_don_tren_1_khoang_co_do_dai_k,
        [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'),('tham_so','tham số'),('do_dai_khoang','độ dài khoảng đơn điệu')]
    ]
]


def lay_cau_tra_loi(tin_nhan, nguoi_dung_gui):
    """
    Lay cau tra loi cua bot cho mot tin nhan
    :param str tin_nhan: tin nhan tu nguoi dung
    :param nguoi_dung.NguoiDung nguoi_dung_gui: nguoi dung gui tin nhan
    :return:
    """
    tin_nhan = xu_ly_chuoi.chuyen_thanh_khong_dau_thuong(tin_nhan)
    if nguoi_dung_gui.cho == 'ham_so':
        try:
            nguoi_dung_gui.de_bai.du_kien['ham_so'] = xu_ly_chuoi.chuyen_latex_thanh_sympy(tin_nhan)
        except:
            return "Biểu thức bạn nhập vào không hợp lệ, xin hãy kiểm tra lại"
        if phuong_trinh.lay_so_bien(nguoi_dung_gui.de_bai.du_kien['ham_so']) == 2:
            nguoi_dung_gui.cho = 'bien'
            return 'Bạn hãy nhập vào biến của hàm số'
        else:
            nguoi_dung_gui.de_bai.du_kien['bien']=list(nguoi_dung_gui.de_bai.du_kien['ham_so'].free_symbols)[0]
            nguoi_dung_gui.cho = 'bai_toan'
            return 'mo_hop_chon'
    elif nguoi_dung_gui.cho == 'bien':
        try:
            bien = xu_ly_chuoi.chuyen_latex_thanh_sympy(tin_nhan)
        except:
            return "Biến bạn nhập vào không hợp lệ, xin hãy kiểm tra lại"
        if str(type(bien))=="<class 'sympy.core.symbol.Symbol'>" and bien in list(nguoi_dung_gui.de_bai.du_kien['ham_so'].free_symbols):
            nguoi_dung_gui.de_bai.du_kien['bien'] = bien
            nguoi_dung_gui.de_bai.du_kien['tham_so']= phuong_trinh.lay_tham_so(nguoi_dung_gui.de_bai.du_kien['ham_so'],bien)
            nguoi_dung_gui.cho = 'bai_toan'
            return 'mo_hop_chon'

    elif nguoi_dung_gui.cho in nguoi_dung_gui.de_bai.du_kien.keys():
        try:
            nguoi_dung_gui.de_bai.du_kien[nguoi_dung_gui.cho] = xu_ly_chuoi.chuyen_latex_thanh_sympy(tin_nhan)
        except:
            return "Dữ kiện bạn nhập vào không hợp lệ, xin hãy kiểm tra lại"
        for du_kien in nguoi_dung_gui.de_bai.du_kien.keys():
            if isinstance(nguoi_dung_gui.de_bai.du_kien[du_kien], str):
                nguoi_dung_gui.cho = du_kien
                return 'Bạn hãy nhập vào {dk}'.format(dk=du_kien[1])
        nguoi_dung_gui.loi_giai = nguoi_dung_gui.de_bai.giai()
        nguoi_dung_gui.loi_huong_dan = nguoi_dung_gui.loi_giai.xuat_loi_huong_dan()
        nguoi_dung_gui.buoc = 0
        return huong_dan_giai(nguoi_dung_gui)
    elif nguoi_dung_gui.cho == "bai_toan":
        for cau_lenh in cac_cau_lenh:
            if re.match(cau_lenh[0], tin_nhan):
                nguoi_dung_gui.de_bai.bai_toan = cau_lenh[1]
                for du_kien in cau_lenh[2]:
                    if du_kien[0] not in nguoi_dung_gui.de_bai.du_kien.keys():
                        nguoi_dung_gui.de_bai.du_kien[du_kien[0]] = du_kien[1]
                for du_kien in nguoi_dung_gui.de_bai.du_kien.keys():
                    if isinstance(nguoi_dung_gui.de_bai.du_kien[du_kien], str):
                        nguoi_dung_gui.cho = du_kien
                        return 'Bạn hãy nhập vào {ten_du_kien}'.format(
                            ten_du_kien=nguoi_dung_gui.de_bai.du_kien[du_kien])
                nguoi_dung_gui.loi_giai = nguoi_dung_gui.de_bai.giai()
                nguoi_dung_gui.loi_huong_dan = nguoi_dung_gui.loi_giai.xuat_loi_huong_dan()
                nguoi_dung_gui.buoc = 0
                return huong_dan_giai(nguoi_dung_gui)
        return "Dạng toán này chưa được hỗ trợ,hãy thử dạng khác'"
    elif nguoi_dung_gui.cho == 'xem':
        if tin_nhan == 'hien het':
            return hien_het(nguoi_dung_gui)
        elif tin_nhan == 'huy':
            nguoi_dung_gui.cho = 'ham_so'
            return 'Đã ngừng hướng dẫn bài toán này,hãy nhập một biểu thức khác mình sẽ hướng dẫn bạn tiếp ^-^'
        elif tin_nhan == 'xem':
            return xem(nguoi_dung_gui)
    elif nguoi_dung_gui.cho == "dap_an":
        if tin_nhan == 'xem':
            return xem(nguoi_dung_gui)
        if tin_nhan == 'hien het':
            return hien_het(nguoi_dung_gui)
        elif tin_nhan == 'huy':
            nguoi_dung_gui.cho = 'ham_so'
            return 'Đã ngừng hướng dẫn bài toán này,hãy nhập một biểu thức khác mình sẽ hướng dẫn bạn tiếp ^-^'
        else:
            try:
                dap_an = xu_ly_chuoi.chuyen_latex_thanh_sympy(tin_nhan)
            except:
                return "Đáp án bạn nhập vào không hợp lệ,xin hãy nhập lại"
            cau_tra_loi = list()
            if so_sanh_dap_an(nguoi_dung_gui.loi_huong_dan[nguoi_dung_gui.buoc][1],dap_an):
                cau_tra_loi.append("Bạn làm đúng rồi")
            else:
                cau_tra_loi.append("Bạn làm không đúng rồi, hãy xem lời giải của mình nhé!")
            cau_tra_loi.append("Lời giải đầy đủ là :<br> {0}".format(
                nguoi_dung_gui.loi_huong_dan[nguoi_dung_gui.buoc][2]))
            nguoi_dung_gui.buoc += 1
            if nguoi_dung_gui.buoc == len(nguoi_dung_gui.loi_huong_dan):
                nguoi_dung_gui.cho = 'ham_so'
            else:
                cau_tra_loi += huong_dan_giai(nguoi_dung_gui)
            return cau_tra_loi

def huong_dan_giai(nguoi_dung_gui):
    """
    Tao loi giai cho bai toan da nhap
    :param nguoi_dung.NguoiDung nguoi_dung_gui: nguoi dung gui
    :return: str:
    """
    cau_tra_loi = list()
    cau_tra_loi.append(nguoi_dung_gui.loi_huong_dan[nguoi_dung_gui.buoc][0])
    if nguoi_dung_gui.loi_huong_dan[nguoi_dung_gui.buoc][1] is None:
        cau_tra_loi.append("Bạn hãy thử làm xem sao, nhập 'xem' mình sẽ cho bạn xem đáp án")
        nguoi_dung_gui.cho = 'xem'
    else:
        nguoi_dung_gui.cho = 'dap_an'
        cau_tra_loi.append("Bạn hãy thử làm xem sao, hãy nhập đáp án của bạn mình sẽ kiểm tra cho bạn")
    return cau_tra_loi


def hien_het(nguoi_dung_gui):
    nguoi_dung_gui.cho = 'ham_so'
    return nguoi_dung_gui.loi_giai.xuat_html()


def xem(nguoi_dung_gui):
    """
    In ra loi giai cua buoc hien tai
    :param nguoi_dung.NguoiDung nguoi_dung_gui:
    :return:
    """
    cau_tra_loi = list()
    cau_tra_loi.append("Lời giải của bước này là :<br> {0}".format(
        nguoi_dung_gui.loi_huong_dan[nguoi_dung_gui.buoc][2]))
    nguoi_dung_gui.buoc += 1
    if nguoi_dung_gui.buoc == len(nguoi_dung_gui.loi_huong_dan):
        nguoi_dung_gui.cho = 'ham_so'
    else:
        cau_tra_loi += huong_dan_giai(nguoi_dung_gui)
    return cau_tra_loi

def so_sanh_dap_an(dap_an,dap_an_nguoi_dung):
    if isinstance(dap_an,list) or isinstance(dap_an,tuple):
        if isinstance(dap_an_nguoi_dung,list):
            dap_an_nguoi_dung_copy=copy.deepcopy(dap_an_nguoi_dung)
            for da in dap_an:
                for dand in dap_an_nguoi_dung_copy:
                    if phuong_trinh.so_sanh(da,dand):
                        dap_an_nguoi_dung_copy.remove(dand)
                        break
                    else:
                        continue
            if dap_an_nguoi_dung_copy==[]:
                return True
            else:
                return False
        else:
            if len(dap_an)==1:
                if isinstance(dap_an_nguoi_dung,sympy.Set):
                    return False
                else:
                    if phuong_trinh.so_sanh(dap_an[0],dap_an_nguoi_dung):
                        return True
                    else:
                        return False
            else:
                return False
    elif isinstance(dap_an,sympy.Set):
        if isinstance(dap_an_nguoi_dung,sympy.Set):
            if dap_an_nguoi_dung.contains(dap_an) and dap_an.contains(dap_an_nguoi_dung):
                return True
            else:
                return False
        else:
            return False
    else:
        if phuong_trinh.so_sanh(dap_an,dap_an_nguoi_dung):
            return True
        else:
            return False

if __name__ == '__main__':
    da=sympy.oo,sympy.oo
    danrd = [sympy.oo,sympy.oo]
    so_sanh_dap_an(da,danrd)
    x=1
