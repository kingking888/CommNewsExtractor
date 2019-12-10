# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：    AutoExtractors.py
   Description :  api入口类
   Author :       Andy Zhong
   date：          2019/12/7
-------------------------------------------------
   Change Activity:
                   2019/12/10:
-------------------------------------------------
"""

__author__ = 'Andy Zhong'

from extractors.Extractors import *


class SupperAutoExtract(object):
    def __init__(self):
        pass

    def get_title(self, html):
        if self.judge_html(html):
            return TitleExtractor().title_extractor(html)
        return None

    def get_author(self, html):
        if self.judge_html(html):
            return AuthorExtractor().author_extractor(html)
        return None

    def get_public_time(self, html):
        if self.judge_html(html):
            return TimeExtractor().time_extractor(html)
        return None

    def get_email(self, html):
        if self.judge_html(html):
            return EmailExtractor().email_extractor(html)
        return None

    def get_phone(self, html):
        if self.judge_html(html):
            return PhoneExtractor().phone_extractor(html)
        return None

    def get_telephone(self, html):
        if self.judge_html(html):
            return TelephoneExtractor().telephone_extractor(html)
        return None

    def get_url(self, html):
        if self.judge_html(html):
            return UrlExtractor().url_extractor(html)
        return None

    def get_ip(self, html):
        if self.judge_html(html):
            return IpExtractor().ip_extractor(html)
        return None

    def get_idcard(self, html):
        if self.judge_html(html):
            return IdcardsExtractor().idcards_extractor(html)
        return None

    def get_file(self, html):
        if self.judge_html(html):
            return FilesExtractor().files_extractor(html)
        return None

    def get_image(self, html):
        if self.judge_html(html):
            return ImageExtractor().image_extractor(html)
        return None

    def get_video(self, html):
        if self.judge_html(html):
            return VideosExtractor().videos_extractor(html)
        return None

    def get_content(self, html):
        if self.judge_html(html):
            return ContentExtractor().content_extractor(html)
        return None


    def judge_html(self, html):
        if html and len(html) > 10 and html != "" and \
                re.search(r"[\u4E00-\u9FA5]{10,20}",html):
            return html
        return None

    # News 提取
    def get_all(self, html):
        title = self.get_title(html)
        author = self.get_author(html)
        public_time = self.get_public_time(html)
        content = self.get_content(html)
        video = self.get_video(html)
        result = {
            "title" : title,
            "author": author,
            "public_time": public_time,
            "content": content,
            "video": video,
        }
        return result if result else None









