import re
import time
import string
import datetime
from dateutil.parser import parse
from Jsonabstract.default import TIME_KEYS,ALL_DATETIME_PATTERN_DICT,Month_Less_To_Full
from Jsonabstract.Common_abstract import Common_abstract


class GetTime(Common_abstract):
    def __init__(self,time_key_exp,time_key='',time_re_rule=''):
        super().__init__(key_exp=time_key_exp,key=time_key,re_rule=time_re_rule,KEYS=TIME_KEYS)

    def time_to_date(self,time_text):
        time_text = str(time_text)  # 统一为字符串类型
        if time_text == '':
            return ''
        if time_text.isdigit():  # 判断是否全为数字，从而确定是否为时间戳
            if len(time_text) == 10:  # 是否为秒时间戳
                time_local = time.localtime(int(time_text))
                dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
            elif len(time_text) == 13:  # 是否为毫秒时间戳
                time_local = time.localtime(int(time_text) / 1000)
                dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
            elif len(time_text) > 13:
                dt = parse(time_text)
                dt = dt.strftime("%Y-%m-%d %H:%M:%S")
            else:
                dt = ''
            return dt
        else:
            time_text = time_text.strip()
            new_time_text = ''
            date_format = '%Y-%m-%d %H:%M:%S'
            for date_format, re_rule in ALL_DATETIME_PATTERN_DICT.items():
                new_time_text = re.search(re_rule, time_text)
                if new_time_text:
                    new_time_text = new_time_text.group(1)
                    date_format = date_format
                    break
            time_text = new_time_text
            try:
                if date_format[0] in string.ascii_lowercase:
                    format = date_format[1:]
                    if ''.join([i if i in time_text else '' for i in ['前', '昨', '内', '刚刚', '今']]):
                        delta_word = re.findall("\D+", time_text)[0].strip()  # 获取表达式中的文字 如前天
                        if '时' in time_text and '分' in time_text:  # 判断时和分是否同时存在，存在则表示是今天 20时30分这种格式，将时和分替换为:，否则则是3分钟前这种格式,保持原样
                            sub_second_time = re.sub('秒', '', time_text)
                            last_time_text = re.sub('时|分', ':', sub_second_time)
                        else:
                            last_time_text = time_text
                        if delta_word and ':' in last_time_text:  # 处理今天 02:21,今天02：21：23，昨天02：21类似这种日期格式
                            len_colon = len(re.findall(':', last_time_text))
                            if len_colon == 1:  # 判断：的数量，如果为1则拼接
                                time_hour = f'{last_time_text.split(delta_word, 1)[1]}:00'
                            else:
                                time_hour = last_time_text.split(delta_word, 1)[1]
                            if '今天' in delta_word:
                                timestamp = time.time()
                            elif '昨天' in delta_word:
                                timestamp = time.time() - 60 * 60 * 24
                            elif '前天' in delta_word:
                                timestamp = time.time() - 60 * 60 * 24 * 2
                            else:
                                return
                            timearray = time.localtime(timestamp)
                            article_data = f"{time.strftime(format, timearray)} {time_hour}"
                        else:  # 处理5分钟前，10秒前，2个月前类似这种日期格式
                            # 获取表达式中的数字
                            delta_num = re.findall("\d+", time_text)
                            if delta_num:
                                delta_num = int(delta_num[0])
                            else:
                                delta_num = 1
                            units = {
                                "刚刚": 60,
                                "天内": delta_num * 24 * 60 * 60,
                                "秒前": delta_num,
                                "秒钟前": delta_num,
                                "秒鐘前": delta_num,
                                "分钟前": delta_num * 60,
                                "分鐘前": delta_num * 60,
                                'minutes ago':delta_num * 60,
                                "小时前": delta_num * 60 * 60,
                                "小時前": delta_num * 60 * 60,
                                'hour ago':delta_num * 60 * 60,
                                "天前": delta_num * 24 * 60 * 60,
                                '前天': 2 * 24 * 60 * 60,
                                '昨天': 24 * 60 * 60,
                                '今天': 60,
                                '周前': delta_num * 24 * 7 * 60 * 60,
                                "个月前": int(delta_num * 365.0 / 12) * 24 * 60 * 60,
                                "月前": int(delta_num * 365.0 / 12) * 24 * 60 * 60,
                                "年前": delta_num * 365 * 24 * 60 * 60,
                            }
                            delta_time = datetime.timedelta(seconds=units[delta_word])
                            article_data = (datetime.datetime.now() - delta_time).strftime(format)
                    else:
                        article_data = datetime.datetime.now().strftime(format)
                elif date_format[0] in string.ascii_uppercase:
                    format = date_format[1:]
                    sub_year_month_time = re.sub('年|月|/|\.', '-', time_text)
                    sub_second_time = re.sub('秒', '', sub_year_month_time)
                    sub_hour_minute_time = re.sub('时|分', ':', sub_second_time)
                    len_gang = len(re.findall('-', sub_year_month_time))
                    len_colon = len(re.findall(':', sub_hour_minute_time))
                    if len_colon == 0:
                        sub_day_time = re.sub('日 |日', '', sub_hour_minute_time, 1)
                    else:
                        sub_day_time = re.sub('日 |日', ' ', sub_hour_minute_time, 1)
                    currentYear = datetime.datetime.now().year
                    if len_gang == 1:
                        if not re.search('\d{4}', sub_day_time):  #姑且通过判断是否有连续四个数字来判断是否有年份
                            add_year_time = f'{currentYear}-{sub_day_time}'
                        else:
                            add_year_time = sub_day_time
                        # 比较转换的时间是否大于当前的时间
                        currentTime = int(time.time())
                        data_sj = time.strptime(add_year_time, format)  # 定义格式
                        time_int = int(time.mktime(data_sj))
                        if time_int > currentTime:
                            currentYear -= 1
                            sub_day_time = f'{currentYear}-{sub_day_time}'
                        else:
                            sub_day_time = add_year_time
                    elif len_gang == 2:
                        if_year = sub_day_time.split('-', 1)[0]
                        len_year = len(if_year)
                        if len_year == 2:
                            year = f'20{if_year}'
                            if int(year) > currentYear:
                                add_year_time = datetime.datetime.strptime(sub_day_time, "%d-%m-%Y")
                                article_data = add_year_time.strftime("%Y-%m-%d %H:%M:%S")
                                return article_data
                            else:
                                sub_day_time = f'20{sub_day_time}'
                    else:
                        sub_day_time = f"{datetime.datetime.now().strftime('%Y-%m-%d')} {sub_day_time}"
                    time_for = datetime.datetime.strptime(sub_day_time, format)
                    article_data = time_for.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    time_text = re.sub('时|分', ':', time_text)
                    eng_time_text = ''.join([re.sub(full, less, time_text) for full, less in Month_Less_To_Full.items() if full in time_text])
                    time_text = eng_time_text if eng_time_text else time_text
                    english_time_text = datetime.datetime.strptime(time_text, date_format)
                    article_data = english_time_text.strftime("%Y-%m-%d %H:%M:%S")
                return article_data
            except:
                return

    # #默认键抽取
    def default_key_abstract(self):
        values= list()
        for key,value in self.text_dict.items():
            if key in self.KEYS and (isinstance(value,str) or isinstance(value,int)):
                self.value = value
            elif isinstance(value,dict):
                for n_key,n_value in value.items():
                    if n_key in self.KEYS and (isinstance(n_value,str) or isinstance(n_value,int)):
                        self.value = n_value
                        break
            values.append(self.value)
        new_val = ""
        for val in values:
            if len(str(val)) > len(str(new_val)):
                new_val = val
        self.value = new_val

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
        date_time = self.time_to_date(self.value)
        return date_time