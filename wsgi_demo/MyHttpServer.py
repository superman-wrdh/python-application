from wsgiref.simple_server import make_server


# 导入我们自己编写的application函数:
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    request_body = environ['wsgi.input'].read(request_body_size)  # 请求的body
    body = request_body.decode('utf8')
    print(body)
    return [b'<h1>Hello, web!</h1>']


def start_server():
    # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
    httpd = make_server('', 8066, application)
    print('Serving HTTP on port 8066...')
    # 开始监听HTTP请求:
    httpd.serve_forever()


if __name__ == '__main__':
    start_server()
