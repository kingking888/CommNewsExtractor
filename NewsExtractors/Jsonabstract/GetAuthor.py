import re
from Jsonabstract.default import AUTHOR_KEYS, AUTHOR_RE_RULES
from Jsonabstract.Common_abstract import Common_abstract


class GetAuthor(Common_abstract):
    def __init__(self, aut_key_exp, aut_key='', aut_re_rule=''):
        super().__init__(key_exp=aut_key_exp, key=aut_key, re_rule=aut_re_rule, KEYS=AUTHOR_KEYS)

    def default_re(self, content):
        for re_rule in AUTHOR_RE_RULES:
            author = re.search(re_rule, content)
            if author:
                self.value = author.group(1)
                break

    def abstract(self,JSONTEXT,content=None):
        self.text_dict = JSONTEXT
        if self.key_expression:
            self.post_expression_abstarct()
        elif self.key:
            self.post_key_abstract()
        elif self.re_rule:
            self.re_abstrat()
        else:
            self.default_key_abstract()
        if not self.value and content:
            self.default_re(content)
        return self.value
