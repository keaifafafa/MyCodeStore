import re##爬视频
import urllib,urllib2
# def geturllist():
# 	res=urllib2.urlopen('http://www.budejie.com/video/')
# 	html=res.read()
# 	print html
# geturllist()
def geturllist():
 
	req = urllib2.Request('http://www.budejie.com/video/');
	req.add_header('User-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)'
          ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Mobile '
          'Safari/537.36')
	res=urllib2.urlopen(req)
	html=res.read()
	reg=r'data-mp4="(.*?)">'
	urllist=re.findall(reg,html)
	for url in urllist:
		urllib.urlretrieve(url,'F:\\MP4/%s.mp4'%url.split('/')[-1])
 
geturllist()
