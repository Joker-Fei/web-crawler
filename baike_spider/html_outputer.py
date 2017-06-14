# coding: utf8

'''
网页输出器
'''

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    #用于搜集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 用于将搜集到的数据写出到html文件中，打开文件就能看到搜集到的数据
    def output_html(self):
        #建立一个文件的输出对象
        fout = open('output.html', 'w')

        #输出一个 html 形式
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        #注意：python默认的编码是 ascii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()
