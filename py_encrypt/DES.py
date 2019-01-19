from pyDes import des, CBC, PAD_PKCS5
import binascii

# 秘钥
KEY = 'mHAxsLYz'


def des_encrypt(s):
    """
    DES 加密
    :param s: 原始字符串
    :return: 加密后字符串，16进制
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


def des_decrypt(s):
    """
    DES 解密
    :param s: 加密后的字符串，16进制
    :return:  解密后的字符串
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de


if __name__ == '__main__':
    scr = "this is a simple sentence"
    print("原文", scr)
    encrypt_src = des_encrypt(scr)
    print("加密后", encrypt_src.decode('utf8'))
    decrypt_src = des_decrypt(encrypt_src)
    print("解密后", decrypt_src.decode('utf8'))
