# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：    html_content_extractor.py
   Description :  通用HTML正文提取类
   Author :       Andy Zhong
   date：          2019/12/7
-------------------------------------------------
   Change Activity:
                   2019/12/7:
-------------------------------------------------
"""
__author__ = 'Andy Zhong'
import re
from extractors.settings import *

class HtmlContentExtractors(object):
    def __init__(self, language='zh'):
        self._content_start_pos = ''
        self._content_end_pos = ''
        self._content_center_pos = ''
        self._paragraphs = ''

    def get_contents(self, html):
        paragraphs = self.__del_html_tag(html, save_useful_tag=True).split('\n')

        # 统计连续n段的文本密度
        paragraph_lengths = [len(self.__del_html_tag(paragraph)) for paragraph in paragraphs]
        # paragraph_lengths = [len(paragraph.strip()) for paragraph in paragraphs]
        paragraph_block_lengths = [sum(paragraph_lengths[i : i + MAX_PARAGRAPH_DISTANCE]) for i in range(len(paragraph_lengths))]  # 连续n段段落长度的总和（段落块），如段落长度为[0,1,2,3,4] 则连续三段段落长度为[3,6,9,3,4]

        self._content_center_pos = content_start_pos = content_end_pos = paragraph_block_lengths.index(max(paragraph_block_lengths)) #文章的开始和结束位置默认在段落块文字最密集处
        min_paragraph_block_length = MIN_PARAGRAPH_LENGHT * MAX_PARAGRAPH_DISTANCE
        # 段落块长度大于最小段落块长度且数组没有越界，则看成在正文内。开始下标继续向上查找
        while content_start_pos > 0 and paragraph_block_lengths[content_start_pos] > min_paragraph_block_length:
            content_start_pos -= 1

        # 段落块长度大于最小段落块长度且数组没有越界，则看成在正文内。结束下标继续向下查找
        while content_end_pos < len(paragraph_block_lengths) and paragraph_block_lengths[content_end_pos] > min_paragraph_block_length:
            content_end_pos += 1

        # 处理多余的换行和空白符
        content = paragraphs[content_start_pos : content_end_pos]
        content = '\n'.join(content)
        content = self.__del_unnecessary_character(content)

        # 此处统计p标签内的文字数占总正文文字数的比例。超过一定阈值，则算为正文
        paragraphs_text_len = len(self.__del_html_tag(''.join(self.get_info(content, '<p.*?>(.*?)</p>'))))
        content_text_len = len(self.__del_html_tag(content))
        if content_text_len and content_text_len > MIN_COUNTENT_WORDS and ((paragraphs_text_len / content_text_len) > MIN_PARAGRAPH_AND_CONTENT_PROPORTION):
            self._content_start_pos = content_start_pos
            self._content_end_pos = content_end_pos
            self._paragraphs = paragraphs
            # print(content_start_pos, content_end_pos, self._content_center_pos)
            return content
        else:
            return ''

    def __del_html_tag(self, html, save_useful_tag=False):
        '''
        @summary:
        ---------
        @param html:
        @param save_useful_tag:保留有用的标签，如img和p标签
        ---------
        @result:
        '''
        html = self.__replace_str(html, r'(?i)<script(.|\n)*?</script>')  # (?i)忽略大小写
        html = self.__replace_str(html, r'(?i)<style(.|\n)*?</style>')
        html = self.__replace_str(html, r'<!--(.|\n)*?-->')
        html = self.__replace_str(html, r'(?!&[a-z]+=)&[a-z]+;?', ' ')  # 干掉&nbsp等无用的字符 但&xxx= 这种表示参数的除外

        if save_useful_tag:
            html = self.__replace_str(html, r'(?!{useful_tag})<(.|\n)+?>'.format(useful_tag='|'.join(USEFUL_TAG)))
        else:
            html = self.__replace_str(html, '<(.|\n)*?>')

        html = self.__replace_str(html, '[\f\r\t\v]')  # 将空格和换行符外的其他空白符去掉
        html = html.strip()
        return html


    def __replace_str(self, source_str, regex, replace_str=''):
        '''
        @summary: 替换字符串
        ---------
        @param source_str: 原字符串
        @param regex: 正则
        @param replace_str: 用什么来替换 默认为''
        ---------
        @result: 返回替换后的字符串
        '''
        str_info = re.compile(regex)
        return str_info.sub(replace_str, source_str)

    def __del_unnecessary_character(self, content):
        '''
        @summary: 去掉多余的换行和空格
        ---------
        @param content:
        ---------
        @result:
        '''
        content = content.strip()
        content = content[content.find('>') + 1:] if content.startswith('</') else content  # 去掉开头的结束符
        content = self.__replace_str(content, ' {2,}', '')  # 去掉超过一个的空格
        return self.__replace_str(content, '(?! )\s+', '\n')  # 非空格的空白符转换为回车


    def get_info(self ,html, regexs, allow_repeat=False, fetch_one=False, split=None):
        regexs = isinstance(regexs, str) and [regexs] or regexs
        _regexs = {}
        infos = []
        for regex in regexs:
            if regex == '':
                continue

            if regex not in _regexs.keys():
                _regexs[regex] = re.compile(regex, re.S)

            if fetch_one:
                infos = _regexs[regex].search(html)
                if infos:
                    infos = infos.groups()
                else:
                    continue
            else:
                infos = _regexs[regex].findall(str(html))

            if len(infos) > 0:
                break

        if fetch_one:
            infos = infos if infos else ('',)
            return infos if len(infos) > 1 else infos[0]
        else:
            infos = allow_repeat and infos or sorted(set(infos), key=infos.index)
            infos = split.join(infos) if split else infos
            return infos