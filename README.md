# CommNewsExtractor

一.

A.版本：

    version_1.5

B.环境：

    python >= 3.7

二.功能：

    通用文章提取，正文，标题，时间，作者，图片，音视频，联系方式等

三.API说明：

        文件：AutoExtractors.py
        1.文章标题提取：get_title()
        2.文章作者提取：get_author()
        3.文章发布时间提取：get_public_time()
        4.文章邮箱提取：get_email()
        5.文章手机提取：get_phone()
        6.固定电话提取：get_telephone()
        7.文章url链接提取：get_url()
        8.html的IP提取：get_ip()
        9.身份证号码提取：get_idcard()
        10.文件提取：get_file()
        11.图片提取：get_image()
        12.视频提取：get_video()
        13.文章正文提取：get_content()
        14.新闻通用提取：get_all()

四.使用方式：

A.下载资源并安装环境

    git clone https://github.com/kingking888/CommNewsExtractor.git

    cd 到CommNewsExtractor目录下的requirements.txt同级别目录

    pip install -r requirements.txt

B.你的爬虫代码

'''
    
    import json, urllib3
    import requests
    from extractors.AutoExtractors import *
    from Jsonabstract.Json_abstract import Json_abstract
    from tools.automatic_detect import automatic_detect
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    
    class NewsExtract(object):
        def __init__(self):
            """
            已测试网站
            """
            # http://www.chinanews.com/
            self.url = "http://www.chinanews.com/gn/2020/05-23/9192614.shtml"
            # https://www.hao123.com/
            # self.url = "https://www.hao123.com/mid?from=shoubai&key=9412104569053922697&type=rec"
            # https://news.sina.com.cn/
            # self.url = "https://news.sina.com.cn/c/2019-12-10/doc-iihnzahi6563166.shtml"
            # http://www.sohu.com/
            # self.url = "http://www.sohu.com/a/359537759_114988?_f=index_chan08news_6"
            # https://news.qq.com/
            # self.url = "https://new.qq.com/omn/PEG20191/PEG2019121000975400.html"
            # https://news.163.com/
            # self.url = "https://news.163.com/19/1210/20/F02GT6270001899O.html"
            # http://news.ifeng.com/
            # self.url = "https://news.ifeng.com/c/7sIDPyRWK36"
            # http://www.xinhuanet.com/
            # self.url = "http://www.xinhuanet.com/gangao/2019-12/10/c_1125331339.htm"
            # http://env.people.com.cn
            # self.url = "http://env.people.com.cn/n1/2019/1210/c1010-31498499.html"
            # http://news.cctv.com/
            # self.url = "http://news.cctv.com/2019/12/10/ARTIOqy9gwiHXKlH5NWHCPPo191210.shtml?spm=C94212.P4YnMod9m2uD.ENPMkWvfnaiV.16"
            # https://www.huanqiu.com/
            # self.url = "https://opinion.huanqiu.com/article/9CaKrnKog6X"
            # http://news.baidu.com/
            # self.url = "http://news.cctv.com/2019/12/10/ARTISVPiNSCB6N4xWZjRPkNV191210.shtml"
            # http://www.cankaoxiaoxi.com
            # self.url = "http://www.cankaoxiaoxi.com/china/20191210/2397383.shtml"
            # https://www.thepaper.cn/
            # self.url = "https://www.thepaper.cn/newsDetail_forward_5198726"
            # http://www.takungpao.com/
            # self.url = "http://www.takungpao.com/news/232109/2019/1209/387560.html"
            # http://www.stnn.cc/
            # self.url = "http://news.stnn.cc/hongkong/2019/1210/697580.shtml"
            # Json---url
            # self.url = "http://www.zhwhg.com/api/article/read?id=1099"
    
            self.headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
            }
            self.key_dict = js_key_dict
            self.Json_abstract = Json_abstract()
    
        def start_requests(self):
            html_encoding = automatic_detect(self.url)
            print(html_encoding)
            res = requests.get(url=self.url, headers=self.headers, timeout=5, verify=False)
            if res.status_code == 200:
                try:
                    if "www.chinanews.com" in self.url:
                        res.encoding = "utf-8"
                    else:
                        res.encoding = html_encoding
                    html_content = res.text
                    if html_content:
                        return html_content
                except Exception as e:
                    # print(e)
                    pass
    
        def judge_if_json(self, html_content):
            if html_content:
                try:
                    json_html = json.loads(html_content)
                    print("This is Json Html")
                    return json_html
                except Exception as e:
                    # print(e)
                    pass
    
        def html_extract(self, html_content):
            # tag=0 正文内容是不带标签，tag=1正文内容是带标签
            result = SupperAutoExtract().get_all(html_content, tag=0)
            return result
    
        def run(self):
            html_content = self.start_requests()
            json_html = self.judge_if_json(html_content)
            if json_html:
                result = self.Json_abstract.all_abstract(json_html, key_exp_dict=self.key_dict)
            else:
                result = self.html_extract(html_content)
            print(result)
    
    
    if __name__ == '__main__':
        ne = NewsExtract()
        ne.run()
'''





五.本项目参考和借助项目：

    1.https://github.com/kingname/GeneralNewsExtractor

    2.https://github.com/striver-ing/distributed-spider

    3.https://github.com/codelucas/newspaper

    4.https://github.com/mozilla/readability

    5.https://github.com/aaronsw/html2text
    
    真诚感谢以上项目的开源作者，致敬!
 
六.欢迎完善项目，star和提issue

    ![image](https://user-images.githubusercontent.com/44130236/226170071-49ca4703-a611-4fce-b008-2e8f70138e51.png)

    
七.声明：

有关资源均来自网络收集与网友提供，任何涉及商业盈利目的的均不得使用，否则产生的一切后果将由您自己承担！

本项目资源仅供个人学习交流、测试使用。

所有内容请在下载后24小时内删除，禁止非法恶意传播，不对任何下载或转载者造成的危害负任何法律责任！

请不要将本项目的资源用于其他用途，所产生的后果我们概不负责！

如果本项目存在的内容对您和您的利益产生损害，请立即私信我们，将在最短时间内对其做出删除处理。
