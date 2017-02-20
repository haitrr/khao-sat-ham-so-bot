var gui_tin_nhan = function () {
    var tin_nhan = o_chat.latex();
    if (tin_nhan == '') return false;
    tin_nhan = tin_nhan.replace(/\$(.*)\$/,"\\($1\\)");
    $("#hoi_thoai").append($('<div class="chat me"><div class="user_photo"><img src="hinh_anh/me.png"></div><p class="chat_message">' + tin_nhan + '</p></div>'));
    o_chat.select();
    o_chat.write("");
    MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
    $("#hoi_thoai").animate({
        scrollTop: $('#hoi_thoai').prop('scrollHeight')
    }, 500);
    return true;
};
$(function () {
    $('#nhap_tin_nhan').keydown(function (event) {
        if (event.keyCode == 13) {
            gui_tin_nhan();
            event.preventDefault();
            return true;
        }
    })
});
$(function() {
    MQ = MathQuill.getInterface(2);
    o_chat = document.getElementById('nhap_tin_nhan');
    o_chat=MQ.TextField(o_chat);
});
$(function () {
    o_chat.focus();
});