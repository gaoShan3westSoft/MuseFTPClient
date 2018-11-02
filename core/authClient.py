# Author Muse
import json
from core.netUtil import MuseNetUtil

class Auth:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            obj = object.__new__(cls)
            obj.socket = MuseNetUtil()
            obj.username = None
            cls.__instance = obj
        return cls.__instance

    def login(self):
        username = input('userName:')
        password = input('passward:')
        if username.strip() and password.strip():
            self.socket.mysend({'username':username,'password':password,
                            'operation':'login'})
            loginResult = self.socket.sk.recv(1024)

    def register(self):
        username = input('username : ')
        password1 = input('password : ')
        password2 = input('password_ensure : ')
        if username.strip() and password1.strip() and password1 == password2:
            self.socket.send({'username': username, 'password': password1,
                            'operation': 'register'})
        ret = self.socket.sk.recv(1024)