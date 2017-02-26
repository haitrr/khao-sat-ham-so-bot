# -*- coding: utf-8 -*-
import re
import random
from xu_ly_chuoi import chuyen_thanh_khong_dau_thuong, chuyen_latex_thanh_sympy
from khao_sat_ham_so import khao_sat_ham_so
from tao_loi_giai import xuat_html
import sympy
from chatterbot import ChatBot
chatbot = ChatBot(
    'Bot',
    trainer='chatterbot.trainers.ListTrainer'
)

chat_lung_tung=[
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
    [r'^(?:(?:(?:khao\ssat|ks)\s(?:ham\sso\s|hs\s)?)|kshs\s)(\$.+\$)$',
     ["kshs {0}"]],
]


def bien_doi(tin_nhan):
    tokens = tin_nhan.split()
    for i, token in enumerate(tokens):
        if token in tuong_duong:
            tokens[i] = tuong_duong[token]
    return ' '.join(tokens)


def tra_loi(tin_nhan):
    for mau, phan_hoi in doi_thoai:
        khop = re.match(mau, tin_nhan.rstrip(".!"))
        if khop:
            phan_hoi = random.choice(phan_hoi)
            return phan_hoi.format(*[bien_doi(g) for g in khop.groups()])
    return tin_nhan

def kiem_tra(phan_hoi):
    pass

def lay_cau_tra_loi(tin_nhan):
    lenh = tra_loi(chuyen_thanh_khong_dau_thuong(tin_nhan))
    toan = re.match(r'kshs \$(.+)\$', lenh)
    if toan:
        ham_so = chuyen_latex_thanh_sympy(toan.groups()[0])
        ham_so = sympy.sympify(ham_so)
        bien = list(ham_so.free_symbols)[0]
        return xuat_html(khao_sat_ham_so(ham_so,bien))
    else:
        phan_hoi = chatbot.get_response(tin_nhan)
        return phan_hoi.text

if __name__ =='__main__':
    print(chatbot.get_response('chao').text.encode('utf-8'))
