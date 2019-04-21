import pdfkit
import os


def list_files(path):
    files = os.listdir(path)
    return [os.path.join(path, f) for f in files if not os.path.isdir(os.path.join(os.path.join(path, f)))]


if __name__ == '__main__':
    # fs = list_files(r"E:\html\test")
    # pdfkit.from_file(fs, 'out.pdf', options={"load-error-handling": "ignore"})
    options = {
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ]
    }
    pdfkit.from_url('https://66super.com', 'out.pdf', options=options)
