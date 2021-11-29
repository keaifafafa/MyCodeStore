#爬取酷狗音乐歌单数据
#运用的正则表达式

import requests
import re
url = 'https://www.kugou.com/yy/rank/home/1-8888.html?from=rank'

response = requests.get(url)
date = response.text

select = re.findall('<li class=" " title="(.*?)".*?<a href="(.*?)".*?</li>',date,re.S)
for i in select:
    print(i)








