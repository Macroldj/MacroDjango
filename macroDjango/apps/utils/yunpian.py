import json

import requests

from macroDjango.settings import API_KEY


class YunPian(object):
    def __init__(self,api_key):
        self.api_key= api_key
        self.single_send_url = "https://www.baidu.com"

    def send_sms(self,code,mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": {"验证码是: {code}".format(code=code)}
        }
        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == '__main__':
    yun_pian = YunPian("xsaxsaxasxasxas")
    yun_pian.send_sms("",API_KEY)