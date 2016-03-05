from splinter import Browser
import time
a = 0
for i in range(100000):
    browser = Browser('firefox')
    url = 'http://adf.ly/1XoGv5/'
    browser.cookies.add({'Cookie':'__cfduid=d65fca672e4ed745194d2af98aabb8efe1457097429; FLYSESSID=84eae741895b01015a60a626a97468d73e5ad96d; adf1=24e38bdc2ec8454845bbb3746f1d0fbc; adf2=71e391e015735904abe1a112e3cfb7fa; __utma=255621336.866444478.1457097430.1457097430.1457097430.1; __utmb=255621336.0.10.1457097430; __utmc=255621336; __utmz=255621336.1457097430.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'})
    browser.visit(url)
    time.sleep(10)
    button = browser.find_by_id('skip_ad_button')
    button.click()
    window = browser.windows.current
    window.close()
    a = a+1
    print('完成'+ str(a) +'次请求')