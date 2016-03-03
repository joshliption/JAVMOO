import requests
from tkinter import *

from bs4 import BeautifulSoup
import urllib.request
import re


#movie_links = []

movie_hrefs = []  #av详情地址
pic_srcs = []  #av缩略图地址


movie_id = []
movie_ids = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

movie_2c = "5d"
for i in movie_ids:
    movie_3c = movie_2c + i
    for x in movie_ids:
        movie_4c = movie_3c + x
        movie_id.append(movie_4c)
movie_id.reverse()
print("抓取ID准备完成")
s = ""
for a in movie_id:
    url = "http://www.avmoo.net/cn/movie/" + a
#url = "http://www.avmoo.net/cn/movie/5d00"
    header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
              }
    source_code = requests.get(url,header)
    print(source_code)
    if str(source_code) == "<Response [200]>":
        plain_text = source_code.text

        file = open("/Users/zhangchenhui/GitHub/JAVMOO/movie_pages/" + a + ".html","w")

        file.write(plain_text)

        movie_id.remove(a)

        print(str(source_code) + a + "页输出完成")
    else:
        print(a + "页面抓取失败")
        pass

print("完成")

#soup = BeautifulSoup(plain_text, "html.parser")

'''
#抓取av详情地址
movie_boxs = soup.find_all("a","movie-box")
for movie_link in movie_boxs:
    movie_links = movie_link.get('href')
    movie_hrefs.append(movie_links)
print(movie_hrefs)
'''

'''
#抓取每个av详情的链接
for movie_box in soup.find_all(href=re.compile("www.avmoo.net/cn/movie/")):
    movie_boxs = movie_box.get('href')
    movie_links.append(movie_boxs)
print(movie_links)
print("Done")
'''

'''
#抓取每个av缩略图链接
for pic_src in soup.find_all(src=re.compile("jp.netcdn.xyz")):
    pic_srcs = pic_src.get('src')
    pic_links.append(pic_srcs)
print(pic_links)
print("Done")
'''

# 抓取每个av的名字

# 抓取每个av的番号

# 抓取每个av的发布日期



'''
#抓取page页面内容
    file = open("/Users/zhangchenhui/Desktop/htmls/" + str(i) + ".html","w")
    file.write(plain_text)
    print("第" + str(i) + "页输出完成")
'''

'''

downloadlinks = []
Downloadlinks = []
print(Downloadlinks)

for download_link in downloadlinks:
    https = str("https:"+download_link)
    Downloadlinks.append(https)
print(Downloadlinks[0])
'''