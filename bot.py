# -*- coding: utf-8 -*-
import re
import xu_ly_chuoi
import sympy
import chatterbot
import phuong_trinh
import nguoi_dung
import copy
import de_bai
import hang_so
import dang_toan
import huong_dan_giai
import trac_nghiem
import random
import dinh_nghia
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

"""
Cau truc dang toan 
[
    regex de match dang toan,
    Ten cua dang toan de nguoi dung chon,
    [Co tham so hay khong ?,Cac dang ham so co the],
    ham de giai toan,
    [Danh sach cac tham so dang (ten tham so,giai thich)]
]
"""


def lay_cau_tra_loi(tin_nhan, nguoi_dung_gui):
    """
    Lay cau tra loi cua bot cho mot tin nhan
    :param str tin_nhan: tin nhan tu nguoi dung
    :param nguoi_dung.NguoiDung nguoi_dung_gui: nguoi dung gui tin nhan
    :return:
    """
    # Chuyen tin nhan ve dang tieng viet thuong khong dau
    tin_nhan = xu_ly_chuoi.chuyen_thanh_khong_dau_thuong(tin_nhan)

    # Cho nguoi dung nhap ham so vao
    if nguoi_dung_gui.cho == 'ham_so':

        # Xem lai loi giai da giai
        if re.match(hang_so.XEM_LOI_GIAI,tin_nhan):
            if nguoi_dung_gui.loi_giai == None:
                return "Bạn chưa giải bài toán nào, hãy thử giải một bài toán trước"
            else:
                return ["Đây là lời giải đầy đủ",nguoi_dung_gui.loi_giai.xuat_html()]
        # Neu hoc sinh yeu cau trac nghiem
        if re.match(hang_so.CauLenh.TRAC_NGHIEM,tin_nhan):
            return chon_cau_trac_nghiem(nguoi_dung_gui)
        print('Ham so : {tn}'.format(tn=tin_nhan))
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
            if not cac_dang_toan_co_the:
                huy(nguoi_dung_gui)
                return 'Không có bài toán nào hỗ trợ biểu thức này,bạn hãy thử nhập biểu thức khác'
            return xu_ly_chuoi.tao_du_lieu_hop_chon(cac_dang_toan_co_the, 'Bạn muốn làm gì với biểu thức này')

    # Nhan vao dap an trac nghiem
    elif nguoi_dung_gui.cho == hang_so.TrangThai.DAP_AN_TRAC_NGHIEM:
        return kiem_tra_da_trac_nghiem(nguoi_dung_gui, tin_nhan)

    # Cho nguoi dung chon bien
    elif nguoi_dung_gui.cho == 'bien':
        print("Bien : {tn}".format(tn=tin_nhan))
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

    # Cho nguoi dung nhap vao mot du kien cua bai toan
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
            if nguoi_dung_gui.loi_giai.lop_cuoi:
                nguoi_dung_gui.cho = 'ham_so'
                return nguoi_dung_gui.loi_giai.xuat_html()
            nguoi_dung_gui.loi_giai.can_huong_dan = True
        except:
            huy(nguoi_dung_gui)
            return 'Không thể giải bài toán, hãy xem lại các dữ kiện nhập vào'
        return huong_dan(nguoi_dung_gui)

    # Cho nguoi dung chon loai bai toan
    elif nguoi_dung_gui.cho == "bai_toan":
        return kiem_tra_bai_toan(tin_nhan, nguoi_dung_gui)

    # Cho nguoi dung nhap cau lenh 'xem' de xem dap an cua buoc giai
    elif nguoi_dung_gui.cho == 'xem':
        if re.match(hang_so.XEM_TOAN_BO_LOI_GIAI, tin_nhan):
            return hien_het(nguoi_dung_gui)
        elif re.match(hang_so.HUY, tin_nhan):
            nguoi_dung_gui.cho = 'ham_so'
            return 'Đã ngừng hướng dẫn bài toán này,hãy nhập một biểu thức khác mình sẽ hướng dẫn bạn tiếp ^-^'
        elif re.match(hang_so.XEM_LOI_GIAI, tin_nhan):
            return xem(nguoi_dung_gui)

    # Cho nguoi dung tra loi cau hoi
    elif nguoi_dung_gui.cho == hang_so.TrangThai.TRA_LOI_CAU_HOI:
        cau_tra_loi = list()
        buoc_hien_tai = nguoi_dung_gui.lay_buoc_hien_tai()
        cau_hoi_hien_tai = buoc_hien_tai.cac_cau_hoi[buoc_hien_tai.cau_hoi_hien_tai]
        da = cau_hoi_hien_tai.kiem_tra_dap_an(tin_nhan)
        if cau_hoi_hien_tai.kiem_tra_dap_an(tin_nhan):
            cau_tra_loi.append('Đúng rồi')
            cau_tra_loi.append(da.dap_an)
            nguoi_dung_gui.loi_giai.cau_hoi_hien_tai+=1
            cau_tra_loi += huong_dan(nguoi_dung_gui)
            return cau_tra_loi
        else:
            if cau_hoi_hien_tai.goi_y_hien_tai == len(cau_hoi_hien_tai.cac_goi_y):
                cau_tra_loi.append('Câu trả lời là : {tl}'.format(tl=cau_hoi_hien_tai.dap_an[0].dap_an))
                nguoi_dung_gui.loi_giai.cau_hoi_hien_tai += 1
                cau_tra_loi += huong_dan(nguoi_dung_gui)
                return cau_tra_loi
            else:
                cau_tra_loi.append('Gợi ý cho bạn nè')
                cau_tra_loi.append(cau_hoi_hien_tai.cac_goi_y[cau_hoi_hien_tai.goi_y_hien_tai])
                cau_hoi_hien_tai.goi_y_hien_tai += 1
                return cau_tra_loi

    # Biet lam chua
    elif nguoi_dung_gui.cho == hang_so.TrangThai.BIET_LAM_CHUA:
        return xu_ly_biet_lam(nguoi_dung_gui, tin_nhan)


    # Hoc sinh hieu cach lam chua
    elif nguoi_dung_gui.cho  == hang_so.TrangThai.HIEU_CHUA:
        for hcl in hang_so.CauTraLoi.HIEU_CACH_LAM:
            if re.match(hcl,tin_nhan):
                return huong_dan(nguoi_dung_gui)
        return dua_ra_bai_toan_mau(nguoi_dung_gui)

    # Cho xac nhan xem xong bai toan mau
    elif nguoi_dung_gui.cho == hang_so.TrangThai.MAU_OK:
        if tin_nhan == 'ok':
            return huong_dan(nguoi_dung_gui)
        else:
            return "Nếu bạn đã xem xong bài giải mẫu hãy chat 'ok' để tiếp tục !"

    # Cho nguoi dung nhap vao dap an
    elif nguoi_dung_gui.cho == "dap_an":

        # Xem loi giai cua buoc hien tai
        if re.match(hang_so.XEM_LOI_GIAI, tin_nhan):
            return xem(nguoi_dung_gui)

        # Xem toan bo loi giai cua bai toan
        elif re.match(hang_so.XEM_TOAN_BO_LOI_GIAI, tin_nhan):
            return hien_het(nguoi_dung_gui)

        # Huy qua trinh huong dan
        elif re.match(hang_so.HUY, tin_nhan):
            nguoi_dung_gui.cho = 'ham_so'
            return 'Đã ngừng hướng dẫn bài toán này,hãy nhập một biểu thức khác mình sẽ hướng dẫn bạn tiếp ^-^'

        # Kiem tra dap an
        else:
            # Chuyen chuoi nhan duoc thanh bieu thuc sympy
            try:
                dap_an = xu_ly_chuoi.chuyen_latex_thanh_sympy(tin_nhan)
            except:
                return "Đáp án bạn nhập vào không hợp lệ,xin hãy nhập lại"

            # Tra loi
            cau_tra_loi = list()
            buoc_hien_tai = nguoi_dung_gui.lay_buoc_hien_tai()
            # So sanh dap an nguoi dung voi dap an
            if so_sanh_dap_an(buoc_hien_tai.dap_an, dap_an):
                cau_tra_loi.append("Bạn làm đúng rồi")
            else:
                cau_tra_loi.append("Bạn làm không đúng rồi, hãy xem lời giải của mình nhé!")

            # Xuat ra loi giai day du
            cau_tra_loi.append("Lời giải đầy đủ là :<br> {lg}".format(
                lg=buoc_hien_tai.xuat_html(chinh=True, ten_loi_giai=False)
            ))

            # Chuyen sang buoc tiep theo
            nguoi_dung_gui.buoc += 1

            # Tang buoc va kiem tra xem het loi giai chua
            if tang_buoc(nguoi_dung_gui):
                cau_tra_loi.append('Xong ! Vậy là đã hoàn thành bài toán. Bạn hãy nhập một bài toán khác')
                nguoi_dung_gui.cho = hang_so.TrangThai.CHO_HAM_SO

            # Neu chua thi huong dan tiep
            else:
                cau_tra_loi += huong_dan(nguoi_dung_gui)
            return cau_tra_loi

