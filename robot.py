#/usr/bin/env python
#coding: utf8
import requests
import json
from random import randint
import httplib
import md5
import urllib
import random
import sys
from weather import *
reload(sys)
sys.setdefaultencoding('utf-8')

appid = 'XXXXXXXXXXXXXXXXXX' #你的appid
secretKey ='XXXXXXXXXXXXXXXXXXXX' #你的密钥
def get_turing_response(req=""):
    url = "http://www.tuling123.com/openapi/api"
    secretcode = "2a220b38970844309f6503db51674c54"
    response = requests.post(url=url, json={"key": secretcode, "info": req, "userid": 12345678})
    return json.loads(response.text)['text'] if response.status_code == 200 else ""

def get_qingyunke_response(req=""):
    url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg={}".format(req)
    response = requests.get(url=url)
    return json.loads(response.text)['content'] if response.status_code == 200 else ""

def is_chinese(uchar):
        """判断一个unicode是否是汉字"""
        if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
                return True
        else:
                return False


def get_dict_result(word):  
	httpClient = None
	myurl = '/api/trans/vip/translate'
	q = word
	q_url = urllib.quote(q.encode('utf-8'))
	if is_chinese(word):
		fromLang = 'zh'
		toLang = 'en'
	else:
		fromLang = 'auto'
		toLang = 'zh'
	salt = random.randint(32768, 65536)
	sign = appid+q+str(salt)+secretKey
	m1 = md5.new()
	m1.update(sign)
	sign = m1.hexdigest()
	myurl = myurl+'?appid='+appid+'&q='+ q_url+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
	try:
		httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
		httpClient.request('GET', myurl)
	 
		#response是HTTPResponse对象
		response = httpClient.getresponse()
		results = response.read()
		data = json.loads(results)
		data2 = data['trans_result']
	        return data2[0]['dst']
    	except Exception, e:
		print e
	finally:
		if httpClient:
			httpClient.close()
# 简单做下。后面慢慢来
def get_response_by_keyword(keyword):
    if '团建' in keyword:
        result = {"type": "image", "content": "3s9Dh5rYdP9QruoJ_M6tIYDnxLLdsQNCMxkY0L2FMi6HhMlNPlkA1-50xaE_imL7"}
    elif keyword in list(['北京','赤峰','丰台','荥阳','门头沟','郑州']):
        result = {"type": "text", "content": tuisongtianqi(keyword)}
    elif '关于' in keyword:
        items = [{"title": "关于我", "description":"瓜子仁", "picurl":"https://avatars3.githubusercontent.com/u/11911302?s=400&u=41f808a323894a0fde626957be47addd2a17bc4e&v=4", "url":"https://github.com/niguadage"},
                 ]
        result = {"type": "news", "content": items}
    else:
	word_result = get_dict_result(keyword)
        result = {"type": "text", "content": word_result}
#         result = {"type": "text", "content": "听不懂在说什么"}
    return result

if __name__ == '__main__':
    result = get_response_by_keyword("天气")
    print result
