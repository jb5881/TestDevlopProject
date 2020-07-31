import requests


class TestWeWorkAccess:
    s = requests.Session()

    def setup_class(self):
        params = {
            "corpid": "ww6a5522c914252fa9",
            "corpsecret": "LjvuTF6qMqUs_KVVB8rFKlbXjQxMjijO4a58f68GQ8w"
        }
        r = self.s.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params)
        self.s.params.update({'access_token': r.json()['access_token']})
        print(self.s.params)

    # 添加成员
    def test_create_member(self):
        data = {
            "userid": "zhangsan1",
            "name": "张三1",
            "alias": "jackzhang1",
            "mobile": "+86 13800000002",
            "department": [1]
        }
        r = self.s.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create",
                          json=data)
        print(r.json())

    # 读取成员
    def test_read_member(self):
        params = {
            "userid": "zhangsan1"
        }
        r = self.s.get(url="https://qyapi.weixin.qq.com/cgi-bin/user/get", params=params)
        print(r.json())

    # 更新成员
    def test_update_memeber(self):
        data = {
            "userid": "zhangsan",
            "name": "李四",
            "department": [1]
        }
        r = self.s.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update",
                          json=data)
        print(r.json())

    # 删除成员
    def test_del_memeber(self):
        params = {
            "userid": "zhangsan"
        }
        r = self.s.get(url="https://qyapi.weixin.qq.com/cgi-bin/user/delete", params=params)
        print(r.json())