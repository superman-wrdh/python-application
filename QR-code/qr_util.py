# -*- coding:utf-8 -*-
import qrcode


def simple_qr():
    img = qrcode.make("http://66super.com")
    img.save("qr.png")
    img.show()


def simple_qr2():
    """
    参数定义：
    version：值为1~40的整数，控制二维码的大小（最小值是1，是个21×21的矩阵）。 如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。
    error_correction：控制二维码的错误纠正功能。可取值下列4个常量：
    ERROR_CORRECT_L 大约7%或更少的错误能被纠正
    ERROR_CORRECT_M （默认）大约15%或更少的错误能被纠正
    ERROR_CORRECT_Q 大约25%或更少的错误能被纠正
    ERROR_CORRECT_H.大约30%或更少的错误能被纠正
    box_size：控制二维码中每个小格子包含的像素数。
    border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）
    QRCode官网https://pypi.python.org/pypi/qrcode
    :return:
    """
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('http://66super.com')
    qr.make(fit=True)
    img = qr.make_image()
    img.save("qr3.png")
    img.show()


def make_qr(s):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(s)
    qr.make(fit=True)
    img = qr.make_image()
    return img


def base64_str():
    import base64
    bs = base64.b64encode("I am string".encode(encoding="utf-8"))
    print(bs)


# if __name__ == '__main__':
#     base64_str()