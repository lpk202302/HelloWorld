# 导入模块
import requests
from bs4 import BeautifulSoup
from lxml import etree

# 发起网络请求
url = 'https://movie.douban.com/top250?start=25&filter='

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
}

urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i * 25)) for i in range(10)]
def get_first_title(list):
    try:
        return list[0].strip()
    except:
        return ''

count = 1
for url in urls:
    # print(url)
    req = requests.get(url=url, headers=headers)

    # print(req.status_code)

    html = etree.HTML(req.text)

    lis = html.xpath('//*[@id="content"]/div/div[1]/ol/li')

    # print(len(lis))

    for li in lis:
        title = get_first_title(li.xpath('./div/div[2]/div[1]/a/span[1]/text()'))
        src = get_first_title(li.xpath('./div/div[2]/div[1]/a/@href'))
        dictor = get_first_title(li.xpath('./div/div[2]/div[2]/p[1]/text()'))
        print(count, title, src, dictor)
        count += 1