def dua_ra_bai_toan_mau(nguoi_dung_gui):
    """
    Dua ra mot bai toan mau cho hoc sinh tham khao
    :param nguoi_dung.NguoiDung nguoi_dung_gui:
    :return:
    """
    cau_tra_loi  = list()
    buoc_hien_tai = nguoi_dung_gui.lay_buoc_hien_tai()
    cau_tra_loi.append("Đây là một bài toán mẫu, bạn hãy tham khảo nha")
    cau_tra_loi.append("Khi xem xong , bạn hãy nói 'OK' để bắt đầu làm bài toán")
    cau_tra_loi.append(buoc_hien_tai.loi_giai_mau)
    nguoi_dung_gui.cho = hang_so.TrangThai.MAU_OK
    cau_tra_loi.append(hang_so.BanPhim.BAN_PHIM_CHU)
    return cau_tra_loi

def huong_dan(nguoi_dung_gui):
    """
    Huong dan nguoi dung bai toan da nhap
    :param nguoi_dung.NguoiDung nguoi_dung_gui: 
    :return: 
    """
    cau_tra_loi = list()
    buoc_hien_tai = nguoi_dung_gui.lay_buoc_hien_tai()
    # Neu buoc giai khong co buoc con
    if buoc_hien_tai.lop_cuoi:
        # Neu con cau hoi de hoi
        if buoc_hien_tai.cau_hoi_hien_tai < len(buoc_hien_tai.cac_cau_hoi):
            # In cau hoi
            cau_tra_loi.append(buoc_hien_tai.cac_cau_hoi[buoc_hien_tai.cau_hoi_hien_tai].cau_hoi)

            # Set kich ban
            nguoi_dung_gui.cho = hang_so.TrangThai.TRA_LOI_CAU_HOI

            # Doi ban phim sang ban phim chu
            cau_tra_loi.append(hang_so.BanPhim.BAN_PHIM_CHU)
            return cau_tra_loi
        elif buoc_hien_tai.cac_dinh_nghia != [] and not buoc_hien_tai.da_neu_dinh_nghia:
            # In ra cac dinh nghia
            cau_tra_loi.append("Để giải bài toán này , bạn hay ghi nhớ các định nghĩa sau đây")
            for dn in buoc_hien_tai.cac_dinh_nghia:
                cau_tra_loi.append(dn.xuat())
            buoc_hien_tai.da_neu_dinh_nghia = True
            cau_tra_loi.append("Bạn đã hiểu cách giải bài toán này chưa")
            nguoi_dung_gui.cho = hang_so.TrangThai.HIEU_CHUA
            return cau_tra_loi
        else:
            # Tạo tên bước
            cau_tra_loi.append("{b}{tb}".format(b=nguoi_dung_gui.xuat_ten_buoc(), tb=buoc_hien_tai.ten_loi_giai))

            # Neu khong can dap an
            if buoc_hien_tai.dap_an is None:
                cau_tra_loi.append("Bạn hãy thử làm xem sao, nhập 'xem' mình sẽ cho bạn xem đáp án")
                nguoi_dung_gui.cho = hang_so.TrangThai.XEM_DAP_AN

            # Neu can dap an
            else:
                nguoi_dung_gui.cho = hang_so.TrangThai.DAP_AN
                cau_tra_loi.append("Bạn hãy thử làm xem sao, hãy nhập đáp án của bạn mình sẽ kiểm tra cho bạn")

            cau_tra_loi.append(hang_so.BanPhim.BAN_PHIM_TOAN)
            return cau_tra_loi
    # Neu co buoc con
    else:
        if buoc_hien_tai.can_huong_dan is None:
            # In ra ten buoc
            cau_tra_loi.append("{b}{tb}".format(b=nguoi_dung_gui.xuat_ten_buoc(), tb=buoc_hien_tai.ten_loi_giai))

            # Hoi xem hoc sinh da biet dang toan nay chua
            cau_tra_loi.append('Bạn đã biết làm dạng toán nào chưa ?')

            # Doi sang ban phim chu
            cau_tra_loi.append(hang_so.BanPhim.BAN_PHIM_CHU)

            # Set kich ban
            nguoi_dung_gui.cho = hang_so.TrangThai.BIET_LAM_CHUA
            return cau_tra_loi
        elif buoc_hien_tai.can_huong_dan is False:
            if buoc_hien_tai.dap_an is None:
                cau_tra_loi.append("Vậy bạn hãy thử làm xem sao, nhập 'xem' mình sẽ cho bạn xem đáp án")
                nguoi_dung_gui.cho = hang_so.TrangThai.XEM_DAP_AN

            # Neu can dap an
            else:
                nguoi_dung_gui.cho = hang_so.TrangThai.DAP_AN
                cau_tra_loi.append("Vậy bạn hãy thử làm xem sao, hãy nhập đáp án của bạn mình sẽ kiểm tra cho bạn")
            return cau_tra_loi
        elif buoc_hien_tai.can_huong_dan is True:
            # Neu con cau hoi de hoi
            if buoc_hien_tai.cau_hoi_hien_tai < len(buoc_hien_tai.cac_cau_hoi):
                # In cau hoi
                cau_tra_loi.append(buoc_hien_tai.cac_cau_hoi[buoc_hien_tai.cau_hoi_hien_tai].cau_hoi)

                # Set kich ban
                nguoi_dung_gui.cho = hang_so.TrangThai.TRA_LOI_CAU_HOI

                # Doi ban phim sang ban phim chu
                cau_tra_loi.append(hang_so.BanPhim.BAN_PHIM_CHU)
                return cau_tra_loi
            elif buoc_hien_tai.cac_dinh_nghia != [] and not buoc_hien_tai.da_neu_dinh_nghia:
                # In ra cac dinh nghia
                cau_tra_loi.append("Để giải bài toán này , bạn hay ghi nhớ các định nghĩa sau đây")
                for dn in buoc_hien_tai.cac_dinh_nghia:
                    cau_tra_loi.append(dn.xuat())
                buoc_hien_tai.da_neu_dinh_nghia = True
                cau_tra_loi.append("Bạn đã hiểu cách giải bài toán này chưa")
                nguoi_dung_gui.cho = hang_so.TrangThai.HIEU_CHUA
                return cau_tra_loi

            # Chuyen buoc hien tai vao buoc con
            nguoi_dung_gui.tien_trinh.append(0)
            cau_tra_loi.append('Vậy mình làm nhé.')
            cau_tra_loi += huong_dan(nguoi_dung_gui)
            return cau_tra_loi
        else:
            raise ValueError


