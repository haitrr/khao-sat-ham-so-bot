from matplotlib import pyplot, rc
from sympy import latex
from PIL import Image
import io


def ve_bieu_thuc_toan_ra_anh(bieu_thuc):
    bieu_thuc = "$" + latex(bieu_thuc) + "$"
    rc("text", usetex=True)
    fig = pyplot.figure()
    text = fig.text(0, 0, bieu_thuc)

    # Saving the figure will render the text.
    buf_temp = io.BytesIO()
    dpi = 300
    fig.savefig(buf_temp, dpi=dpi)

    # Now we can work with text's bounding box.
    bbox = text.get_window_extent()
    width, height = bbox.size / float(dpi) + 0.005
    # Adjust the figure size so it can hold the entire text.
    fig.set_size_inches((width, height))

    # Adjust text's vertical position.
    dy = (bbox.ymin / float(dpi)) / height
    text.set_position((0, -dy))

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    pyplot.close(fig)
    im = Image.open(buf)
    return im
    buf.close()
