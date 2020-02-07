#!python3
#coding:utf-8
import json, sys, requests

import warnings
warnings.filterwarnings("ignore")
reload(sys)
sys.setdefaultencoding('utf-8')



 
def tuisongtianqi(position):
	#下载天气JSON
	weatherJsonUrl = "http://wthrcdn.etouch.cn/weather_mini?city=%s"%position
	response = requests.get(weatherJsonUrl)
	try:
		response.raise_for_status()
	except:
		print("网址请求出错")
		
	#将json文件格式导入成python的格式
	weatherData = json.loads(response.content)
	 
	#以好看的形式打印字典与列表表格
	#import pprint
	#pprint.pprint(weatherData)
	 
	w = weatherData['data']
	title = w['city'] + "天气预报"
	
	content = "%s天气"%position 
	#日期
	date_a = []
	#最高温与最低温
	highTemp = []
	lowTemp = []
	#天气
	weather = []
	#风向
	fengxiang = []
	#风力
	fengli = []
	#进行五天的天气遍历
	for i in range(len(w['forecast'])):
		date_a.append(w['forecast'][i]['date'])
		highTemp.append(w['forecast'][i]['high'])
		lowTemp.append(w['forecast'][i]['low'])
		weather.append(w['forecast'][i]['type'])
		fengxiang.append(w['forecast'][i]['fengxiang'])
		fengli.append(w['forecast'][i]['fengli'])
		#输出
		content = content + "\n\n" +  "日期：" + date_a[i] + "\n" + "\t温度：最" + lowTemp[i] + '~最' + highTemp[i] + '.'+ "\n" + "\t天气：" + weather[i] + "\n" + "\t风向：" + fengxiang[i]
	content = content + "\n" +  "今日着装：" + w['ganmao'] + "\n" + "当前温度：" + w['wendu'] + "℃" + "\n" 

	

	
	return content













