import json

import requests

import jsonpath


class ApiKey:
    #基于jsonpath 获取数据关键字，用于提取所需内容
    def get_text(self, data, key):
        dic_data = json.loads(data)
        value_list = jsonpath.jsonpath(dic_data, key)
        return value_list[0]

    def get(self, url, params, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    def post(self, **kwargs):
        return requests.post(**kwargs)



