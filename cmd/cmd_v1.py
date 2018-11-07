from subprocess import PIPE, Popen


def _cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]


def cmd(command):
    r = _cmdline(command)
    cr = ""
    try:
        cr = r.decode('utf8')
    except Exception as e:
        try:
            cr = r.decode('gbk')
        except Exception as e:
            pass
    return cr
