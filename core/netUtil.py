# Author Muse
import socket
import json
from conf import settings
class MuseNetUtil:
    def __init__(self):
        self.sk = socket.socket()
        self.sk.connect(settings.addr)

    def send(self,content):
        ret = json.dumps(content)
        self.sk.send(ret.encode(settings.code))