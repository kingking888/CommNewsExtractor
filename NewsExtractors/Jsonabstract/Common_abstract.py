import re
import json

class Common_abstract():
    def __init__(self,key_exp,key,re_rule,KEYS):
        self.value = ''
        self.text_dict = {}
        self.key = key
        self.re_rule = re_rule
        self.key_expression = key_exp
        self.KEYS = KEYS

    # #默认键抽取
    def default_key_abstract(self):
        values= list()
        for key,value in self.text_dict.items():
            if key in self.KEYS and isinstance(value,str):
                self.value = value
            elif isinstance(value,dict):
                for n_key,n_value in value.items():
                    if n_key in self.KEYS and isinstance(n_value,str):
                        self.value = n_value
                        break
            values.append(self.value)
        new_val = ""
        for val in values:
            if len(val) > len(new_val):
                new_val = val
        self.value = new_val


    # 正则抽取
    def re_abstrat(self):
        text_str = json.dumps(self.text_dict)
        re_value = re.search(self.re_rule,text_str,re.S)
        if re_value:
            self.value = re_value.group(1)

    # 传键抽取，内容没有在嵌套的情况下
    def post_key_abstract(self):
        self.value = self.text_dict[self.key]

    #使用表达式来抽取
    def post_expression_abstarct(self):
        get_value_code_format = '''
def exec_get_value(json_text):
    value = {}
    return value
'''
        exec(get_value_code_format.format(self.key_expression))
        get_value_func = locals()['exec_get_value']
        self.value = get_value_func(self.text_dict)


    def abstract(self,JSONTEXT):
        self.text_dict = JSONTEXT
        if self.key_expression:
            self.post_expression_abstarct()
        elif self.key:
            self.post_key_abstract()
        elif self.re_rule:
            self.re_abstrat()
        else:
            self.default_key_abstract()
        return self.value