def xu_ly_biet_lam(nguoi_dung_gui, tra_loi):
    """
    Biet lam chua
    :param  nguoi_dung.NguoiDung nguoi_dung_gui: 
    :return: 
    """
    cau_tra_loi = list()
    buoc_hien_tai = nguoi_dung_gui.lay_buoc_hien_tai()
    # Chuyen cau tra loi ve dang tieng viet thuong khong dau
    tra_loi = xu_ly_chuoi.chuyen_thanh_khong_dau_thuong(tra_loi)
    for mau in hang_so.CauTraLoi.BIET_LAM:
        if re.match(mau, tra_loi):
            # Chuyen buoc hien tai thanh buoc con cua buoc giai nay
            buoc_hien_tai.can_huong_dan = False

            # Thong bao
            cau_tra_loi += huong_dan(nguoi_dung_gui)
            return cau_tra_loi
    # Danh dau can huong dan
    buoc_hien_tai.can_huong_dan = True

    # Thong bao
    cau_tra_loi += huong_dan(nguoi_dung_gui)
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
    cau_tra_loi.append("Lời giải của bước này là :<br> {lg}".format(
        lg=nguoi_dung_gui.lay_buoc_hien_tai().xuat_html(chinh=True, ten_loi_giai=False)))

    # Tang buoc va kiem tra xem het loi giai chua
    if tang_buoc(nguoi_dung_gui):
        cau_tra_loi.append('Xong ! Vậy là đã hoàn thành bài toán. Bạn hãy nhập một bài toán khác')
        nguoi_dung_gui.cho = hang_so.TrangThai.CHO_HAM_SO

    # Neu chua thi huong dan tiep
    else:
        cau_tra_loi += huong_dan(nguoi_dung_gui)
    return cau_tra_loi


