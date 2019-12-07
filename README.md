# CommNewsExtractor

一.版本：version_1.0

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
        14.新闻内容提取：get_all()

四：使用方式：

你的爬虫代码

    import requests

    from extractors.AutoExtractors import *

    class NewsExtract(object):

        def __init__(self):
            # self.url = "http://dy.163.com/v2/article/detail/EVQC8LOO0514D3UH.html"
            self.url = "http://www.chinanews.com/gn/2019/12-07/9027657.shtml"
            self.headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
            }

        def start_requests(self):
            res = requests.get(url=self.url,headers=self.headers,timeout=5,verify=False)
            if res.status_code == 200:
                res.encoding = "UTF-8"
                html_content = res.text
                if html_content and len(html_content) > 10 and re.search(r"[\u4E00-\u9FA5]{5,20}",html_content):
                    return html_content
                return None

        def html_extract(self, html_content):
            <!--单独功能提取 -->
            # title = SuperAutoExtract().get_title(html_content)
            # return title

            # author = SuperAutoExtract().get_author(html_content)
            # # return author

            # publish_time = SuperAutoExtract().get_public_time(html_content)
            # return publish_time
            
            # email = SuperAutoExtract().get_email(html_content)
            # return email
            
            # url = SuperAutoExtract().get_url(html_content)
            # return url
            
            # file = SuperAutoExtract().get_file(html_content)
            # return file
            
            # image = SuperAutoExtract().get_image(html_content)
            # return image
            #
            # video = SuperAutoExtract().get_video(html_content)
            # # return video


            <!-- 新闻通用提取 -->
            result = SuperAutoExtract().get_all(html_content)
            return result

        def run(self):
            html_content = self.start_requests()
            result = self.html_extract(html_content)
            print(result)


    if __name__ == '__main__':
        ne = NewsExtract()
        ne.run()


五.本项目参考和借助项目：

    1.https://github.com/kingname/GeneralNewsExtractor
    2.https://github.com/striver-ing/distributed-spider
    3.https://github.com/codelucas/newspaper
    4.https://github.com/mozilla/readability
    5.https://github.com/aaronsw/html2text
    
    真诚感谢以上项目的开源作者，致敬!
 
六.欢迎完善项目，star和提issue

    微信：zhongyiping168
    QQ: 184108270

    
七.声明：
有关资源均来自网络收集与网友提供，任何涉及商业盈利目的的均不得使用，否则产生的一切后果将由您自己承担！
本项目资源仅供个人学习交流、测试使用。
所有内容请在下载后24小时内删除，禁止非法恶意传播，不对任何下载或转载者造成的危害负任何法律责任！
请不要将本项目的资源用于其他用途，所产生的后果我们概不负责！
如果本项目存在的内容对您和您的利益产生损害，请立即私信我们，将在最短时间内对其做出删除处理。