# coding:utf-8

import socket
from base64 import encode

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = '''Hello world! <h1> from the5five 《Django》 </h1>'''

response_params = [
    'HTTP/1.0 200 OK',
    'Date: Sun, 12 may 2019 01:01:01 GMT',
    'Content-Type: text/plain; charset=utf-8',
    'Content-Length: {} \r\n'.format(len(body.encode())),
    body,
]

response = '\r\n'.join(response_params)

def handle_conection(conn, address):
    print('oh, new conn', conn, address)
    import time
    time.sleep(10)
    request = b""
    while EOL1 not in request and EOL2 not in request:
        request = conn.recv(1024)
    print(request)
    conn.send(response.encode())    # response 转为bytes后传输
    conn.close()

def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('127.0.0.1', 8000))
    serversocket.listen(5)
    print('http://127.0.0.1:8000')

    try:
        while True:
            conn, address = serversocket.accept()
            handle_conection(conn, address)
    finally:
        serversocket.close()


if __name__ == '__main__':
    main()


