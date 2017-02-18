var gui_tin_nhan = function () {
    var mathFieldSpan = document.getElementById('input_toan1');
    var MQ = MathQuill.getInterface(2);
    var mathField = MQ.MathField(mathFieldSpan, {
        spaceBehavesLikeTab: true
    });
    var tin_nhan = mathField.latex();
    if (tin_nhan == '') return false;
    $("#hoi_thoai").append($('<div class="chat me"><div class="user_photo"><img src="hinh_anh/me.png"></div><p class="chat_message">' +"\\("+ tin_nhan +"\\)"+ '</p></div>'))
    $('#tin_nhan').val('');
    MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
    $("#hoi_thoai").animate({
        scrollTop: $('#hoi_thoai').prop('scrollHeight')
    }, 500);
    return true;
};
$(function () {
    $("#gui").click(gui_tin_nhan);
    return true;
});

$(function () {
    $('#tin_nhan').keydown(function (event) {
        if (event.keyCode == 13) {
            gui_tin_nhan()
            return true;
        }
    })
});
$(function () {
    var mathFieldSpan = document.getElementById('input_toan1');

    var MQ = MathQuill.getInterface(2); // for backcompat
    var mathField = MQ.MathField(mathFieldSpan, {
        spaceBehavesLikeTab: true
    });
});

them_span = function(text){
    if(text==true){
        
    }
}