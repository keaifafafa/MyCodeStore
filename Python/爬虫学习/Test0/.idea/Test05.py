#爬取各大音乐网站的歌曲（初级）
import requests
#周杰伦的夜曲：https://webfs.yun.kugou.com/202005271921/1e184b474eb4e32ca2246d41f63157eb/part/0/961537/G140/M06/08/1D/LIcBAFuIK1OAch8fADbwlB1Fkjg764.mp3
url = ''#歌曲下载地址

#破解反爬机制
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4043.400'
}

response = requests.get(url,headers=headers)
print(response)
a = response

with open(r'C:\Users\发发\Desktop\新建文件夹\你好不好.m4a','wb')as file:
    file.write(a.content)