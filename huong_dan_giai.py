import io
import uuid


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

    def them_thao_tac(self, buoc, ten_buoc=None):
        """
        Them buoc giai vao loi giai
        :param buoc: BuocGiai
        :param ten_buoc: string
        :return: None
        """
        self.cac_buoc_giai.append(buoc)
        if isinstance(buoc, LoiGiai):
            self.lop_cuoi = False

    def xuat_html(self, xuat_file=None, stt_loi_giai='', chinh=True):
        """
        Xuat loi giai ra dang html
        :param xuat_file: string
        :return: string
        """
        output = io.StringIO()

        stt = 1
        # In moi buoc giai ra
        if chinh:
            output.write("<div class = 'w3-container'></div>")
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
