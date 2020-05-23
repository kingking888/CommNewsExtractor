import json

class Clean_json_text():
    def __init__(self):
        pass

    def judge_text(self, json_text):
        if isinstance(json_text, dict):
            self.text_dict = json_text
        elif isinstance(json_text, str):
            self.text_dict = json.loads(json_text)
        elif isinstance(json_text, list):
            self.text_dict = json_text[0]
        else:
            return '传入文本格式不符'
        return self.text_dict

    def clean_json_text(self,JSONTEXT):
        text = self.judge_text(JSONTEXT)
        return text