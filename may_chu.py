import flask
import flask_socketio
import bot

may_chu = flask.Flask(__name__, static_url_path='', static_folder='')
io = flask_socketio.SocketIO(may_chu)

nguoi_dung = []
hoi_thoai = []
ham_so = []


@may_chu.route('/')
def index():
    return may_chu.send_static_file('chat.html')


@io.on('ket_noi')
def ket_noi():
    print(flask.request.sid + ' da ket noi.')
    nguoi_dung.append(flask.request.sid)
    flask_socketio.emit('phan_hoi', 'Chào bạn, mình có thể giúp gì cho bạn ?', room=flask.request.sid)


@io.on('disconnect')
def ngat_ket_noi():
    print(flask.request.sid + ' da ngat ket noi.')
    nguoi_dung.remove(flask.request.sid)


@io.on('tin_nhan')
def nhan_tin_nhan(tin_nhan):
    # Thu nghiem
    tra_loi = bot.lay_cau_tra_loi(str(tin_nhan))
    flask_socketio.emit('phan_hoi', tra_loi, room=flask.request.sid)

if __name__ == '__main__':
    io.run(may_chu)
