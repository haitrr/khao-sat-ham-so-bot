import io
import uuid
import re
import xu_ly_chuoi


class LoiGiai:
    """
    Class loi giai
    """

    def __init__(self, de_bai):
        """
        Khoi tao mot loi giai
        :param de_bai: string
        """
        self.ten_loi_giai = de_bai
        self.cac_buoc_giai = list()
        self.dap_an = None
        self.lop_cuoi = True

        # cac cau hoi huong dan
        self.cac_cau_hoi = list()

        # Cac dinh nghia su dung trong bai toan
        self.cac_dinh_nghia = list()
        self.da_neu_dinh_nghia = False

        # Co can huong dan cac buoc con hay khong
        self.can_huong_dan = None

        # Cau hoi dang duoc hoi
        self.cau_hoi_hien_tai = 0

        # Loi giai mau de tham khao
        self.loi_giai_mau = None

    def them_thao_tac(self, buoc):
        """
        Them buoc giai vao loi giai
        :param buoc: BuocGiai
        :return: None
        """
        self.cac_buoc_giai.append(buoc)
        if isinstance(buoc, LoiGiai):
            self.lop_cuoi = False

    def them_danh_sach_thao_tac(self, cac_thao_tac):
        """
        Them mot danh sach cac thao tac vao loi giai
        :param cac_thao_tac: list
        :return: None
        """
        for thao_tac in cac_thao_tac:
            self.cac_buoc_giai.append(thao_tac)
            if isinstance(thao_tac, LoiGiai):
                self.lop_cuoi = False

    def xuat_cac_buoc(self):
        """
        Xuat ra danh sach cac buoc giai cua bai toan
        :return: 
        """
        cac_buoc = []

        # Loi giai khong co buoc con
        if self.lop_cuoi:
            return None
        else:
            dem = 1
            for buoc_giai in self.cac_buoc_giai:
                cac_buoc.append("Bước {stt} : {ten_buoc}".format(stt=str(dem), ten_buoc=buoc_giai.ten_loi_giai))
                dem += 1
            return cac_buoc

    def xuat_loi_huong_dan(self, chinh=True):
        cac_loi_huong_dan = list()
        cac_loi_huong_dan += self.cac_cau_hoi
        if chinh:
            cac_loi_huong_dan.append((self.ten_loi_giai + '<br>Đầu tiên bạn phải {0}'.format(
                self.cac_buoc_giai[0].ten_loi_giai), self.cac_buoc_giai[0].dap_an, self.cac_buoc_giai[0].xuat_html()))
        else:
            cac_loi_huong_dan.append(("Tiếp theo bạn hãy " + self.ten_loi_giai + '<br>Đầu tiên bạn phải {0}'.format(
                self.cac_buoc_giai[0].ten_loi_giai), self.cac_buoc_giai[0].dap_an, self.cac_buoc_giai[0].xuat_html()))
        for buoc in self.cac_buoc_giai[1:-1]:
            if buoc.lop_cuoi is True:
                cac_loi_huong_dan.append(
                    ("Tiếp theo bạn hãy {0}".format(buoc.ten_loi_giai), buoc.dap_an, buoc.xuat_html()))
            else:
                cac_loi_huong_dan += buoc.xuat_loi_huong_dan(chinh=False)
        cac_loi_huong_dan.append(('Cuối cùng hãy {0}'.format(
            self.cac_buoc_giai[-1].ten_loi_giai), self.cac_buoc_giai[-1].dap_an, self.cac_buoc_giai[-1].xuat_html()))
        return cac_loi_huong_dan

    def xuat_html(self, xuat_file=None, stt_loi_giai='', chinh=True, ten_loi_giai=True):
        """
        Xuat loi giai ra dang html
        :param chinh: boolean
        :param stt_loi_giai: string
        :param xuat_file: string
        :return: string
        """
        output = io.StringIO()

        stt = 1
        # In moi buoc giai ra
        if chinh:
            output.write("<div class='w3-container'>")
            if ten_loi_giai:
                output.write(self.ten_loi_giai + "<br>")
        else:
            id = uuid.uuid4()
            output.write(
                '<button onclick=dat_buoc_giai("{0}") class="w3-btn-block w3-left-align w3-green" '
                'style="width:auto"><b>Bước {1} : {2}</b></button><br>'.format(
                    id, stt_loi_giai, self.ten_loi_giai))
            output.write('<div id="{0}" class="w3-hide w3-container w3-animate-zoom">'.format(id))
        if self.lop_cuoi is False:
            for buoc in self.cac_buoc_giai:
                if chinh:
                    output.write(buoc.xuat_html(stt_loi_giai=str(stt),
                                                chinh=False))
                else:
                    output.write(buoc.xuat_html(stt_loi_giai=stt_loi_giai + '.' + str(stt),
                                                chinh=False))
                stt += 1
        else:
            for buoc in self.cac_buoc_giai:
                output.write(buoc + "<br>")
        output.write('</div>')
        if xuat_file:
            # Moi file hoac tao file khi chua co
            # Phai dung utf-8 hien thi tieng viet
            file_loi_giai_html = open(xuat_file, "w", encoding='utf8')
            # Header cua file phai import mathjax de hien thi bieu thuc
            file_loi_giai_html.write(
                "<!doctype html><html><head><meta charset=\"UTF-8\"><title>Lời giải của bài toán</title><link "
                "rel='stylesheet' href='css/w3.css'><script type=\"text/javascript\" "
                "src=\"http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML\"></script"
                "><script src='js/loi_giai.js' charset='utf-8'></script></head><body>")
            # Dong the
            file_loi_giai_html.write(output.getvalue())
            file_loi_giai_html.write("</body></html>")
        loi_giai_html = output.getvalue()
        # Dong file
        output.close()
        return loi_giai_html


class HoiDap:
    """
    Cau hoi de huong dan hoc sinh lam bai
    bao gom:
    Cau hoi,
    cau tra loi,
    cac tu khoa de xac dinh cau tra loi cua hoc sinh la dung
    """

    def __init__(self, cau_hoi):
        self.cau_hoi = cau_hoi
        self.dap_an = list()
        self.cac_goi_y = list()
        self.goi_y_hien_tai = 0
        self.da_hoi_xong = False

    def kiem_tra_dap_an(self, cau_tra_loi):
        # Chuyen thanh khong dau thuong
        cau_tra_loi = xu_ly_chuoi.chuyen_thanh_khong_dau_thuong(cau_tra_loi)

        # Kiem tra tat ca cac dap an trong danh sach da
        for da in self.dap_an:
            # flag
            khop = True

            # Kiem tra cac tu khoa cua dap an
            for tu_khoa in da.cac_tu_khoa:
                if isinstance(tu_khoa, tuple):
                    trung = False
                    for tk in tu_khoa:
                        tk = r'\b{tk}\b'.format(tk=tk)
                        tim = re.search(tk, cau_tra_loi)
                        if tim:
                            cau_tra_loi = cau_tra_loi[tim.end():]
                            trung = True
                            break
                    if trung is True:
                        continue
                    else:
                        khop = False
                        break
                else:
                    tu_khoa = r'\b{tk}\b'.format(tk=tu_khoa)
                    tim = re.search(tu_khoa, cau_tra_loi)
                    if tim:
                        cau_tra_loi = cau_tra_loi[tim.end():]
                        continue
                    else:
                        khop = False
                        break
            if khop:
                return da
        return None


class DapAnCauHoi:
    def __init__(self, dap_an, cac_tu_khoa):
        self.dap_an = dap_an
        self.cac_tu_khoa = cac_tu_khoa