def tang_buoc(nguoi_dung_gui):
    """
    Tang len buoc tiep theo trong qua trinh huong dan
    :param nguoi_dung.NguoiDung nguoi_dung_gui: 
    :return: da huong dan het hay chua
    """
    nguoi_dung_gui.tien_trinh[-1] += 1
    if kiem_tra_buoc(nguoi_dung_gui):
        return True
    else:
        return False


def kiem_tra_buoc(nguoi_dung_gui):
    """
    Kiem tra va chinh sua lai thu tu buoc
    :param nguoi_dung_gui: 
    :return: da huong dan het hay chua
    """

    # Neu buoc truoc la buoc cuoi cung
    if nguoi_dung_gui.tien_trinh[-1] == len(nguoi_dung_gui.lay_buoc_cha_cua_buoc_hien_tai().cac_buoc_giai):

        # Tro ve buoc cha cua no
        nguoi_dung_gui.tien_trinh = nguoi_dung_gui.tien_trinh[:-1]

        # Neu buoc cha la loi giai
        if nguoi_dung_gui.tien_trinh == []:
            return True

        # Tang buoc cha len mot
        nguoi_dung_gui.tien_trinh[-1] += 1
        # Kiem tra tiep
        kiem_tra_buoc(nguoi_dung_gui)

    # Neu da hop le
    else:
        return False


