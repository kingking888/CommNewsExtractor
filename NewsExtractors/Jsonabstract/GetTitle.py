from Jsonabstract.default import TITLE_KEYS
from Jsonabstract.Common_abstract import Common_abstract


class GetTitle(Common_abstract):
    def __init__(self,tit_key_exp,title_key='',tit_re_rule=''):
        super().__init__(key_exp=tit_key_exp,key=title_key,re_rule=tit_re_rule,KEYS=TITLE_KEYS)