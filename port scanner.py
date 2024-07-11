from multiprocessing import Process
from flask import Flask
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def run_server(port):
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return f'Hello, World! I am running on port {port}'

    app.run(host='0.0.0.0', port=port)

def run_ftp_server(port):
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "12345", ".", perm="elradfmw")
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer(("0.0.0.0", port), handler)
    server.serve_forever()

if __name__ == "__main__":
    http_ports = [5000, 5001]  # Add more ports as needed
    ftp_ports = [2121, 2122]  # Add more ports as needed
    servers = []

    for port in http_ports:
        server = Process(target=run_server, args=(port,))
        server.start()
        servers.append(server)

    for port in ftp_ports:
        ftp_server = Process(target=run_ftp_server, args=(port,))
        ftp_server.start()
        servers.append(ftp_server)

    for server in servers:
        server.join()
