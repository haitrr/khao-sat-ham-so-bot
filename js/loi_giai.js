/**
 * Created by Hai on 3/2/2017.
 */
function dat_buoc_giai(ma_buoc) {
    var buoc = document.getElementById(ma_buoc);
    if (buoc.className.indexOf("w3-show") == -1) {
        buoc.className += " w3-show";
        buoc.previousElementSibling.className += " w3-red";
    } else {
        buoc.className = buoc.className.replace(" w3-show", "");
        buoc.previousElementSibling.className =
            buoc.previousElementSibling.className.replace(" w3-red", "");
    }
}