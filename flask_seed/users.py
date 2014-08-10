#-*- coding:utf-8 -*-
from flask.ext.login import UserMixin
class User(UserMixin):
    def __init__(self,uid,username,password):
        self.id = uid
        self.username = username
        self.password = password

    @classmethod
    def by_id(cls,uid):
        for user in _users:
            if user.id == uid:
                return user
    @classmethod
    def check_login(cls,username,password):
        for user in _users:
            if user.username == username and user.password == password:
                return True,user
        return False,None

_users = [
    User('1','banxi','123456'),
    User('2','iyan','123456'),
    User('3','admin','admin'),
    User('4','superadmin','superadmin'),
    User('5','manager','manager')
]
