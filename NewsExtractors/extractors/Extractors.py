# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：    Extractors.py
   Description :  通用提取类
   Author :       Andy Zhong
   date：          2019/12/7
-------------------------------------------------
   Change Activity:
                   2019/12/10:
-------------------------------------------------
"""
__author__ = 'Andy Zhong'


import html2text
from extractors.settings import *
from newspaper import fulltext
from extractors.html_content_extractor import *
from readability.readability import Document


# 标题提取类
class TitleExtractor(object):
    def __init__(self):
        self.title_pattern = TITLE_PATTERN
        self.title_split_char_pattern = TITLE_SPLIT_CHAR_PATTERN

    def title_extractor(self, text):
        for pattern in self.title_pattern:
            title_obj = re.search(pattern, text)
            if title_obj:
                title = title_obj.group(1)
                new_title = re.split(self.title_split_char_pattern, title)
                return new_title[0] if new_title else None


# 作者提取类
class AuthorExtractor(object):
    def __init__(self):
        self.author_pattern = AUTHOR_PATTERN

    def author_extractor(self, html):
        for pattern in self.author_pattern:
            author_obj = re.search(pattern, html)
            if author_obj:
                return author_obj.group(1) if author_obj else None


# 发布时间提取类
class TimeExtractor(object):
    def __init__(self):
        self.time_pattern = DATETIME_PATTERN

    def time_extractor(self, html):
        for pattern in self.time_pattern:
            time_obj = re.search(pattern, html)
            if time_obj:
                return time_obj.group(1) if time_obj else None


# 邮箱提取类
class EmailExtractor(object):
    def __init__(self):
        self.email_pattern = EMAIL_PATTERN

    def email_extractor(self, html):
        email_list = []
        for pattern in self.email_pattern:
            email_obj = re.findall(pattern, html)
            if email_obj:
                for em in email_obj:
                    if em:
                        e = em[0]
                        if e and len(e) > 7 and e != "":
                            email_list.append(e)
        return set(email_list) if email_list else None


# 手机提取类
class PhoneExtractor(object):
    def __init__(self):
        self.phone_pattern = PHONE_PATTERN

    def phone_extractor(self, html):
        phone_list = []
        num_str = "345789"
        for pattern in self.phone_pattern:
            phone_obj = re.findall(pattern, html)
            if phone_obj:
                for phone in phone_obj:
                    if phone:
                        p = phone[0]
                        if p and p > 10 and p != "" \
                                and p[1:2] in num_str:
                            phone_list.append(p)
            else:
                return None
        return set(phone_list) if phone_list else None


# 固话提取类
class TelephoneExtractor(object):
    def __init__(self):
        self.telephone_pattern = TELEPHONE_PATTEN
        self.html_clean_pattern = HTML_CLEAN_PATTERN

    def telephone_extractor(self, html):
        new_html = re.sub(self.html_clean_pattern, "", html)
        if new_html and new_html != "":
            telephone_list = []
            for pattern in self.telephone_pattern:
                telephone_obj = re.findall(pattern, html)
                if telephone_obj:
                    for telephone in telephone_obj:
                        if telephone:
                            t = telephone[0]
                            if t and len(t) > 8 and t != "":
                                telephone_list.append(t)
                else:
                    return None
            return set(telephone_list) if telephone_list else None


# url提取类
class UrlExtractor(object):
    def __init__(self):
        self.url_pattern = URL_PATTERN

    def url_extractor(self, html):
        url_list = []
        for pattern in self.url_pattern:
            url_obj = re.findall(pattern, html)
            if url_obj:
                for url in url_obj:
                    if url:
                        u = url[0]
                        if u and len(u) > 5 and u != "":
                            url_list.append(u)
            else:
                return None
        return set(url_list) if url_list else None


# ip提取类
class IpExtractor(object):
    def __init__(self):
        self.ip_pattern = IP_PATTERN

    def ip_extractor(self, html):
        ip_list = []
        for pattern in self.ip_pattern:
            ip_obj = re.findall(pattern, html)
            if ip_obj:
                for ip in ip_obj:
                    if ip:
                        i = ip[0]
                        if i and len(i) > 10 and i != "":
                            ip_list.append(i)
            else:
                return None
        return set(ip_list) if ip_list else None


# 身份证提取类
class IdcardsExtractor(object):
    def __init__(self):
        self.idcards_pattern = IDCARDS_PATTERN

    def idcards_extractor(self, html):
        for pattern in self.idcards_pattern:
            idcards_obj = re.search(pattern, html)
            if idcards_obj:
                return idcards_obj.group(1) \
                    if idcards_obj else None


from lxml import etree


class ImageExtractor(object):
    def __init__(self):
        self.image_pattern = IMAGE_PATTERN
        self.image_type_list = IMAGE_TYPE_LIST
        self.image_xpath_pattern = IMAGE_XPATH_PATTREN

    def image_extractor(self, html_text):
        if html_text and html_text != "":
            try:
                content = HtmlContentExtractors() \
                    .get_contents(html_text)
                if content:
                    images = re.findall(self.image_pattern, content)
                    return images if images else None
            finally:
                pass
            html_text_new = etree.HTML(html_text)
            source_list = []
            for xp in self.image_xpath_pattern:
                image_list = html_text_new.xpath(xp)
                if image_list:
                    for image in image_list:
                        if image and len(image) > 10 and \
                                image != "" and "http" in image:
                            source_list.append(image)
                    continue
                continue

            return set(source_list) if source_list else None

# 图片提取类
# class ImageExtractor(object):
#     def __init__(self):
#         self.image_pattern = IMAGE_PATTERN
#         self.image_type_list = IMAGE_TYPE_LIST
#         self.get_div_pattern = GET_DIV_PATTERN
#
#     def image_extractor(self, html):
#         new_html = "".join(re.findall(self.get_div_pattern[0],html))
#         image_list = []
#         for pattern in self.image_pattern:
#             image_obj = re.findall(pattern, new_html)
#             if image_obj:
#                 for image in image_obj:
#                     if image and len(image) > 20 and image != "" and "http" in image:
#                         for im_t in self.image_type_list:
#                             if im_t in image:
#                                 image_list.append(image)
#
#         return set(image_list)

        # if image_list and image_list != "":
        #     new_image_list = []
        #     for im_t in self.image_type_list:
        #         for im in image_list:
        #             if im_t in im and im.endswith(im_t):
        #                 new_image_list.append(im)
        #     return set(new_image_list)


# 文档提取类
class FilesExtractor(object):
    def __init__(self):
        self.files_pattern = URL_PATTERN
        self.file_type_list = FILE_TYPE_LIST

    def files_extractor(self, html):
        file_list = []
        for pattern in self.files_pattern:
            files_obj = re.findall(pattern, html)
            if files_obj:
                for fi in files_obj:
                    if fi:
                        f = fi[0]
                        if f and len(f) > 4 and f != "":
                            file_list.append(f)
            else:
                return None
        if file_list and file_list != "":
            return self.f_extractor(file_list)
        return None

    def f_extractor(self, file_list):
        new_file_list = []
        for f in self.file_type_list:
            for f_l in file_list:
                if f and f in f_l and f != "" and f_l.endswith(f):
                    new_file_list.append(f_l)
        return set(new_file_list) if new_file_list else None


# 视频提取类
class VideosExtractor(object):
    def __init__(self):
        self.videos_pattern = URL_PATTERN
        self.videos_type_list = VIDEO_TYPE_LIST

    def videos_extractor(self, html):
        video_list = []
        for pattern in self.videos_pattern:
            videos_obj = re.findall(pattern, html)
            if videos_obj:
                for v in videos_obj:
                    v_link = v[0]
                    if v_link and len(v_link) > 5 and v_link != "":
                        video_list.append(v_link)
            else:
                print("没有找到视频链接")
                return None
        if video_list and video_list != "":
            return self.video_extractor(video_list)

    def video_extractor(self, video_list):
        link_list = []
        for f in self.videos_type_list:
            for v in video_list:
                if f and f in v and v.endswith(f):
                    link_list.append(v)
        return set(link_list) if link_list else None


class ContentExtractor(object):
    def __init__(self):
        pass

    def content_extractor(self,html):
        try:
            content = HtmlContentExtractors().get_contents(html)
            if content and content != "":
                return content
            else:
                return self.newspaper_extractor(html)
        except:
            return self.newspaper_extractor(html)

    def newspaper_extractor(self,html):
        try:
            content = fulltext(html)
            if content and content != "":
                return content
            else:
                return self.readability_extractor(html)
        except:
            return self.readability_extractor(html)

    def readability_extractor(self, html):
        try:
            doc = Document(html)
            content = doc.summary()
            if content and content != "":
                return content
            else:
                return self.html2text_extractor(html)
        except:
            return self.html2text_extractor(html)

    def html2text_extractor(self, html):
        try:
            h = html2text.HTML2Text()
            h.ignore_links = True
            content = h.handle(html)
            if content and content != "":
                return content
            else:
                return None
        except:
            return None





