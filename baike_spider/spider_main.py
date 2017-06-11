# coding: utf8
import url_manager import UrlManager
import html_downloader import HtmlDownloader
import html_parser import HtmlParser
import html_outputer import HtmlOutputer


class SpiderMain(object):

    # 初始化
    def __init__(self):
        self.urls = url_manager.UrlManager()#初始化url管理器
        self.downloader = html_downloader.HtmlDownloader()#下载器
        self.parser = html_parser.HtmlParser()#解析器
        self.outputer = html_outputer.HtmlOutputer()#输出器

    def craw(self,root_url):
        self.urls.add_new_url(root_url)# 将入口url添加进管理器
        #启动爬取的循环
        while self.urls.has_new_url():
            new_url = self.get_new_url()
            html_cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(new_url, html_cont)

if __name__=="__main__":
    root_url = "http://baike.baidu.com/view/21087.html"# 爬虫的入口url
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)# obj_spider的craw()方法启动爬虫
