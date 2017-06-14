 # coding: utf8
import urllib2

'''
网页下载器
'''

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url) #请求 url 的内容

        if response.getcode() != 200:
            return None

        return response.read()