def so_sanh_dap_an(dap_an, dap_an_nguoi_dung):
    """
    Kiem tra dap an nguoi dung nhap vao co dung khong
    :param dap_an: Dap an dung do bot giai
    :param dap_an_nguoi_dung: Dap an ma nguoi dung nhap vao
    :return: bool
    """

    # Neu dap an la list hoac tuple thi khong can de y thu tu
    if isinstance(dap_an, list) or isinstance(dap_an, tuple):

        # Truong hop dap an cua hoc sinh la list
        if isinstance(dap_an_nguoi_dung, list):
            dap_an_nguoi_dung_copy = copy.deepcopy(dap_an_nguoi_dung)
            for da in dap_an:
                for dand in dap_an_nguoi_dung_copy:
                    if phuong_trinh.so_sanh(da, dand):
                        dap_an_nguoi_dung_copy.remove(dand)
                        break
                    else:
                        continue
            # Neu khop het thi dung khong thi sai
            if not dap_an_nguoi_dung_copy:
                return True
            else:
                return False

        # Dap an hoc sinh khong phai la list
        else:

            # Neu dap an co 1 phan tu thi co the dung
            if len(dap_an) == 1:

                # Neu la khoang thi sai
                if isinstance(dap_an_nguoi_dung, sympy.Set):
                    return False
                else:

                    # So sanh bieu thuc nhap vao voi dap an
                    if phuong_trinh.so_sanh(dap_an[0], dap_an_nguoi_dung):
                        return True
                    else:
                        return False
            else:
                return False

    # Neu dap an la set thi kiem tra nguoi dung co nhap vao set khong
    elif isinstance(dap_an, sympy.Set):
        if isinstance(dap_an_nguoi_dung, sympy.Set):

            # Hai set bang nhau khi chua lan nhau
            if dap_an_nguoi_dung.contains(dap_an) and dap_an.contains(dap_an_nguoi_dung):
                return True
            else:
                return False
        else:
            return False

    # Dap an la mot bieu thuc
    else:

        # So sanh bieu thuc
        if phuong_trinh.so_sanh(dap_an, dap_an_nguoi_dung):
            return True
        else:
            return False


