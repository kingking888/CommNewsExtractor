import re
from lxml import etree
from Jsonabstract.default import CONTENT_KEYS,USELESS_TAG,CLEAN_TAG
from Jsonabstract.Common_abstract import Common_abstract



class GetContent(Common_abstract):
    def __init__(self,con_key_exp,content_key='',con_re_rule=''):
        super().__init__(key_exp=con_key_exp, key=content_key, re_rule=con_re_rule, KEYS=CONTENT_KEYS)
        self.len_value = 0

    #默认抽取
    def default_abstract(self):
        for key,value in self.text_dict.items():
            if isinstance(value,str):
                len_value = len(value)
                if len_value > self.len_value:  #判断值的长度，谁长即姑且认为谁是正文内容
                    self.value = value
                    self.len_value = len_value

    def abstract(self,json_text):
        self.text_dict = json_text
        if self.key_expression:
            self.post_expression_abstarct()
        elif self.key:
            self.post_key_abstract()
        elif self.re_rule:
            self.re_abstrat()
        else:
            self.default_key_abstract()
            if not self.value:
                self.default_abstract()
        element = etree.HTML(self.value)
        etree.strip_elements(element, *USELESS_TAG)
        contents = ''.join([text.strip() for text in element.xpath('//text()')])
        content = ''.join([re.sub(tag,'',contents,re.S) for tag in CLEAN_TAG])
        return content