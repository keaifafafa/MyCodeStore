#运用正则表达式来爬取歌单
import requests
import re

url = 'https://www.kugou.com/yy/rank/home/1-8888.html?from=homepage'

response = requests.get(url)
print(response)
data = response.text
print(len(data))
print(type(data))
#print(date)
content = 'i love u 1 i love 2 i love 3'
# result = re.findall('<i.*? 3',content,re.S)
# for i in result:
#     print(i)

result = re.findall('<li class.*?title="(.*?)".*?<a href="(.*?)".*?</li>',data,re.S)
print(result)
for i in result:
    print(i)