def lay_dang_toan_co_the(ham_so, bien, tham_so=False):
    """
    Lay cac dang toan co the cua ham so da nhap 
    :param ham_so:
    :param bien:
    :param tham_so:
    :return: 
    """
    # Xac dinh loai ham so
    loai_hs = phuong_trinh.loai_ham_so(ham_so, bien)
    dang_toan_co_the = list()

    # Neu khop loai ham so va can tham so thi them vao cac dang toan co the
    for dt in dang_toan.cac_dang_toan:
        if isinstance(dt,dang_toan.DangToan):
            if loai_hs in dt.loai_ham_so and tham_so == dt.can_tham_so:
                dang_toan_co_the.append(dt.ten)
        else:
            rs = [dt[0]]
            for k in dt[1:]:
                if loai_hs in k.loai_ham_so and tham_so == k.can_tham_so:
                    rs.append(k.ten)
            if len(rs)>1:
                dang_toan_co_the.append(rs)
    return dang_toan_co_the


def kiem_tra_bai_toan(tin_nhan, nguoi_dung_gui):
    """
    Kiem tra dang toan nguoi dung nhap vao sau do tao loi giai va huong dan
    :param tin_nhan: 
    :param nguoi_dung_gui: 
    :return: 
    """
    for dt in dang_toan.cac_dang_toan:
        if isinstance(dt,dang_toan.DangToan):
            so = so_khop_du_lieu_dang_toan(dt,tin_nhan,nguoi_dung_gui)
            if so:
                return so
        else:
            for k in dt[1:]:
                so = so_khop_du_lieu_dang_toan(k, tin_nhan, nguoi_dung_gui)
                if so:
                    return so
    return "Dạng toán này chưa được hỗ trợ,hãy thử dạng khác'"

def so_khop_du_lieu_dang_toan(dt,tin_nhan,nguoi_dung_gui):
    """

    :param dt:
    :param tin_nhan:
    :param nguoi_dung_gui:
    :return:
    """
    if re.match(dt.khop, tin_nhan):

        # Kiem tra loai ham so
        loai_hs = phuong_trinh.loai_ham_so(nguoi_dung_gui.de_bai.du_kien['ham_so'],
                                           nguoi_dung_gui.de_bai.du_kien['bien'])

        # Kiem tra xem bai toan co can tham so khong
        co_tham_so = 'tham_so' in nguoi_dung_gui.de_bai.du_kien.keys()

        # So khop dang toan
        if loai_hs in dt.loai_ham_so and co_tham_so == dt.can_tham_so:

            # Gan ham giai cho de bai
            nguoi_dung_gui.de_bai.bai_toan = dt.ham_giai

            for du_kien in dt.cac_du_kien:

                # Neu du kien chua duoc nhap thi gan du kien bang mo ta
                if du_kien.ten_du_kien not in nguoi_dung_gui.de_bai.du_kien.keys():
                    nguoi_dung_gui.de_bai.du_kien[du_kien.ten_du_kien] = du_kien.mo_ta

            # Kiem tra tat ca cac du kien chua nhap, va yeu cau nguoi dung nhap vao
            for du_kien in nguoi_dung_gui.de_bai.du_kien.keys():
                if isinstance(nguoi_dung_gui.de_bai.du_kien[du_kien], str):
                    nguoi_dung_gui.cho = du_kien
                    return 'Bạn hãy nhập vào {ten_du_kien}'.format(
                        ten_du_kien=nguoi_dung_gui.de_bai.du_kien[du_kien])

            # Neu da du du kien thi giai va xuat huong dan
            try:
                nguoi_dung_gui.loi_giai = nguoi_dung_gui.de_bai.giai()
                if nguoi_dung_gui.loi_giai.lop_cuoi:
                    nguoi_dung_gui.cho = 'ham_so'
                    return nguoi_dung_gui.loi_giai.xuat_html()
                nguoi_dung_gui.loi_giai.can_huong_dan = True
            except:
                huy(nguoi_dung_gui)
                return 'Không thể giải bài toán, hãy xem lại các dữ kiện nhập vào'
            # Set buoc huong dan ve 0
            nguoi_dung_gui.buoc = 0

            # Bat dau hang dan
            return huong_dan(nguoi_dung_gui)
        else:
            return "Dạng toán này chưa được hỗ trợ,hãy thử dạng khác'"
    else:
        return None

