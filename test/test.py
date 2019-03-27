#encoding : gbk
import requests
from urllib.parse import urlencode
from urllib.parse import quote,unquote
s=requests.session()
s.encoding='gbk'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
         'Upgrade-Insecure-Requests':'1',
         'Referer':'http://search.people.com.cn/cnpeople/news/getNewsResult.jsp',
         'Host':'search.people.com.cn',
         'Origin':'http://search.people.com.cn',
         'Cookie':'JSESSIONID=F66909D27D1DB2572C59D91211ABE0D0; wdcid=1f4169fcbc59ce94; sso_c=0',
         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
         'Accept-Encoding':'gzip, deflate, sdch',
         'Accept-Language':'zh-CN,zh;q=0.8',
         'Cache-Control':'max-age=0'
         }
url='http://search.people.com.cn/cnpeople/news/getNewsResult.jsp'
posturl='http://search.people.com.cn/cnpeople/search.do'

formdata={'siteName':'news',
'pageNum':'1',
'keyword':'b',
'facetFlag':'null',
'nodeType':'belongsId',
'nodeId':'0',
'pageCode':'',
'originName':''}

page=s.post(posturl,data=formdata,headers=headers)

page=s.get(url,headers=headers)
print(page.text)
