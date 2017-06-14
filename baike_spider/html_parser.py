# coding: utf8
import urlparse
'''
网页解析器
'''
class HtmlParser(object):

    #此方法需要从 html_cont 解析出两个数据：1.新的url列表  2.数据
    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding= 'utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls,new_data



    def _get_new_urls(self,page_url, soup):
        new_urls = set()
        # /view/123.htm
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)# 将new_url按照page_url的格式配成新的url

            new_url.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url, soup):
        res_data = {}

        #url
        res_data['url'] = page_url

        #打开网页，查看网页数据结构
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1") # 根据网页结构爬取信息
        res_data['title'] = title_node.get_text() #将数据提取出来

        # <div class="lemma-summary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text() #将数据提取出来

        return absres_data
