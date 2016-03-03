from bs4 import BeautifulSoup
import requests
print("开始get页面")
#请求页面
url = 'http://www.avmoo.net/cn/movie/5e0h'
#header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
wb_data = requests.get(url)
if str(wb_data) == "<Response [200]>":
    #分析抓取地址
    Soup = BeautifulSoup(wb_data.text,'lxml')
    #av标题
    titles = Soup.select('body > div.container > h3')
    #av封面图
    images = Soup.select('body > div.container > div.row.movie > div.col-md-9.screencap > a > img')
    #av番号
    movie_ids = Soup.select('body > div.container > div.row.movie > div.col-md-3.info > p:nth-of-type(1) > span:nth-of-type(2)')
    #av发行商
    labels = Soup.select('body > div.container > div.row.movie > div.col-md-3.info > p:nth-of-type(7) > a')
    #av系列
    series = Soup.select('body > div.container > div.row.movie > div.col-md-3.info > p:nth-of-type(6) > a')
    #av类别 - 多内容
    genres = Soup.select('body > div.container > div.row.movie > div.col-md-3.info > p > span > a')
    #av演员 - 多内容
    players = Soup.select('#avatar-waterfall > a > span')
    #av播放截图 - 多内容
    simples = Soup.select('#sample-waterfall > a > div > img')

    print("设定完成,构建列表")

    #抓取并写入字典
    Genre = []
    Player =[]
    Simple =[]
    for genre in genres:
        Genre.append(genre.get_text())
    for player in players:
        Player.append(player.get_text())
    for simple in simples:
        Simple.append(simple.get('src'))

    print("列表构建完成,开始写入字典")

    for title,image,movie_id,serie,genre,player,simple in zip(titles,images,movie_ids,series,genres,players,simples):
        data = {
            'av标题':title.get_text(),
            'av封面图':image.get('src'),
            'av番号':movie_id.get_text(),
            'av系列':serie.get_text(),
            'av类别':Genre,
            'av演员':Player,
            'av播放截图':Simple
        }
        print(data)

    print("写入完成")
else:
    print("网址访问失败" + str(wb_data))