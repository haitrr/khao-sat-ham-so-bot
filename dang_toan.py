import cuc_tri
import dao_ham
import gia_tri
import hang_so
import khao_sat_ham_so
import phuong_trinh
import tinh_don_dieu
import tuong_giao_do_thi


class DangToan():
    def __init__(self, khop, ten, can_tham_so, loai_ham_so, ham_giai, cac_du_kien):
        self.khop = khop
        self.ten = ten
        self.can_tham_so = can_tham_so
        self.loai_ham_so = loai_ham_so
        self.ham_giai = ham_giai
        self.cac_du_kien = list()
        for du_kien in cac_du_kien:
            self.cac_du_kien.append(DuKien(du_kien[0], du_kien[1]))


class DuKien():
    def __init__(self, ten_du_kien, mo_ta):
        self.ten_du_kien = ten_du_kien
        self.mo_ta = mo_ta


# TODO: them dang toan
cac_dang_toan = [
    [
        'Cực trị',
        DangToan(
            r'^tim tham so de ham so co cuc tri$',
            'Tìm tham số để hàm số có cực trị',
            True,
            hang_so.CAC_HAM_DA_THUC + hang_so.CAC_HAM_PHAN_THUC,
            cuc_tri.tim_tham_so_de_ham_so_co_cuc_tri,
            [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số')]
        ),
        DangToan(
            r'^tim tham so de ham so co cuc tri nam o hai phia truc tung$',
            'Tìm tham số để hàm số có cực trị nằm ở hai phía trục tung',
            True,
            [hang_so.HAM_BAC_BA],
            cuc_tri.tim_tham_so_de_cuc_tri_nam_o_hai_phia_truc_tung,
            [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số')]
        ),
        DangToan(
            r'^tim tham so de ham so dat cuc tri tai mot diem cho truoc$',
            'Tìm tham số để hàm số đạt cực trị tại một điểm cho trước',
            True,
            [hang_so.HAM_BAC_BA, hang_so.HAM_BAC_BON],
            cuc_tri.tim_tham_so_de_ham_so_dat_cuc_tri_tai_mot_diem,
            [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số'), ('diem', 'điểm đạt cực trị')]
        ),
        DangToan(
            r'^tim tham so de ham so dat cuc tieu tai mot diem cho truoc$',
            'Tìm tham số để hàm số đạt cực tiểu tại một điểm cho trước',
            True,
            [hang_so.HAM_BAC_BA, hang_so.HAM_BAC_BON],
            cuc_tri.tim_tham_so_de_ham_so_dat_cuc_tieu_tai_mot_diem,
            [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số'), ('diem', 'điểm đạt cực tiểu')]
        ),
        DangToan(
            r'^tim tham so de ham so dat cuc dai tai mot diem cho truoc$',
            'Tìm tham số để hàm số đạt cực đại tại một điểm cho trước',
            True,
            [hang_so.HAM_BAC_BA, hang_so.HAM_BAC_BON],
            cuc_tri.tim_tham_so_de_ham_so_dat_cuc_dai_tai_mot_diem,
            [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số'), ('diem', 'điểm đạt cực đại')]
        ),
        DangToan(
            r'^tim tham so de ham so khong co cuc tri$',
            'Tìm tham số để hàm số không có cực trị',
            True,
            hang_so.CAC_HAM_PHAN_THUC + hang_so.CAC_HAM_DA_THUC,
            cuc_tri.tim_tham_so_de_ham_so_khong_co_cuc_tri,
            [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số')]
        ),
    ],
    [
        'Đạo hàm',
        DangToan(
            r'tinh dao ham',
            'Tính đạo hàm',
            False,
            hang_so.CAC_HAM_PHAN_THUC + hang_so.CAC_HAM_DA_THUC,
            dao_ham.tinh_dao_ham_cap_1,
            [('ham_so', 'hàm số'), ('bien', 'biến của hàm số')]
        ),
    ],
    [
        'Cơ bản',
        DangToan(
            r'rut gon',
            'Rút gọn',
            False,
            hang_so.CAC_HAM_PHAN_THUC + hang_so.CAC_HAM_DA_THUC,
            phuong_trinh.rut_gon_bieu_thuc,
            [('ham_so', 'hàm số')]
        ),
        DangToan(
            r'giai phuong trinh',
            'Giải phương trình',
            False,
            hang_so.CAC_HAM_PHAN_THUC + hang_so.CAC_HAM_DA_THUC,
            phuong_trinh.giai_phuong_trinh,
            [('ham_so', 'hàm số'), ('bien', 'biến của hàm số')]
        ),
        DangToan(
            r'phan tich thanh nhan tu',
            'Phân tích thành nhân tử',
            False,
            hang_so.CAC_HAM_PHAN_THUC + hang_so.CAC_HAM_DA_THUC,
            phuong_trinh.phan_tich_thanh_nhan_tu_giai,
            [('ham_so', 'hàm số')]
        ),
    ],
    [
        'Tính đơn điệu',
        DangToan(
            r'^tim tham so de ham so don dieu tren mot khoang co do dai cho truoc$',
            'Tìm tham số để hàm số đơn điệu trên một khoảng có độ dài cho trước',
            True,
            [hang_so.HAM_BAC_BA],
            tinh_don_dieu.tim_tham_so_de_ham_so_don_tren_1_khoang_co_do_dai_k,
            [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số'),
             ('do_dai_khoang', 'độ dài khoảng đơn điệu')]
        ),
        DangToan(
            r'^tim tham so de ham so nghich bien tren tap xac dinh$',
            'Tìm tham số để hàm số nghịch biến trên tập xác định',
            True, [hang_so.HAM_BAC_BA],
            tinh_don_dieu.tim_tham_so_de_ham_so_nghich_bien_tren_tap_xac_dinh,
            [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số')]
        ),
        DangToan(
            r'^tim tham so de ham so dong bien tren tap xac dinh$',
            'Tìm tham số để hàm số đồng biến trên tập xác định',
            True,
            [hang_so.HAM_BAC_BA],
            tinh_don_dieu.tim_tham_so_de_ham_so_dong_bien_tren_tap_xac_dinh,
            [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số')]
        ),
    ],
    [
        'Tương giao đồ thị',
        DangToan(
            r'^tim giao diem cua do thi ham so voi duong thang$',
            'Tìm giao điểm của đồ thị hàm số với đường thẳng',
            False,
            hang_so.CAC_HAM_DA_THUC + hang_so.CAC_HAM_PHAN_THUC,
            cuc_tri.tim_tham_so_de_cuc_tri_nam_o_hai_phia_truc_hoanh,
            [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('duong_thang', 'đường thẳng')]
        ),
        DangToan(
            r'^tim tham so de do thi ham so cat truc hoanh tai mot diem duy nhat$',
            'Tìm tham số để đồ thị hàm số cắt trục hoành tại một điểm duy nhất',
            True,
            [hang_so.HAM_BAC_BA],
            tuong_giao_do_thi.tim_tham_so_de_ham_so_cat_truc_hoanh_tai_1_diem_duy_nhat,
            [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('tham_so', 'tham số')]
        ),
        DangToan(
            r'^viet phuong trinh tiep tuyen voi do thi ham so co he so goc cho truoc$',
            'Viết phương trình tiếp tuyến với đồ thị hàm số có hệ số góc cho trước',
            False,
            hang_so.CAC_HAM_PHAN_THUC + hang_so.CAC_HAM_DA_THUC,
            tuong_giao_do_thi.viet_phuong_trinh_tiep_tuyen_voi_do_thi_co_he_so_goc,
            [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('he_so_goc', 'hệ số góc của tiếp tuyến')]
        ),
        DangToan(
            r'^viet phuong trinh tiep tuyen voi do thi ham so di qua mot diem cho truoc$',
            'Viết phương trình tiếp tuyến với đồ thị hàm số đi qua một điểm cho trước',
            False,
            hang_so.CAC_HAM_PHAN_THUC + hang_so.CAC_HAM_DA_THUC,
            tuong_giao_do_thi.viet_phuong_trinh_tiep_tuyen_voi_do_thi_ham_so_di_qua_mot_diem,
            [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('diem', 'điểm mà tiếp tuyến đi qua')]
        ),
    ],
    [
        "Giá trị lớn nhất,nhỏ nhất",
        DangToan(
            r'^tim gia tri lon nhat va nho nhat cua ham so$',
            'Tìm giá trị lớn nhất và nhỏ nhất của hàm số',
            False,
            hang_so.CAC_HAM_DA_THUC + hang_so.CAC_HAM_PHAN_THUC,
            gia_tri.tim_gia_tri_lon_nhat_va_nho_nhat_cua_ham_so,
            [('ham_so', 'hàm số'), ('bien', 'biến của hàm số')]
        ),
        DangToan(
            r'^tim gia tri lon nhat va nho nhat cua ham so trong mot khoang cho truoc',
            'Tìm giá trị lớn nhất và nhỏ nhất của hàm số trong một khoảng cho trước',
            False,
            hang_so.CAC_HAM_DA_THUC + hang_so.CAC_HAM_PHAN_THUC,
            gia_tri.tim_gia_tri_lon_nhat_va_nho_nhat_cua_ham_so_trong_mot_khoang_cho_truoc,
            [('ham_so', 'hàm số'), ('bien', 'biến của hàm số'), ('khoang', 'khoảng')]
        ),
    ],
    DangToan(
        r'^khao sat va ve do thi ham so$',
        'Khảo sát và vẽ đồ thị hàm số',
        False,
        hang_so.CAC_HAM_PHAN_THUC + hang_so.CAC_HAM_DA_THUC,
        khao_sat_ham_so.khao_sat_ham_so,
        [('ham_so', 'hàm số'), ('bien', 'biến của hàm số')]
    ),
]