def chon_cau_trac_nghiem(nguoi_dung_gui):
    """
    Hoi cau trac nghiem bat ky'
    :param nguoi_dung.NguoiDung nguoi_dung_gui:
    :return: 
    """
    cau_tra_loi = list()
    cac_bai_toan = trac_nghiem.cac_cau_hoi_trac_nghiem
    tiep = random.randint(0, len(cac_bai_toan) - 1)
    cac_bai_toan = cac_bai_toan[tiep]

    # Tam thoi chua ho tro chuyen muc
    # Random bai toan
    while isinstance(cac_bai_toan[0], str):
        tiep = random.randint(1, len(cac_bai_toan) - 1)
        cac_bai_toan = cac_bai_toan[tiep]
    tiep = random.randint(0, len(cac_bai_toan) - 1)
    cac_bai_toan = cac_bai_toan[tiep]
    nguoi_dung_gui.trac_nghiem = cac_bai_toan
    # Set trang thai
    nguoi_dung_gui.cho = hang_so.TrangThai.DAP_AN_TRAC_NGHIEM

    # Tra ve de bai
    cau_tra_loi.append(nguoi_dung_gui.trac_nghiem.de_bai)
    cau_tra_loi.append(nguoi_dung_gui.trac_nghiem.xuat_dap_an())
    return cau_tra_loi


def kiem_tra_da_trac_nghiem(nguoi_dung_gui, tin_nhan):
    """
    Kiem tra dap an trac nghiem va dua ra bai giai chi tiet
    :param nguoi_dung.NguoiDung nguoi_dung_gui: 
    :param str tin_nhan: 
    :return: 
    """
    cau_tra_loi = list()
    tin_nhan = xu_ly_chuoi.chuyen_thanh_khong_dau_thuong(tin_nhan)

    # So sanh voi dap an
    if tin_nhan == xu_ly_chuoi.chuyen_thanh_khong_dau_thuong(nguoi_dung_gui.trac_nghiem.dap_an_dung):
        cau_tra_loi.append("Bạn chọn đúng rồi!")
    else:
        cau_tra_loi.append("Câu trả lời của bạn không đúng rồi!")

    # Dua ra dap an dung
    cau_tra_loi.append("Đáp án là {da}".format(
        da=nguoi_dung_gui.trac_nghiem.dap_an_dung
    ))

    # Dua ra loi giai chi tiet
    cau_tra_loi.append("Đây là lời giải chi tiết : \n{lg}".format(
        lg=nguoi_dung_gui.trac_nghiem.giai_chi_tiet())
    )

    # Set trang thai lai
    nguoi_dung_gui.cho = hang_so.TrangThai.CHO_HAM_SO
    nguoi_dung_gui.trac_nghiem = None
    return cau_tra_loi


def huy(nguoi_dung_gui):
    nguoi_dung_gui.de_bai = de_bai.DeBai()
    nguoi_dung_gui.cho = 'ham_so'


if __name__ == '__main__':
    da = sympy.oo, sympy.oo
    danrd = [sympy.oo, sympy.oo]
    so_sanh_dap_an(da, danrd)
    x = 1
