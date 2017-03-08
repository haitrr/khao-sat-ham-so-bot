$(function () {
    $('#nhap_tin_nhan').keydown(function (event) {
        if (event.keyCode == 13) {
            gui_tin_nhan();
            event.preventDefault();
            return true;
        }
    })
});
var o_chat;
$(function () {
    var MQ = MathQuill.getInterface(2);
    o_chat = document.getElementById('nhap_tin_nhan');
    o_chat = MQ.TextField(o_chat);
});
$(function () {
    o_chat.focus();
});
var socket;
document.addEventListener("DOMContentLoaded", function () {
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
    var hop_chat= $("#hop_chat");
    console.log(tin_nhan);
    socket.emit('tin_nhan', tin_nhan);
    tin_nhan = tin_nhan.replace(/\$(.*)\$/, "\\($1\\)");
    hop_chat.append($('<div class="o_tin_nhan toi"><div class="anh_dai_dien"><img src="hinh_anh/toi.png"></div><div class="tin_nhan">' + tin_nhan + '</div></div>'));
    o_chat.select();
    o_chat.write("");
    MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
    hop_chat.animate({
        scrollTop: hop_chat.prop('scrollHeight')
    }, 500);
    return true;
};
var nhan_tin_nhan = function (tin_nhan) {
    if(tin_nhan=="mo_hop_chon"){
        $("#hop_chon").css("display","block");
    }
    else {
        var hop_chat=$("#hop_chat");
        hop_chat.append($('<div class="o_tin_nhan bot"><div class="anh_dai_dien"><img src="hinh_anh/bot.png"></div><div class="tin_nhan">' + tin_nhan + '</div></div>'));
        MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        hop_chat.animate({
            scrollTop: hop_chat.prop('scrollHeight')
        }, 500);
    }
};