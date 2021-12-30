import unittest
from flask_testing import TestCase
from app import create_app
import json


class SettingBase(TestCase):
    def create_app(self):
        return create_app("testing")

      # 在運行測試之前會先被執行
    def setUp(self):
        return

      # 在結束測試時會被執行
    def tearDown(self):
        return

    def index(self):
        response = self.client.get('/')
        return response


# 這邊繼承剛剛的寫的 SettingBase class，接下來會把測試都寫在這裡
class CheckIndex(SettingBase):
    def test_index(self):
        response = self.index()
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

if __name__ == '__main__':
    unittest.main()
