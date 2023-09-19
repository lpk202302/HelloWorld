import requests
from bs4 import BeautifulSoup
from lxml import etree

url = 'https://movie.douban.com/subject/1291560/comments?status=P'

headers = {'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62'
           }

req = requests.get(url=url, headers=headers)

print(req.status_code)

# print(req.text)

bs = BeautifulSoup(req.text, 'lxml')
short_print = bs.findAll('span', 'short')

# print(short_print)
short = []
for i in short_print:
    short.append(i.text)

# 列表生成式  和上面三行代码作用一致
# short = [i.text for i in short_print]

print(len(short))
print(short)

# html = etree.HTML(req.text)
#
# divs = html.xpath('//*[@id="comments"]/div[10]')
# print(len(divs))
# count = 1
# def get_first_code(list):
#     return list[0]
#
# for div in divs:
#     short_print = get_first_code(div.xpath('./div[2]/p/span/text()'))
#     print('第' + str(count) + '条短评:', short_print)
#     count += 1
