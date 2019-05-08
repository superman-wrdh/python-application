import chardet


def main():
    ss = [("utf8编码", "utf8"), ("gbk编码", "gbk")]
    for s in ss:
        r = s[0].encode(s[1])
        predict = chardet.detect(r)
        encoding = predict['encoding']
        print(encoding)
        print(r.decode(encoding))


if __name__ == '__main__':
    main()
