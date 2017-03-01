import io
class BuocGiai:
    """
    Class buoc cua loi giai
    """
    def __init__(self,ten_buoc,stt_buoc):
        """
        khoi tao mot buoc giai
        :param ten_buoc: string
        """
        self.ten_buoc=ten_buoc
        self.cac_thao_tac = list()
        self.ket_qua=None
        self.stt_buoc = stt_buoc

    def them_thao_tac(self,thao_tac):
        """
        Them thao tac vao buoc giai
        :param thao_tac: string
        :return: None
        """
        self.cac_thao_tac.append(thao_tac)

    def xuat_html(self):
        """
        Xuat buoc giai ra html
        :return: str
        """
        output = io.StringIO()
        # In ra ten buoc
        output.write("<b>Bước {0} : {1}</b><br>".format(self.stt_buoc, self.ten_buoc))

        # Xuat ra cac thao tac hoac buoc con
        for thao_tac in self.cac_thao_tac:
            if isinstance(thao_tac,BuocGiai):
                output.write(thao_tac.xuat_html()+"<br>")
            else:
                output.write(thao_tac+"<br>")
        return output.getvalue()

class LoiGiai:
    """
    Class loi giai
    """
    def __init__(self,de_bai):
        """
        Khoi tao mot loi giai
        :param de_bai: string
        """
        self.de_bai = de_bai
        self.cac_buoc_giai=list()

    def them_buoc(self,buoc):
        """
        Them buoc giai vao loi giai
        :param buoc: BuocGiai
        :return: None
        """
        self.cac_buoc_giai.append(buoc)

    def xuat_html(self,xuat_file=None):
        """
        Xuat loi giai ra dang html
        :param xuat_file: string
        :return: string
        """

        output = io.StringIO()
        # In ra de bai
        output.write(self.de_bai+"<br>")

        # In moi buoc giai ra
        for buoc in self.cac_buoc_giai:
            output.write(buoc.xuat_html())

        if xuat_file:
            # Moi file hoac tao file khi chua co
            # Phai dung utf-8 hien thi tieng viet
            file_loi_giai_html = open(xuat_file, "w", encoding='utf8')
            # Header cua file phai import mathjax de hien thi bieu thuc
            file_loi_giai_html.write(
                "<!doctype html><html><head><meta charset=\"UTF-8\"><title>Lời giải của bài toán</title><script type=\"text/javascript\" src=\"http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML\"></script></head><body>")
            # Dong the
            file_loi_giai_html.write(output.getvalue())
            file_loi_giai_html.write("</body></html>")
        loi_giai_html = output.getvalue()
        # Dong file
        output.close()
        return loi_giai_html