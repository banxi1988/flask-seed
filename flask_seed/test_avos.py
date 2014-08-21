#-*- coding:utf-8 -*-
from pprint import pprint
import time
import avos


avos_api= avos.avos_api()
username = 'banxi'+str(int(time.time()))
r = avos_api.reg_user(username,'1234567')
#{'objectId':'lwlw','createdAt':'','sessionToken':'token'}
pprint(r)

user_objectId = r['objectId']

## 创建course
course = {'name':'Python Programming','gradeName':'高三','className':'(08)班','teacherName':'banxi'}
cr = avos_api.create('Course',course)
pprint(cr)
course_objectId = cr['objectId']

## 为course创建teacher关联到user
ar =  avos_api.add_relation('Course','teacher',course_objectId,'_User',user_objectId)
pprint(ar)


