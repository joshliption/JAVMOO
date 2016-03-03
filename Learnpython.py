from bs4 import BeautifulSoup
with open("/Users/zhangchenhui/Desktop/ACY-017.html",'r') as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
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

    # print(series)
    # print(titles,images,movie_ids,series,genres,players,sep='\n------------\n')
'''
for title in titles:
    title.get_text()
    print(title.get_text())

for image in images:
    image.get('src')
    print(image.get('src'))

for movie_id in movie_ids:
    movie_id.get_text()
    print(movie_id.get_text())

for serie in series:
    serie.get_text()
    print(serie.get_text())

for genre in genres:
    genre.get_text()
    print(genre.get_text())

for player in players:
    player.get_text()
    print(player.get_text())

for simple in simples:
    simple.get('src')
    print(simple.get('src'))
'''
for simple in simples:
    simple.get('src')
    print(simple.get('src'))

for title,image,movie_id,label,serie,player,simple in zip(titles,images,movie_ids,labels,series,players,simples):
    data = {
        'title':title.get_text(),
        'image':image.get('src'),
        'movie_id':movie_id.get_text(),
        'label':label.get_text(),
        'serie':serie.get_text(),
        'genre':genre.get_text(),
        'player':player.get_text(),
        'simple':simple.get('src')
    }
    print(data)

'''
for title,image,movie_id,serie,genre,player in zip(titles,images,movie_ids,series,genres,players):
    data = \
    {
        'title': title.get_text(),
        'image': image.get('src'),
        'movie_id': movie_id.get_text(),
        #'time':time.get_text(),
        'serie': serie.get_text(),
        'genre': genre.get_text(),
        'player': player.get_text()
    }
    print(data)
'''
'''
#avatar-waterfall > a > span
#avatar-waterfall > a > span
body > div.container > div.row.movie > div.col-md-3.info > p:nth-child(1) > span:nth-child(2)
body > div.container > div.row.movie > div.col-md-9.screencap > a > img
body > div.container > div.row.movie > div.col-md-3.info > p:nth-child(1) > span:nth-child(2)
body > div.container > div.row.movie > div.col-md-3.info > p:nth-child(2) > span
body > div.container > div.row.movie > div.col-md-3.info > p:nth-child(3)
body > div.container > div.row.movie > div.col-md-3.info > p:nth-child(6) > a
body > div.container > div.row.movie > div.col-md-3.info > p:nth-child(8) > span:nth-child(1) > a
'''