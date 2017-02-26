$(function () {
    $('#nhap_tin_nhan').keydown(function (event) {
        if (event.keyCode == 13) {
            gui_tin_nhan();
            event.preventDefault();
            return true;
        }
    })
});
$(function () {
    var MQ = MathQuill.getInterface(2);
    var o_chat = document.getElementById('nhap_tin_nhan');
    o_chat = MQ.TextField(o_chat);
});
$(function () {
    o_chat.focus();
});
var socket;
document.addEventListener("DOMContentLoaded", function (event) {
    socket = io.connect('http://' + document.domain + ':' + location.port);
    socket.on('connect', function () {
        socket.emit('ket_noi');
    });
    socket.on('phan_hoi', function (tin_nhan) {
        nhan_tin_nhan(tin_nhan);
    });
});
var gui_tin_nhan = function () {
    var tin_nhan = o_chat.latex();
    if (tin_nhan == '') return false;
    console.log(tin_nhan);
    socket.emit('tin_nhan', tin_nhan);
    tin_nhan = tin_nhan.replace(/\$(.*)\$/, "\\($1\\)");
    $("#hoi_thoai").append($('<div class="o_tin_nhan toi"><div class="anh_dai_dien"><img src="hinh_anh/toi.png"></div><p class="tin_nhan">' + tin_nhan + '</p></div>'));
    o_chat.select();
    o_chat.write("");
    MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
    $("#hoi_thoai").animate({
        scrollTop: $('#hoi_thoai').prop('scrollHeight')
    }, 500);
    return true;
};
var nhan_tin_nhan = function (tin_nhan) {
    $("#hoi_thoai").append($('<div class="o_tin_nhan bot"><div class="anh_dai_dien"><img src="hinh_anh/bot.png"></div><p class="tin_nhan">' + tin_nhan + '</p></div>'));
    MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
    $("#hoi_thoai").animate({
        scrollTop: $('#hoi_thoai').prop('scrollHeight')
    }, 500);
}