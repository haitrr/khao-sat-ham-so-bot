import time
from matplotlib import pyplot, rc
import sympy as sp
#from sympy import preview
from PIL import Image
import io
rc("text", usetex=True)


def ve_bieu_thuc_toan_ra_anh2(bieu_thuc):
    n = time.time()
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
    fig.savefig(buf)
    buf.seek(0)
    pyplot.close(fig)
    im = Image.open(buf)
    print(time.time() - n)
    return im
    buf.close()


def ve_bieu_thuc_toan_ra_anh(bieu_thuc, fontsize=4, dpi=300):
    """Renders LaTeX formula into image.
    """
    #n = time.time()
    fig = pyplot.figure(figsize=(0.01, 0.01))
    bieu_thuc = "$" + sp.latex(bieu_thuc) + "$"
    fig.text(0, 0, bieu_thuc, fontsize=fontsize)
    buf = io.BytesIO()
    fig.savefig(buf, dpi=dpi,
                bbox_inches='tight', pad_inches=0.0)
    pyplot.close(fig)
    # buf.seek(0)
    im = Image.open(buf)
    #print(time.time() - n)
    return im


def ve_bieu_thuc_toan_ra_anh3(bieu_thuc):
    n = time.time()
    buf = io.BytesIO()
    #preview(bieu_thuc, viewer='file', outputbuffer=buf, euler=False)
    sp.preview(bieu_thuc, viewer='BytesIO', outputbuffer=buf, euler=False)
    im = Image.open(buf)
    print(time.time() - n)
    return im
