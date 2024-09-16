from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

authorizer = DummyAuthorizer()

# for login with password
# authorizer.add_user("Afnan", "ammumalik", "/storage/emulated/0", perm="elradfmwMT")
authorizer.add_user(os.getenv("USER"),os.getenv("PASSWORD"), "/storage/emulated/0", perm="elradfmwMT")

# for without password login 
authorizer.add_anonymous("/storage/emulated/0/DCIM/")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("192.168.171.190", 8021), handler)

server.serve_forever()
