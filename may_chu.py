import flask
import flask_socketio
import bot
import nguoi_dung

may_chu = flask.Flask(__name__, static_url_path='', static_folder='')
io = flask_socketio.SocketIO(may_chu)

cac_nguoi_dung = dict()


@may_chu.route('/')
def index():
    return may_chu.send_static_file('chat.html')


@io.on('ket_noi')
def ket_noi():
    ma_nguoi_dung = flask.request.sid
    print(ma_nguoi_dung + ' da ket noi.')
    nguoi_dung_moi = nguoi_dung.NguoiDung(ma_nguoi_dung)
    cac_nguoi_dung[ma_nguoi_dung] = nguoi_dung_moi
    flask_socketio.emit('phan_hoi', 'Chào bạn, mình có thể giúp gì cho bạn ?', room=nguoi_dung_moi.ma_nguoi_dung)


@io.on('disconnect')
def ngat_ket_noi():
    ma_nguoi_dung = flask.request.sid
    print(ma_nguoi_dung + ' da ngat ket noi.')
    del cac_nguoi_dung[ma_nguoi_dung]


@io.on('tin_nhan')
def nhan_tin_nhan(tin_nhan):
    # Thu nghiem
    ma_nguoi_dung = flask.request.sid
    nguoi_gui = cac_nguoi_dung[ma_nguoi_dung]
    tra_loi = bot.lay_cau_tra_loi(str(tin_nhan),nguoi_gui)
    if isinstance(tra_loi,list):
        for tl in tra_loi:
            flask_socketio.emit('phan_hoi', tl, room=ma_nguoi_dung)
    else:
        flask_socketio.emit('phan_hoi', tra_loi, room=ma_nguoi_dung)

if __name__ == '__main__':
    io.run(may_chu)
