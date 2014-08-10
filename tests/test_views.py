#-*- coding:utf-8 -*-
from test import test_support
from flask.ext.testing import TestCase
from flask_seed import app

class ViewTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_principal(self):
        r = self.client.get('/')
        self.assert_401(r)
        r = self.client.post('/login',{'username':'banxi','password':'123456'})
        self.assert_200(r)


def test_main():
    test_support.run_unittest(ViewTestCase)

if __name__ == '__main__':
    test_main()
