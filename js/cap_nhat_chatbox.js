$(function () {
    $('#nhap_tin_nhan').keydown(function (event) {
        if (event.keyCode == 13) {
            gui_tin_nhan_o_chat();
            event.preventDefault();
            return true;
        }
    })
});
var chat_cuoi = 'nguoi';
var o_chat;
var o_chat_element;
var MQ;
var phim_so = true;
$(function () {
    MQ = MathQuill.getInterface(2);
    o_chat_element = document.getElementById('nhap_tin_nhan');
    o_chat = MQ.MathField(o_chat_element);
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
var gui_tin_nhan_o_chat = function () {
    var tin_nhan;
    if (phim_so == true) {
        tin_nhan = o_chat.latex();
        if (tin_nhan == '') return false;
        gui_tin_nhan(tin_nhan);
    }
    else {
        tin_nhan = o_chat.text();
        if (tin_nhan == '') return false;
        gui_tin_nhan(tin_nhan, false);
    }
};
var gui_tin_nhan = function (tin_nhan, latex) {
    latex = typeof latex !== 'undefined' ? latex : true;
    console.log(tin_nhan)
    var hop_chat = $("#hop_chat");
    socket.emit('tin_nhan', tin_nhan);
    if (latex == true) tin_nhan = boc_mathjax(tin_nhan)
    if (chat_cuoi == 'nguoi') {
        hop_chat.append($('<div class="o_tin_nhan toi"><div class="anh_dai_dien an"><img src="hinh_anh/toi.png"></div><div class="tin_nhan">' + tin_nhan + '</div></div>'));

    }
    else {
        hop_chat.append($('<div class="o_tin_nhan toi"><div class="anh_dai_dien"><img src="hinh_anh/toi.png"></div><div class="tin_nhan">' + tin_nhan + '</div></div>'));
        chat_cuoi = 'nguoi';
    }
    o_chat.select();
    o_chat.write("");
    MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
    hop_chat.animate({
        scrollTop: hop_chat.prop('scrollHeight')
    }, 500);
    o_chat.focus();
    return true;
};
var khop = /^mo_hop_chon{(.+)}{(.+)}$/g;

// Nhan tin nhan tu may chu
var nhan_tin_nhan = function (tin_nhan) {
    console.log(tin_nhan);
    // Kiem tra xem co phai la hien bang chon khong
    du_lieu = khop.exec(tin_nhan);
    khop.lastIndex = 0;

    // Xu ly hien bang chon
    if (du_lieu) {
        tua_de = du_lieu[1];
        doi_tua_de(tua_de);
        du_lieu = du_lieu[2].split(';');
        xoa_cac_lua_chon();
        du_lieu.forEach(function (lua_chon) {
            them_lua_chon(lua_chon)
        });
        them_click_event();
        $("#hop_chon").css("display", "block");
    }
    // Chuyen ban phim sang dang chu
    else if (tin_nhan == 'ban_phim_chu') {
        chuyen_ban_phim_chu();
    }

    // Chuyen ban phim sang dang toan
    else if (tin_nhan == 'ban_phim_toan') {
        chuyen_ban_phim_toan();
    }
    // Tin nhan thuong
    else {
        var hop_chat = $("#hop_chat");
        if (chat_cuoi == 'bot') {
            hop_chat.append($('<div class="o_tin_nhan bot"><div class="anh_dai_dien an"><img src="hinh_anh/bot.png"></div><div class="tin_nhan">' + tin_nhan + '</div></div>'));
        }
        else {
            hop_chat.append($('<div class="o_tin_nhan bot"><div class="anh_dai_dien"><img src="hinh_anh/bot.png"></div><div class="tin_nhan">' + tin_nhan + '</div></div>'));
            chat_cuoi = 'bot';
        }
        MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        hop_chat.animate({
            scrollTop: hop_chat.prop('scrollHeight')
        }, 500);
    }
    o_chat.focus();
};
var boc_mathjax = function (tin_nhan) {
    return '\\(' + tin_nhan + '\\)'
};

var chuyen_ban_phim_chu = function () {
    o_chat = MQ.TextField(o_chat_element);
    o_chat_element.classList.remove('mq-math-mode');
    phim_so = false;
    o_chat.select();
    o_chat.write("");
    o_chat.focus();
};

var chuyen_ban_phim_toan = function () {
    o_chat = MQ.MathField(o_chat_element);
    o_chat_element.classList.remove('mq-text-mode');
    phim_so = true;
    o_chat.select();
    o_chat.write("");
    o_chat.focus();
};