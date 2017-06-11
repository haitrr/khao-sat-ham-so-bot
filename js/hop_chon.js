$(document).ready(function () {
    $('#mathpanel').mqmathpanel();
    // Get the modal
    var modal = document.getElementById('hop_chon');
// Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
    };

// When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
    $('.lua_chon').click(function () {
        modal.style.display = "none";
        gui_tin_nhan($(this).text(),false);
    });
});
var khop_muc = /\((.+)\)/g;
them_lua_chon = function (lua_chon,tra_ve) {
    tra_ve = tra_ve || false;
    var cac_lua_chon = $('#cac_lua_chon');
    var du_lieu = khop_muc.exec(lua_chon);
    khop_muc.lastIndex = 0;
    if (du_lieu){
        var rs = "";
        du_lieu = du_lieu[1].split("::");
        i = Math.random().toString(36).substring(7);
        rs+="<button onclick=hien_an_muc('"+i+"') class='w3-btn-block w3-green'><b>"+du_lieu[0]+"</b></button><br>";
        rs+="<div id='"+i+"' class='w3-hide w3-container w3-animate-zoom muc'>";
        du_lieu = du_lieu.slice(1);
        du_lieu.forEach(function (lc) {
            rs+="<div class='w3-button lua_chon'>"+lc+"</div>"
        });
        rs+="</div>";
        cac_lua_chon.append(rs)
    }
    else cac_lua_chon.append("<div class='w3-button lua_chon'>"+lua_chon+"</div><br>");
};
xoa_cac_lua_chon = function () {
    $('#cac_lua_chon').html('');
};
doi_tua_de = function (tua_de) {
    $('#tua_de').html(tua_de);
};
them_click_event=function () {
    var modal = document.getElementById('hop_chon');
    $('.lua_chon').click(function () {
        modal.style.display = "none";
        gui_tin_nhan($(this).text(),false);
    });
};
function hien_an_muc(ma_muc) {
    var muc = document.getElementById(ma_muc);
    if (muc.className.indexOf("w3-show") == -1) {
        var tat_ca_muc = $('.muc');
        tat_ca_muc.each(function () {
            if (this.className.indexOf("w3-show") != -1){
                this.className = this.className.replace(" w3-show", "");
                this.previousElementSibling.className =
                this.previousElementSibling.className.replace(" w3-red", "");
            }
        });
        muc.className += " w3-show";
        muc.previousElementSibling.className += " w3-red";
    } else {
        muc.className = muc.className.replace(" w3-show", "");
        muc.previousElementSibling.className =
            muc.previousElementSibling.className.replace(" w3-red", "");
    }
}