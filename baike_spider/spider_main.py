# coding: utf8
import url_manager
import html_downloader
import html_parser
import html_outputer

'''
是爬虫总调度程序+入口程序
'''

class SpiderMain(object):

    # 初始化
    def __init__(self):
        self.urls = url_manager.UrlManager()#初始化url管理器
        self.downloader = html_downloader.HtmlDownloader()#下载器
        self.parser = html_parser.HtmlParser()#解析器
        self.outputer = html_outputer.HtmlOutputer()#输出器

    #craw()方法==>即调度程序
    def craw(self,root_url):
        count = 1 # count 用来记录当前爬取的是第几个 url
        self.urls.add_new_url(root_url)# 将入口url（即:root_url）添加进管理器
        #启动爬取的循环
        #当url管理器中有待爬取的url时，执行循环
        while self.urls.has_new_url():
            try:
                new_url = self.get_new_url() #获取待爬取的url
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url) #启动下载器来下载这个页面，结果存储到 html_cont 中
                new_urls, new_data = self.parser.parse(new_url, html_cont) #调用解析器解析数据
                #分别处理解析后的url（即：new_urls）和数据（即：new_data）
                self.urls.add_new_urls(new_urls) #将新的 url 补充进 url 管理器。注意此处是new_urls即批量的url
                self.outputer.collect_data(new_data) #收集数据

                if count == 1000:
                    break

                count = count+1
            except:
                print 'craw failed!'

        self.outputer.output_html()

if __name__=="__main__":
    root_url = "http://baike.baidu.com/view/21087.html"# 爬虫的入口url
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)# obj_spider的craw()方法启动爬虫
