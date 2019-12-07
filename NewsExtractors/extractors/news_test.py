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
                   2019/12/7:
-------------------------------------------------
"""
__author__ = 'Andy Zhong'


# import cpca
# from newspaper import Article
import requests
# import html2text
# from readability.readability import Document
from extractors.AutoExtractors import *

class NewsExtract(object):
    def __init__(self):
        # self.url = "http://dy.163.com/v2/article/detail/EVQC8LOO0514D3UH.html"
        self.url = "http://www.chinanews.com/gn/2019/12-07/9027657.shtml"
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            # "Cookie": "BAIDU_SSP_lcr=https://www.baidu.com/link?url=2LitDHEM-W9aA3W1TTRKtnjOzsipIPNC26MeKtkHI1VdYW1IfRlZnCyeXBYqpkEsQtLWnOELJzVu1IETFHAjAlCDT59D1nAi8slyqcCVOhK&wd=&eqid=ef72e4590009b25c000000065dea19ca; Hm_lvt_f2fc44453e24fa1ffd7ca381e15e880d=1575623050; Hm_lpvt_f2fc44453e24fa1ffd7ca381e15e880d=1575623050; Hm_lvt_871ed0033d2b0c46a62993ece27ad71c=1575623051; Hm_lpvt_871ed0033d2b0c46a62993ece27ad71c=1575623051",
            # "Host": "news.e23.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        }

    def start_requests(self):
        res = requests.get(url=self.url,headers=self.headers,timeout=5,verify=False)
        if res.status_code == 200:
            res.encoding = "UTF-8"
            html_content = res.text
            if html_content and len(html_content) > 10 and re.search(r"[\u4E00-\u9FA5]{5,20}",html_content):
                return html_content
            print("提取内容为空或者太短")
            return None

    def html_extract(self, html_content):
        # pass

        # result = {}
        # title = SuperAutoExtract().get_title(html_content)
        # # return title
        #
        # author = SuperAutoExtract().get_author(html_content)
        # # return author
        #
        # publish_time = SuperAutoExtract().get_public_time(html_content)
        # # return publish_time
        #
        # # email = SuperAutoExtract().get_email(html_content)
        # # return email
        #
        # # url = SuperAutoExtract().get_url(html_content)
        # # return url
        #
        # # file = SuperAutoExtract().get_file(html_content)
        # # return file
        #
        # image = SuperAutoExtract().get_image(html_content)
        # # return image
        #
        # video = SuperAutoExtract().get_video(html_content)
        # # return video
        #
        # # title = TitleExtractor().title_extractor(html_content)
        # # content = HtmlContentExtract(html_content).main_body_longest()
        # doc = Document(html_content)
        # content = doc.summary()
        # #
        # # h = html2text.HTML2Text()
        # # h.ignore_links = True
        # # content = h.handle(html_content)
        # # return content
        #
        # result = {
        #     "title": title,
        #     "author": author,
        #     "publish_time": publish_time,
        #     "image": image,
        #     "video": video,
        #     "content" : content,
        # }
        result = SuperAutoExtract().get_all(html_content)
        # result = HtmlContentExtractors().get_contents(html_content)

        return result

    def run(self):
        html_content = self.start_requests()
        result = self.html_extract(html_content)
        print(result)


if __name__ == '__main__':
    ne = NewsExtract()
    ne.run()

