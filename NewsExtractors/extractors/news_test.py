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
                   2019/12/10:
-------------------------------------------------
"""
__author__ = 'Andy Zhong'


import requests
from extractors.AutoExtractors import *


class NewsExtract(object):
    def __init__(self):
        self.url = "http://www.chinanews.com/gn/2019/12-07/9027657.shtml"
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
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

        return result

    def run(self):
        html_content = self.start_requests()
        result = self.html_extract(html_content)
        print(result)


if __name__ == '__main__':
    ne = NewsExtract()
    ne.run()

