import io,sys
import json
import urllib.parse
import jsonpath   #re xpath
import requests
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding="gb18030")

#https://www.duitang.com/napi/blog/list/by_search/?kw=%E7%BE%8E%E5%A5%B3&start=24
#https://www.duitang.com/napi/blog/list/by_search/?kw=%E7%BE%8E%E5%A5%B3&start=48
#https://www.duitang.com/napi/blog/list/by_search/?kw=%E5%B8%85%E5%93%A5&start=120帅哥头像
#https://www.duitang.com/napi/blog/list/by_search/?kw=%E5%B8%85%E5%93%A5&type&start=24

url = 'https://www.duitang.com/napi/blog/list/by_search/?kw=%E7%BE%8E%E5%A5%B3&start=24'
num = 1

res = requests.get(url) #浏览器
we_data = res.text

#类型转换
html = json.loads(we_data)
photos = jsonpath.jsonpath(html,'$..path')
print(photos)

for i in photos:
        a = requests.get(i)
        with open(r'C:\Users\发发\Desktop\测试4\{}.jpg'.format(num),'wb')as f:
            f.write(a.content)
            num += 1


