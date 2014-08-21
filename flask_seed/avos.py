#-*- coding:utf-8 -*-
import requests
import json

def _avos_api(app_id,app_key):
    if not (app_id and app_key):
        raise Exception("App id or app key cannot be None")
    return AvosApi(app_id,app_key)

def avos_api():
    from os import environ as envs
    return _avos_api(envs.get('FLASK_SEED_AVOS_APP_ID'),
                     envs.get('FLASK_SEED_AVOS_APP_KEY'))

BASE_URL = 'https://cn.avoscloud.com/1.1'
class AvosApi(object):

    def __init__(self,app_id,app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.session = requests.session()
        self.session.headers['X-AVOSCloud-Application-Id'] = self.app_id
        self.session.headers['X-AVOSCloud-Application-Key'] = self.app_key
        self.post_content_type = {'Content-Type': 'application/json'}


    def post(self,path,data):
        return self.session.post(BASE_URL + path,data=json.dumps(data),headers = self.post_content_type)\
                           .json()

    def put(self,path,data):
        return self.session.put(BASE_URL + path,data=json.dumps(data),headers = self.post_content_type)\
                           .json()

    def get(self,path,params):
        return self.session.get(BASE_URL + path,params=params)\
                           .json()

    def reg_user(self,username,password,**data):
        data['username'] = username
        data['password'] = password
        return self.post('/users',data)

    def create(self,className,data):
        path = '/classes/'+className
        return self.post(path,data)

    def array_add(self,className,objectid,propertyname,objects):
        ''' 为对象的数组字段类型添加数据'''
        d = {
            propertyname:{
                '__op':'addunique',
                'objects':objects
            }
        }
        path = '/classes/'+className+'/'+objectid
        return self.put(path,d)

    def add_relation(self,className,objectId,propertyName,targetClassName,targetObjectId):
        ''' 为对象更新关系字段 '''
        path = '/classes/'+className+'/'+objectId
        data = {
            propertyName:{
                '__op':'AddRelation','objects':[
                {'__type':'Pointer','className':targetClassName,'objectId':targetObjectId}
                ]
            }
        }
        return self.put(path,data)







