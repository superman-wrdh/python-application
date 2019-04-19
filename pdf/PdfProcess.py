import os, codecs
from PyPDF2 import PdfFileReader, PdfFileMerger


def get_file_list(path):
    files = os.listdir(path)
    return [os.path.join(path, f) for f in files if f.endswith(".pdf") and (not os.path.isdir(os.path.join(path, f)))]


def merge(path):
    merger = PdfFileMerger()
    filelist = get_file_list(path)
    for filename in filelist:
        f = codecs.open(filename, 'rb')
        file_rd = PdfFileReader(f)
        short_filename = os.path.basename(os.path.splitext(filename)[0])
        if file_rd.isEncrypted:
            print('不支持的加密文件：{}'.format(filename))
            continue
        merger.append(file_rd, bookmark=short_filename, import_bookmarks=True)
        print('合并文件：{}'.format(filename))
        f.close()
    out_filename = os.path.join(path, "merge2.pdf")
    merger.write(out_filename)
    print('合并后的输出文件：{}'.format(out_filename))
    merger.close()


if __name__ == '__main__':
    merge(r"E:\书籍\最近\test")
    pass
