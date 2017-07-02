THU_MUC_TAM = "./file_tam/"


# Loai ham so
class LoaiHamSo:
    '''
    Các loại hàm số
    '''
    HAM_BAC_NHAT = 'ham bac nhat'
    HAM_BAC_HAI = 'ham bac hai'
    HAM_BAC_BA = 'ham bac ba'
    HAM_BAC_BON = 'ham bac bon'
    HAM_BAC_BON_TRUNG_PHUONG = 'ham bac bon trung phuong'
    HAM_HUU_TY = 'ham huu ty'
    HAM_NHAT_BIEN = 'ham nhat bien'
    HAM_PHAN_THUC = 'ham phan thuc'
    HAM_DA_THUC = 'ham da thuc'
    CAC_HAM_DA_THUC = [
        HAM_BAC_NHAT, HAM_BAC_HAI, HAM_BAC_BA, HAM_BAC_BON,
        HAM_BAC_BON_TRUNG_PHUONG, HAM_DA_THUC
    ]
    CAC_HAM_PHAN_THUC = [HAM_HUU_TY, HAM_NHAT_BIEN, HAM_PHAN_THUC]


#Cau lenh
class CauLenh:
    TRAC_NGHIEM = r'^trac\\ nghiem$'


XEM_LOI_GIAI = r'^xem$'
XEM_TOAN_BO_LOI_GIAI = r'^xem\\ het$'
HUY = r'^huy$'


# Trang thai
class TrangThai:
    CHO_HAM_SO = 'ham_so'
    TRA_LOI_CAU_HOI = 'tra_loi_cau_hoi'
    DAP_AN = 'dap_an'
    XEM_DAP_AN = 'xem'
    BIET_LAM_CHUA = 'biet_lam_chua'
    DAP_AN_TRAC_NGHIEM = 'dap_an_trac_nghiem'
    HIEU_CHUA = 'hieu_chua'
    MAU_OK = ""


# Chuyen ban phim chu
class BanPhim:
    BAN_PHIM_CHU = 'ban_phim_chu'
    BAN_PHIM_TOAN = 'ban_phim_toan'


# Cau tra loi biet lam
class CauTraLoi:
    BIET_LAM = [r'^biet$', r'^biet roi$', r'^duoc$', r'^OK$', r'^roi$']
    HIEU_CACH_LAM = [
        r'^biet$', r'^biet roi$', r'^duoc$', r'^OK$', r'^roi$', r'^hieu$',
        r'^hieu roi$'
    ]
    KHONG_BIET_HIEU = [
        r'khong', r'chua$', r'huong\sdan', r'chua\shieu', r'huong\sdan\s\lai'
    ]
