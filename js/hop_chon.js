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