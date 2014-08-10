#-*- coding:utf-8 -*-
import requests
import json

def _avos_api(app_id,app_key):
    if not (app_id and app_key):
        raise Error("App id or app key cannot be None")
    return AvosApi(app_id,app_key)

def avos_api():
    from os import environ as envs
    return _avos_api(envs.get('FLASK_SEED_AVOS_APP_ID'),
                     envs.get('FLASK_SEED_AVOS_APP_KEY'))

class AvosApi(object):
    BASE_URL = 'https://cn.avoscloud.com/1'

    def __init__(self,app_id,app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.session = requests.session()
        self.session.headers['X-AVOSCloud-Application-Id'] = self.app_id
        self.session.headers['X-AVOSCloud-Application-Key'] = self.app_key
        self.post_content_type = {'Content-Type': 'application/json'}


    def post(self,path,data):
        return session.post(BASE_URL + path,data=json.dumps(data),headers = self.post_content_type)

    def put(self,path,data):
        return session.put(BASE_URL + path,data=json.dumps(data),headers = self.post_content_type)

    def get(self,path,params)
        return session.get(BASE_URL + path,params=params)

    def regUser(username,password,**options)
        r = self.post('/users',{'username':username,'password':password})





