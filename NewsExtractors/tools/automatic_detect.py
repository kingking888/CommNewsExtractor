import chardet  # 字符集检测
import urllib.request


# 自动获取网站解码方式
def automatic_detect(url):
    content = urllib.request.urlopen(url).read()
    result = chardet.detect(content)
    encoding = result['encoding']
    return encoding
