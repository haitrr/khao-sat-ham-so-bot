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
import de_bai
import hang_so
import tuong_giao_do_thi
import cuc_tri

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

cac_dang_toan = [
    [
        r'^khao sat va ve do thi ham so$',
        'Khảo sát và vẽ đồ thị hàm số',
        [False, hang_so.CAC_HAM_PHAN_THUC + hang_so.CAC_HAM_DA_THUC],
        khao_sat_ham_so.khao_sat_ham_so,
        [('ham_so', 'hàm số'), ('bien', 'biến của hàm số')]
    ],
    [
        r'^tim tham so de ham so don dieu tren mot khoang co do dai cho truoc$',
        'Tìm tham số để hàm số đơn điệu trên một khoảng có độ dài cho trước',
        [True, [hang_so.HAM_BAC_BA]],
        tinh_don_dieu.tim_tham_so_de_ham_so_don_tren_1_khoang_co_do_dai_k,
        [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số'),
         ('do_dai_khoang', 'độ dài khoảng đơn điệu')]
    ],
    [
        r'^tim tham so de ham so nghich bien tren tap xac dinh$',
        'Tìm tham số để hàm số nghịch biến trên tập xác định',
        [True, [hang_so.HAM_BAC_BA]],
        tinh_don_dieu.tim_tham_so_de_ham_so_nghich_bien_tren_tap_xac_dinh,
        [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số')]
    ],
    [
        r'^tim tham so de ham so dong bien tren tap xac dinh$',
        'Tìm tham số để hàm số đồng biến trên tập xác định',
        [True, [hang_so.HAM_BAC_BA]],
        tinh_don_dieu.tim_tham_so_de_ham_so_dong_bien_tren_tap_xac_dinh,
        [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số')]
    ],
    [
        r'^tim tham so de ham so co cuc tri$',
        'Tìm tham số để hàm số có cực trị',
        [True, [hang_so.HAM_DA_THUC+hang_so.HAM_PHAN_THUC]],
        cuc_tri.tim_tham_so_de_ham_so_co_cuc_tri,
        [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số')]
    ],
    [
        r'^tim tham so de ham so co cuc tri nam o hai phia truc tung$',
        'Tìm tham số để hàm số có cực trị nằm ở hai phía trục tung',
        [True, [hang_so.HAM_BAC_BA]],
        cuc_tri.tim_tham_so_de_cuc_tri_nam_o_hai_phia_truc_tung,
        [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số')]
    ],
    [
        r'^tim giao diem cua do thi ham so voi duong thang$',
        'Tìm giao điểm của đồ thị hàm số với đường thẳng',
        [False, hang_so.HAM_PHAN_THUC+hang_so.HAM_DA_THUC],
        cuc_tri.tim_tham_so_de_cuc_tri_nam_o_hai_phia_truc_hoanh,
        [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('duong_thang','đường thẳng')]
    ],
    [
        r'^tim tham so de do thi ham so cat truc hoanh tai mot diem duy nhat$',
        'Tìm tham số để đồ thị hàm số cắt trục hoành tại một điểm duy nhất',
        [True, [hang_so.HAM_BAC_BA]],
        tuong_giao_do_thi.tim_tham_so_de_ham_so_cat_truc_hoanh_tai_1_diem_duy_nhat,
        [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số')]
    ],
    [
        r'^tim tham so de ham so dat cuc tri tai mot diem cho truoc$',
        'Tìm tham số để hàm số đạt cực trị tại một điểm cho trước',
        [True, [hang_so.HAM_BAC_BA,hang_so.HAM_BAC_BON]],
        cuc_tri.tim_tham_so_de_ham_so_dat_cuc_tri_tai_mot_diem,
        [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số'),('diem','điểm đạt cực trị')]
    ],
    [
        r'^tim tham so de ham so dat cuc tieu tai mot diem cho truoc$',
        'Tìm tham số để hàm số đạt cực tieu tại một điểm cho trước',
        [True, [hang_so.HAM_BAC_BA, hang_so.HAM_BAC_BON]],
        cuc_tri.tim_tham_so_de_ham_so_dat_cuc_tieu_tai_mot_diem,
        [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số'), ('diem', 'điểm đạt cực tiểu')]
    ],
    [
        r'^tim tham so de ham so dat cuc tri tai mot diem cho truoc$',
        'Tìm tham số để hàm số đạt cực trị tại một điểm cho trước',
        [True, [hang_so.HAM_BAC_BA, hang_so.HAM_BAC_BON]],
        cuc_tri.tim_tham_so_de_ham_so_dat_cuc_dai_tai_mot_diem,
        [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số'), ('diem', 'điểm đạt cực đại')]
    ],
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
            return xu_ly_chuoi.tao_du_lieu_hop_chon([xu_ly_chuoi.tao_latex(
                list(nguoi_dung_gui.de_bai.du_kien['ham_so'].free_symbols)[1]),
                xu_ly_chuoi.tao_latex(list(nguoi_dung_gui.de_bai.du_kien['ham_so'].free_symbols)[0])],
                'Bạn hãy chọn biến của hàm số')
        else:
            nguoi_dung_gui.de_bai.du_kien['bien'] = list(nguoi_dung_gui.de_bai.du_kien['ham_so'].free_symbols)[0]
            nguoi_dung_gui.cho = 'bai_toan'
            cac_dang_toan_co_the = lay_dang_toan_co_the(nguoi_dung_gui.de_bai.du_kien['ham_so'],
                                                        nguoi_dung_gui.de_bai.du_kien['bien'], False)
            if cac_dang_toan_co_the == []:
                huy(nguoi_dung_gui)
                return 'Không có bài toán nào hỗ trợ biểu thức này,bạn hãy thử nhập biểu thức khác'
            return xu_ly_chuoi.tao_du_lieu_hop_chon(cac_dang_toan_co_the, 'Bạn muốn làm gì với biểu thức này')
    elif nguoi_dung_gui.cho == 'bien':
        try:
            bien = xu_ly_chuoi.chuyen_latex_thanh_sympy(tin_nhan)
        except:
            return "Biến bạn nhập vào không hợp lệ, xin hãy kiểm tra lại"
        if str(type(bien)) == "<class 'sympy.core.symbol.Symbol'>" and bien in list(
                nguoi_dung_gui.de_bai.du_kien['ham_so'].free_symbols):
            nguoi_dung_gui.de_bai.du_kien['bien'] = bien
            nguoi_dung_gui.de_bai.du_kien['tham_so'] = phuong_trinh.lay_tham_so(nguoi_dung_gui.de_bai.du_kien['ham_so'],
                                                                                bien)
            nguoi_dung_gui.cho = 'bai_toan'
            cac_dang_toan_co_the = lay_dang_toan_co_the(nguoi_dung_gui.de_bai.du_kien['ham_so'],
                                                        nguoi_dung_gui.de_bai.du_kien['bien'], True)
            return xu_ly_chuoi.tao_du_lieu_hop_chon(cac_dang_toan_co_the, 'Bạn muốn làm gì với biểu thức này')

    elif nguoi_dung_gui.cho in nguoi_dung_gui.de_bai.du_kien.keys():
        try:
            nguoi_dung_gui.de_bai.du_kien[nguoi_dung_gui.cho] = xu_ly_chuoi.chuyen_latex_thanh_sympy(tin_nhan)
        except:
            return "Dữ kiện bạn nhập vào không hợp lệ, xin hãy kiểm tra lại"
        for du_kien in nguoi_dung_gui.de_bai.du_kien.keys():
            if isinstance(nguoi_dung_gui.de_bai.du_kien[du_kien], str):
                nguoi_dung_gui.cho = du_kien
                return 'Bạn hãy nhập vào {dk}'.format(dk=du_kien[1])
        try:
            nguoi_dung_gui.loi_giai = nguoi_dung_gui.de_bai.giai()
        except:
            huy(nguoi_dung_gui)
            return 'Không thể giải bài toán, hãy xem lại các dữ kiện nhập vào'
        nguoi_dung_gui.loi_huong_dan = nguoi_dung_gui.loi_giai.xuat_loi_huong_dan()
        nguoi_dung_gui.buoc = 0
        return huong_dan_giai(nguoi_dung_gui)
    elif nguoi_dung_gui.cho == "bai_toan":
        return kiem_tra_bai_toan(tin_nhan, nguoi_dung_gui)
    elif nguoi_dung_gui.cho == 'xem':
        if re.match(hang_so.XEM_TOAN_BO_LOI_GIAI, tin_nhan):
            return hien_het(nguoi_dung_gui)
        elif re.match(hang_so.HUY, tin_nhan):
            nguoi_dung_gui.cho = 'ham_so'
            return 'Đã ngừng hướng dẫn bài toán này,hãy nhập một biểu thức khác mình sẽ hướng dẫn bạn tiếp ^-^'
        elif re.match(hang_so.XEM_LOI_GIAI, tin_nhan):
            return xem(nguoi_dung_gui)
    elif nguoi_dung_gui.cho == "dap_an":
        if re.match(hang_so.XEM_LOI_GIAI, tin_nhan):
            return xem(nguoi_dung_gui)
        elif re.match(hang_so.XEM_TOAN_BO_LOI_GIAI, tin_nhan):
            return hien_het(nguoi_dung_gui)
        elif re.match(hang_so.HUY, tin_nhan):
            nguoi_dung_gui.cho = 'ham_so'
            return 'Đã ngừng hướng dẫn bài toán này,hãy nhập một biểu thức khác mình sẽ hướng dẫn bạn tiếp ^-^'
        else:
            try:
                dap_an = xu_ly_chuoi.chuyen_latex_thanh_sympy(tin_nhan)
            except:
                return "Đáp án bạn nhập vào không hợp lệ,xin hãy nhập lại"
            cau_tra_loi = list()
            if so_sanh_dap_an(nguoi_dung_gui.loi_huong_dan[nguoi_dung_gui.buoc][1], dap_an):
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


def so_sanh_dap_an(dap_an, dap_an_nguoi_dung):
    if isinstance(dap_an, list) or isinstance(dap_an, tuple):
        if isinstance(dap_an_nguoi_dung, list):
            dap_an_nguoi_dung_copy = copy.deepcopy(dap_an_nguoi_dung)
            for da in dap_an:
                for dand in dap_an_nguoi_dung_copy:
                    if phuong_trinh.so_sanh(da, dand):
                        dap_an_nguoi_dung_copy.remove(dand)
                        break
                    else:
                        continue
            if dap_an_nguoi_dung_copy == []:
                return True
            else:
                return False
        else:
            if len(dap_an) == 1:
                if isinstance(dap_an_nguoi_dung, sympy.Set):
                    return False
                else:
                    if phuong_trinh.so_sanh(dap_an[0], dap_an_nguoi_dung):
                        return True
                    else:
                        return False
            else:
                return False
    elif isinstance(dap_an, sympy.Set):
        if isinstance(dap_an_nguoi_dung, sympy.Set):
            if dap_an_nguoi_dung.contains(dap_an) and dap_an.contains(dap_an_nguoi_dung):
                return True
            else:
                return False
        else:
            return False
    else:
        if phuong_trinh.so_sanh(dap_an, dap_an_nguoi_dung):
            return True
        else:
            return False


def lay_dang_toan_co_the(ham_so, bien, tham_so=False):
    """
    Lay cac dang toan co the cua ham so da nhap
    :param nguoi_dung.NguoiDung nguoi_dung_gui: 
    :return: 
    """
    loai_hs = phuong_trinh.loai_ham_so(ham_so, bien)
    dang_toan_co_the = list()
    for dang_toan in cac_dang_toan:
        if loai_hs in dang_toan[2][1] and tham_so == dang_toan[2][0]:
            dang_toan_co_the.append(dang_toan[1])
    return dang_toan_co_the


def kiem_tra_bai_toan(tin_nhan, nguoi_dung_gui):
    for dang_toan in cac_dang_toan:
        if re.match(dang_toan[0], tin_nhan):
            loai_hs = phuong_trinh.loai_ham_so(nguoi_dung_gui.de_bai.du_kien['ham_so'],
                                               nguoi_dung_gui.de_bai.du_kien['bien'])
            co_tham_so = 'tham_so' in nguoi_dung_gui.de_bai.du_kien.keys()
            if loai_hs in dang_toan[2][1] and co_tham_so == dang_toan[2][0]:
                nguoi_dung_gui.de_bai.bai_toan = dang_toan[3]
                for du_kien in dang_toan[4]:
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
            else:
                return "Dạng toán này chưa được hỗ trợ,hãy thử dạng khác'"
    return "Dạng toán này chưa được hỗ trợ,hãy thử dạng khác'"


def huy(nguoi_dung_gui):
    nguoi_dung_gui.de_bai = de_bai.DeBai()
    nguoi_dung_gui.cho = 'ham_so'


if __name__ == '__main__':
    da = sympy.oo, sympy.oo
    danrd = [sympy.oo, sympy.oo]
    so_sanh_dap_an(da, danrd)
    x = 1
