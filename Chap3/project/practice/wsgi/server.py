from wsgiref.simple_server import make_server
from hello import application

port = 8080
httpd = make_server('',port,application)
print(f'Serving HTTP on port {port}...')
httpd.serve_forever()
