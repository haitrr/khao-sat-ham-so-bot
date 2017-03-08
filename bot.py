# -*- coding: utf-8 -*-
import re
import khao_sat_ham_so
import xu_ly_chuoi
import khao_sat_ham_so
import sympy
import chatterbot

chatbot = chatterbot.ChatBot(
    'Bot',
    trainer='chatterbot.trainers.ListTrainer'
)

khop_bieu_thuc = r'\$(.+)\$'

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

doi_thoai = [
    [[r'^(?:(?:(?:khao\ssat|ks)\s(?:ham\sso\s|hs\s)?)|kshs\s)\$(.+)\$\s?$'],
     [khao_sat_ham_so.khao_sat_ham_so, [['ham_so', '{0}']]]]
]


def tra_loi(tin_nhan):
    for cac_mau, phan_hoi in doi_thoai:
        for mau in cac_mau:
            khop = re.match(mau, tin_nhan)
            if khop:
                if callable(phan_hoi[0]):
                    tham_so = phan_hoi[1]
                    nhom_khop = khop.groups()
                    for nhom in range(len(nhom_khop)):
                        tham_so[nhom][1] = sympy.sympify(xu_ly_chuoi.chuyen_latex_thanh_sympy(nhom_khop[nhom]))
                    tham_so = dict(tham_so)
                    return phan_hoi[0](**tham_so).xuat_html()

    return 'Không khớp'


def lay_cau_tra_loi(tin_nhan,nguoi_dung_gui):
    """
    Lay cau tra loi cua bot cho mot tin nhan
    :param tin_nhan: string
    :param nguoi_dung_gui: NguoiDung
    :return: string
    """
    khop = re.match(khop_bieu_thuc,tin_nhan)
    if khop :
        if nguoi_dung_gui.dang_cho == None:
            return 'mo_hop_chon'
        elif nguoi_dung_gui.dang_cho =='bieu_thuc':
            bieu_thuc_nhap_vao = khop.group(0)
            bieu_thuc_nhap_vao=xu_ly_chuoi.chuyen_latex_thanh_sympy(bieu_thuc_nhap_vao)
            nguoi_dung_gui.loi_giai = nguoi_dung_gui.bai_toan(bieu_thuc_nhap_vao)
        elif isinstance(nguoi_dung_gui.dang_cho,list):


    cau_tra_loi = tra_loi(tin_nhan)
    return cau_tra_loi


if __name__ == '__main__':
    print(chatbot.get_response('chao').text.encode('utf-8'))
