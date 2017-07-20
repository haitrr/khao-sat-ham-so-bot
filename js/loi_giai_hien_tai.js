/**
 * Created by Hai on 6/16/2017.
 */

function cap_nhat_loi_giai_hien_tai(loi_giai_ht) {
    // todo toi uu hoa viec cap nhat
    $('#loi_giai_hien_tai').html(loi_giai_ht);
    MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
}