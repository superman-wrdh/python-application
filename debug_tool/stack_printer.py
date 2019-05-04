import stackprinter


# https://github.com/cknd/stackprinter
def demo1():
    def dangerous_function(blub):
        return sorted(blub, key=lambda xs: sum(xs))

    try:
        somelist = [[1, 2], [3, 4]]
        anotherlist = [['5', 6]]
        dangerous_function(somelist + anotherlist)
    except Exception as e:
        stackprinter.show(style='plaintext', source_lines=3)


def demo2():
    try:
        1 / 0
    except Exception as e:
        stackprinter.show(style='plaintext', source_lines=3)


if __name__ == '__main__':
    # demo1()
    demo2()
