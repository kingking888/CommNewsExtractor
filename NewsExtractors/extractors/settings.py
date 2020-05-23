# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：    settings.py
   Description :  通用设置类
   Author :       Andy Zhong
   date：          2019/12/7
-------------------------------------------------
   Change Activity:
                   2020/05/23:
-------------------------------------------------
"""
__author__ = 'Andy Zhong'

# 作者正则匹配
AUTHOR_PATTERN = [
    r"责编[：|:| |丨|/]\s*([\u4E00-\u9FA5a-zA-Z]{2,20})[^\u4E00-\u9FA5|:|：]",
    r"责任编辑[：|:| |丨|/]\s*([\u4E00-\u9FA5a-zA-Z]{2,20})[^\u4E00-\u9FA5|:|：]",
    r"作者[：|:| |丨|/]\s*([\u4E00-\u9FA5a-zA-Z]{2,20})[^\u4E00-\u9FA5|:|：]",
    r"编辑[：|:| |丨|/]\s*([\u4E00-\u9FA5a-zA-Z]{2,20})[^\u4E00-\u9FA5|:|：]",
    r"文[：|:| |丨|/]\s*([\u4E00-\u9FA5a-zA-Z]{2,20})[^\u4E00-\u9FA5|:|：]",
    r"原创[：|:| |丨|/]\s*([\u4E00-\u9FA5a-zA-Z]{2,20})[^\u4E00-\u9FA5|:|：]",
    r"撰文[：|:| |丨|/]\s*([\u4E00-\u9FA5a-zA-Z]{2,20})[^\u4E00-\u9FA5|:|：]",
    r"来源[：|:| |丨|/]\s*([\u4E00-\u9FA5a-zA-Z]{2,20})[^\u4E00-\u9FA5|:|：|<]",
    r'"editorName":"(.*?)",',
    r'<p class="author-name">(.*?)</p>',
    r'"media": "(.*?)",',
]

# 日期正则匹配
DATETIME_PATTERN = [
    r"(\d{4}[-|/|.]\d{1,2}[-|/|.]\d{1,2}\s*?[0-1]?[0-9]:[0-5]?[0-9]:[0-5]?[0-9])",
    r"(\d{4}[-|/|.]\d{1,2}[-|/|.]\d{1,2}\s*?[2][0-3]:[0-5]?[0-9]:[0-5]?[0-9])",
    r"(\d{4}[-|/|.]\d{1,2}[-|/|.]\d{1,2}\s*?[0-1]?[0-9]:[0-5]?[0-9])",
    r"(\d{4}[-|/|.]\d{1,2}[-|/|.]\d{1,2}\s*?[2][0-3]:[0-5]?[0-9])",
    r"(\d{4}[-|/|.]\d{1,2}[-|/|.]\d{1,2}\s*?[1-24]\d时[0-60]\d分)([1-24]\d时)",
    r"(\d{2}[-|/|.]\d{1,2}[-|/|.]\d{1,2}\s*?[0-1]?[0-9]:[0-5]?[0-9]:[0-5]?[0-9])",
    r"(\d{2}[-|/|.]\d{1,2}[-|/|.]\d{1,2}\s*?[2][0-3]:[0-5]?[0-9]:[0-5]?[0-9])",
    r"(\d{2}[-|/|.]\d{1,2}[-|/|.]\d{1,2}\s*?[0-1]?[0-9]:[0-5]?[0-9])",
    r"(\d{2}[-|/|.]\d{1,2}[-|/|.]\d{1,2}\s*?[2][0-3]:[0-5]?[0-9])",
    r"(\d{2}[-|/|.]\d{1,2}[-|/|.]\d{1,2}\s*?[1-24]\d时[0-60]\d分)([1-24]\d时)",
    r"(\d{4}年\d{1,2}月\d{1,2}日\s*?[0-1]?[0-9]:[0-5]?[0-9]:[0-5]?[0-9])",
    r"(\d{4}年\d{1,2}月\d{1,2}日\s*?[2][0-3]:[0-5]?[0-9]:[0-5]?[0-9])",
    r"(\d{4}年\d{1,2}月\d{1,2}日\s*?[0-1]?[0-9]:[0-5]?[0-9])",
    r"(\d{4}年\d{1,2}月\d{1,2}日\s*?[2][0-3]:[0-5]?[0-9])",
    r"(\d{4}年\d{1,2}月\d{1,2}日\s*?[1-24]\d时[0-60]\d分)([1-24]\d时)",
    r"(\d{2}年\d{1,2}月\d{1,2}日\s*?[0-1]?[0-9]:[0-5]?[0-9]:[0-5]?[0-9])",
    r"(\d{2}年\d{1,2}月\d{1,2}日\s*?[2][0-3]:[0-5]?[0-9]:[0-5]?[0-9])",
    r"(\d{2}年\d{1,2}月\d{1,2}日\s*?[0-1]?[0-9]:[0-5]?[0-9])",
    r"(\d{2}年\d{1,2}月\d{1,2}日\s*?[2][0-3]:[0-5]?[0-9])",
    r"(\d{2}年\d{1,2}月\d{1,2}日\s*?[1-24]\d时[0-60]\d分)([1-24]\d时)",
    r"(\d{1,2}月\d{1,2}日\s*?[0-1]?[0-9]:[0-5]?[0-9]:[0-5]?[0-9])",
    r"(\d{1,2}月\d{1,2}日\s*?[2][0-3]:[0-5]?[0-9]:[0-5]?[0-9])",
    r"(\d{1,2}月\d{1,2}日\s*?[0-1]?[0-9]:[0-5]?[0-9])",
    r"(\d{1,2}月\d{1,2}日\s*?[2][0-3]:[0-5]?[0-9])",
    r"(\d{1,2}月\d{1,2}日\s*?[1-24]\d时[0-60]\d分)([1-24]\d时)",
    r"(\d{4}[-|/|.]\d{1,2}[-|/|.]\d{1,2})",
    r"(\d{2}[-|/|.]\d{1,2}[-|/|.]\d{1,2})",
    r"(\d{4}年\d{1,2}月\d{1,2}日)",
    r"(\d{2}年\d{1,2}月\d{1,2}日)",
    r"(\d{1,2}月\d{1,2}日)",
]

# 部分特别规范的新闻网站，可以直接从 HTML 的 meta 数据中获得发布时间
PUBLISH_TIME_META = [
    '//meta[starts-with(@property, "rnews:datePublished")]/@content',
    '//meta[starts-with(@property, "article:published_time")]/@content',
    '//meta[starts-with(@property, "og:published_time")]/@content',
    '//meta[starts-with(@property, "og:release_date")]/@content',
    '//meta[starts-with(@itemprop, "datePublished")]/@content',
    '//meta[starts-with(@itemprop, "dateUpdate")]/@content',
    '//meta[starts-with(@name, "OriginalPublicationDate")]/@content',
    '//meta[starts-with(@name, "article_date_original")]/@content',
    '//meta[starts-with(@name, "og:time")]/@content',
    '//meta[starts-with(@name, "apub:time")]/@content',
    '//meta[starts-with(@name, "publication_date")]/@content',
    '//meta[starts-with(@name, "sailthru.date")]/@content',
    '//meta[starts-with(@name, "PublishDate")]/@content',
    '//meta[starts-with(@name, "publishdate")]/@content',
    '//meta[starts-with(@name, "PubDate")]/@content',
    '//meta[starts-with(@name, "pubtime")]/@content',
    '//meta[starts-with(@name, "_pubtime")]/@content',
    '//meta[starts-with(@name, "weibo: article:create_at")]/@content',
    '//meta[starts-with(@pubdate, "pubdate")]/@content',
]

# 标题正则匹配
TITLE_PATTERN = [
    r"<title>(.*?)</title>",
    r"<title>\s*(.*?)\s*</title>",
    r"<h1>(.*?)</h1>",
    r"<h2>(.*?)</h2>",
    r"<h3>(.*?)</h3>",
    r"<h4>(.*?)</h4>",
]

# 注释正则匹配
ANNOTATION_PATTERN = [
    "(<!--(.*?)-->)"
]

# 图片匹配
IMAGE_PATTERN = [
    # r"< *[img][^\>]*[src] *= *[\"\']{0,1}([^\"\'\ >]*)",
    r'src="(.*?)"',
    r'<*[img][^\>]*[src]="(.*?)"\s*',
]

# 邮箱正则匹配
EMAIL_PATTERN = [
    r"^[*#\u4e00-\u9fa5 a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$",
    r"([\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?)",
    r"[a-zA-Z0-9]{1,64}@[a-zA-Z0-9]{1,64}(.net|.cn|.com.cn|.com|.org|.edu.cn)",
    r"([a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)",
]

# 手机正则匹配
PHONE_PATTERN = [
    r"^((13[0-9])|(14[0-9])|(15[0-9])|(17[0-9])|(18[0-9])|(19[0-9]))\d{8}$",
    r"^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$",
    r"^((13[0-9])|(14[0-9])|(15[0-9])|(17[0-9])|(18[0-9]))\d{8}$",
    r"(^1\d{10}$)",
    r"(\d{2}[+-]1\d{10})",
]

# 固定电话正则匹配
TELEPHONE_PATTEN = [
    r"(^\(?0\d{2,3}[)-]?\d{7,8}$)",
    r"[0-9-()（）]{7,18}",
    r"(\d{3}|\(\d{3}\))-\d{3}-\d{4}(\s{0,5}(ext|x|ext.|\#)\s{0,5}\d{1,10})?",
    r"(\d{4}-\d{7}|\d{3}-\d{8})",
    r"(\d{2}[+-]\d{4}-\d{7}|\d{3}-\d{8})",

]

# IP匹配
IP_PATTERN = [
    r"(\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b)",
    r"([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])",
    r"^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$",
    r"(?<![:.\w])(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}(?![:.\w])",
]

# 身份证正则匹配
IDCARDS_PATTERN = [
    r"^([1-9]\d{5}[12]\d{3}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])\d{3}[0-9xX])$",
    # 15位
    r"^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$",
    # 18位
    r"^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}([0-9]|X)$"
]

# url正则匹配
URL_PATTERN = [
    r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)|([a-zA-Z]+.\w+\.+[a-zA-Z0-9\/_]+)",
]

# 汉字匹配
CHINESE_PATTERN = [
    r"[\u4E00-\u9FA5]{1,10}"
]

HTML_CLEAN_PATTERN = [
    r"<script|\/script>|<div|\/div>|<li|\/li>|<div|\/div>|html|body|<|>"
]

VIDEO_TYPE_LIST = [
    ".rm", ".rmvb", ".mk", ".mkv", ".mpg", ".mpeg", ".avi",
    ".mp4", ".mp3", ".wma", ".dat", ".mv", ".mov", ".3gp", ".asf"
]

FILE_TYPE_LIST = [
    ".doc", ".docx", ".ppt", ".txt", ".pdf", ".xls",
    "word", ".wps", ".zip", ".rar"
]

IMAGE_TYPE_LIST = [
    ".jpg", ".jpeg", ".tiff", ".raw", ".bmp", ".gif", ".png"
]

GET_IMAGE_PATTERN = [
    r"<div\s*(.*?)\s*\/div>"
]

IMAGE_XPATH_PATTREN = [
    "//image/@src"
    "//div[@id='article']//p//img/@src",
    "//div[@id='article']//img/@src",
    "//div[@class='article-content']//p//img/@src",
    "//div[@class='article-content']//img/@src",
    "//div[starts-with(@class,'main')]//div[@class='img-container']//img/@src",
    "//div[starts-with(@class,'main')]//div[@class='article']//img/@src",
    "//div[starts-with(@class,'article')]//img/@src",
    "//div[@class='content']//div//p//img/@src",
    "//div[@class='content']//div//img/@src",
    "//div[starts-with(@class,'main')]//div[starts-with(@style,'text')]//img/@src"
]

TITLE_SPLIT_CHAR_PATTERN = '[-_|]'

# 提取正文的阈值配置
MIN_PARAGRAPH_LENGHT = 5  # 最小段落长度
MAX_PARAGRAPH_DISTANCE = 5  # 正文段落与段落之间的最大距离 段落之间可能有空白行
MIN_PARAGRAPH_AND_CONTENT_PROPORTION = 0.5  # p标签内的文字长度/正文长度 最小占比
MIN_COUNTENT_WORDS = 500  # 最小文章内容长度
RELEASE_TIME_OFFSET = 10  # 发布时间偏离正文区域的距离， 如正文在 10~28 行 ，发布时间在 (10-RELEASE_TIME_OFFSET) ~ (28 + RELEASE_TIME_OFFSET) 行之内

# html 中需要保留的标签
USEFUL_TAG = [
    r'<img(.|\n)+?>',
    r'<p(.|\n)*?>',
    r'</p>',
    r'<span(.|\n)+?>',
    r'</span>',
    r'<strong.*?>',
    r'</strong>',
    r'<br.*?/>'
]

js_key_dict = {
                "tit_key_exp": "json_text['data']['title']",
                "con_key_exp": "json_text['data']['content']",
                "time_key_exp": "json_text['data']['time']"
}