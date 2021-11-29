import requests
import json
import time
# url="https://www.cnblogs.com/GODYCA/archive/2012/12/06/2804500.html"

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36*"
}

def getData(url):
    response=requests.get(url=url,headers=headers)
    data=response.text
    data=json.loads(data)

    print(data["subjects"])
    return data["subjects"]

def SavaIntoJson(data):
    date=time.strftime("%Y-%m-%d")
    with open(date+"电影排行榜","a",encoding='utf-8') as f:
        for index,key in enumerate(data):
            f.write(json.dumps(data[index],ensure_ascii=False,indent=4,separators=(",",":")))
            f.write(",")

def main():
    for i in range(10,20):
        # url = "https://steamstats.cn/api/steam/top?page="+str(i)+"&format=json&lang=zh-hans"
        # url="https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start="+str(i)//豆瓣
        # //boss 行业 data["zpData"]
        # url="https://www.zhipin.com/wapi/zpCommon/data/oldindustry.json"
        #图书
        url="https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start="+str(i)
        data=getData(url)
        SavaIntoJson(data)
main()