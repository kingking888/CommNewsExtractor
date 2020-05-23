# -*- coding: UTF-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：    news_test.py
   Description :  测试类
   Author :       Andy Zhong
   date：          2019/12/7
-------------------------------------------------
   Change Activity:
                   2020/05/23:
-------------------------------------------------
"""
__author__ = 'Andy Zhong'

import json, urllib3
import requests
from extractors.AutoExtractors import *
from extractors.settings import js_key_dict
from Jsonabstract.Json_abstract import Json_abstract
from tools.automatic_detect import automatic_detect
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class NewsExtract(object):
    def __init__(self):
        """
        已测试网站
        """
        # http://www.chinanews.com/
        self.url = "http://www.chinanews.com/gn/2020/05-23/9192614.shtml"
        # https://www.hao123.com/
        # self.url = "https://www.hao123.com/mid?from=shoubai&key=9412104569053922697&type=rec"
        # https://news.sina.com.cn/
        # self.url = "https://news.sina.com.cn/c/2019-12-10/doc-iihnzahi6563166.shtml"
        # http://www.sohu.com/
        # self.url = "http://www.sohu.com/a/359537759_114988?_f=index_chan08news_6"
        # https://news.qq.com/
        # self.url = "https://new.qq.com/omn/PEG20191/PEG2019121000975400.html"
        # https://news.163.com/
        # self.url = "https://news.163.com/19/1210/20/F02GT6270001899O.html"
        # http://news.ifeng.com/
        # self.url = "https://news.ifeng.com/c/7sIDPyRWK36"
        # http://www.xinhuanet.com/
        # self.url = "http://www.xinhuanet.com/gangao/2019-12/10/c_1125331339.htm"
        # http://env.people.com.cn
        # self.url = "http://env.people.com.cn/n1/2019/1210/c1010-31498499.html"
        # http://news.cctv.com/
        # self.url = "http://news.cctv.com/2019/12/10/ARTIOqy9gwiHXKlH5NWHCPPo191210.shtml?spm=C94212.P4YnMod9m2uD.ENPMkWvfnaiV.16"
        # https://www.huanqiu.com/
        # self.url = "https://opinion.huanqiu.com/article/9CaKrnKog6X"
        # http://news.baidu.com/
        # self.url = "http://news.cctv.com/2019/12/10/ARTISVPiNSCB6N4xWZjRPkNV191210.shtml"
        # http://www.cankaoxiaoxi.com
        # self.url = "http://www.cankaoxiaoxi.com/china/20191210/2397383.shtml"
        # https://www.thepaper.cn/
        # self.url = "https://www.thepaper.cn/newsDetail_forward_5198726"
        # http://www.takungpao.com/
        # self.url = "http://www.takungpao.com/news/232109/2019/1209/387560.html"
        # http://www.stnn.cc/
        # self.url = "http://news.stnn.cc/hongkong/2019/1210/697580.shtml"
        # Json---url
        # self.url = "http://www.zhwhg.com/api/article/read?id=1099"

        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        }
        self.key_dict = js_key_dict
        self.Json_abstract = Json_abstract()

    def start_requests(self):
        html_encoding = automatic_detect(self.url)
        print(html_encoding)
        res = requests.get(url=self.url, headers=self.headers, timeout=5, verify=False)
        if res.status_code == 200:
            try:
                if "www.chinanews.com" in self.url:
                    res.encoding = "utf-8"
                else:
                    res.encoding = html_encoding
                html_content = res.text
                if html_content:
                    return html_content
            except Exception as e:
                # print(e)
                pass

    def judge_if_json(self, html_content):
        if html_content:
            try:
                json_html = json.loads(html_content)
                print("This is Json Html")
                return json_html
            except Exception as e:
                # print(e)
                pass

    def html_extract(self, html_content):
        result = SupperAutoExtract().get_all(html_content, tag=0)
        return result

    def run(self):
        html_content = self.start_requests()
        json_html = self.judge_if_json(html_content)
        if json_html:
            result = self.Json_abstract.all_abstract(json_html, key_exp_dict=self.key_dict)
        else:
            result = self.html_extract(html_content)
        print(result)


if __name__ == '__main__':
    ne = NewsExtract()
    ne.run()

