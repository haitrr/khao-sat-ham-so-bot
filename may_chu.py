from flask import Flask, request
from flask.ext.socketio import SocketIO, emit
import os
from tao_loi_giai import *

may_chu = Flask(__name__, static_url_path='', static_folder='')
io = SocketIO(may_chu)

nguoi_dung = []
hoi_thoai = []
ham_so = []


@may_chu.route('/')
def index():
    return may_chu.send_static_file('chat.html')


@io.on('ket_noi')
def ket_noi():
    print(request.sid + ' da ket noi.')
    nguoi_dung.append(request.sid)
    emit('phan_hoi', 'Chào bạn, mình có thể giúp gì cho bạn ?', room=request.sid)


@io.on('disconnect')
def ngat_ket_noi():
    print(request.sid + ' da ngat ket noi.')
    nguoi_dung.remove(request.sid)


@io.on('tin_nhan')
def nhan_tin_nhan(tin_nhan):
    # Thu nghiem
    print(tin_nhan)
    x = sympy.Symbol('x')
    t = sympy.sympify("x^3 +3*(x^2)-4")
    loi_giai = xuat_html(khao_sat_ham_so(t, x))
    emit('phan_hoi', loi_giai, room=request.sid)

if __name__ == '__main__':
    io.run(may_chu)
