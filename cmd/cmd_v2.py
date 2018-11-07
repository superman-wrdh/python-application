from subprocess import PIPE, Popen
import chardet


def _cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]


def cmd(command):
    r = _cmdline(command)
    try:
        predict = chardet.detect(r)
        encoding = predict['encoding']
        # print(encoding)
        cr = r.decode(encoding)
    except Exception as e:
        # print(e)
        cr = "error"
    return cr


if __name__ == '__main__':
    result = cmd("ipconfig")
    print(result)
