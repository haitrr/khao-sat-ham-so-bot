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
        self.ma_loi_giai = uuid.uuid4()
        self.lop_cuoi = True
        self.cac_cau_hoi = list()

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

    def xuat_loi_huong_dan(self, chinh=True):
        cac_loi_huong_dan = list()
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

    def xuat_html(self, xuat_file=None, stt_loi_giai='', chinh=True):
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
            output.write(self.ten_loi_giai + "<br>")
        else:
            output.write(
                '<button onclick=dat_buoc_giai("{0}") class="w3-btn-block w3-left-align w3-green" '
                'style="width:auto"><b>Bước {1} : {2}</b></button><br>'.format(
                    self.ma_loi_giai, stt_loi_giai, self.ten_loi_giai))
            output.write('<div id="{0}" class="w3-hide w3-container w3-animate-zoom">'.format(self.ma_loi_giai))
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
    def __init__(self,cau_hoi):
        self.cau_hoi = cau_hoi
        self.dap_an = list()

    def kiem_tra_dap_an(self,cau_tra_loi):
        cau_tra_loi = xu_ly_chuoi.chuyen_thanh_khong_dau_thuong(cau_tra_loi)
        for da in self.dap_an:
            khop=True
            for tu_khoa in da.cac_tu_khoa:
                tu_khoa=r'\b{tk}\b'.format(tk=tu_khoa)
                tim = re.search(tu_khoa,cau_tra_loi)
                if tim:
                    cau_tra_loi = cau_tra_loi[tim.end():]
                    continue
                else:
                    khop=False
                    break
            if khop:
                return da
        return None

class DapAnCauHoi:
    def __init__(self,dap_an,tu_khoa):
        self.dap_an = dap_an
        self.cac_tu_khoa = self.cac_tu_khoa