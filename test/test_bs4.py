# coding:utf8

from bs4 import BeautifulSoup
import re

some_info="""
<a href="www.baidu.com/tieba"> baidu_news</a>
<a href="www.sina.com/yule"> sina_news</a>
<a href="www.meituan.com/waimai"> meituan_waimai</a>

<p class="title">
    阳光明媚的一天。
</p>
"""

soup = BeautifulSoup(some_info,'html.parser',from_encoding='utf-8')

print '获取所有链接'
links = soup.find_all('a')
for link in links:
     print link.name, link['href'], link.get_text()


print '获取yule的链接'
link_node = soup.find('a',href='www.sina.com/yule')
print link.name, link['href'], link.get_text()


print '正则匹配'
link_node = soup.find('a',href=re.compile(r"yule"))#加r是为了遇到反斜线的时候只加一个反斜线就可以了
print link_node.name, link_node['href'], link_node.get_text()


print '获取p段落文字'
p_node = soup.find('p',class_="title")
print p_node.name, p_node.get_text()# p_node['href']没有了，所以删掉
