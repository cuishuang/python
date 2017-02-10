#-*- coding: utf-8 -*- 
# 第一行必须有，否则报中文字符非ascii码错误
import urllib
import hashlib
from bs4 import BeautifulSoup
import re
import requests
#import sys
import imp,sys
import json
import random
#import MYSQLdb #还不支持python3,用pymysql
import pymysql

import sys

import time


db = pymysql.connect(user='root', passwd='root',host='localhost', db='bigdata',charset='utf8')  
#上面要是写password而不是passwd竟然会报错...
#print(db)

#使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()


 
# 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak
queryStr = 'http://api.map.baidu.com/geocoder/v2/?callback=renderReverse&location=39.983424,116.322987&output=xml&pois=1&ak=yourak'
 


imp.reload(sys)

def AutoApiTest(url, params):  # 动态获取URL和参数
    s = requests
    r = s.post("%s" % url, params) 
    try:
        data = r.json()  # 将返回的json字符串转为字典格式
        results = json.dumps(data, ensure_ascii=False).encode('utf8')
        print (results, r.status_code)
    except:
        print (r.text, r.status_code)

def getUrlSrc(url):   # 获取页面信息
    head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
    try:
        html = requests.get(url, headers=head)
        #html.encoding = 'gbk'#如果网页的字符编码为gbk,则取消这行注释,注释掉下一行;而如果网页编码为utf8,则就是现在这个样子
        html.encoding = 'utf8'
        return html.text
    except Exception:
        print ("无法打开网页")



url = "http://api.map.baidu.com/geocoder/v2/?"


#print('到此结束')


count = 0

while(count<400):




    a = random.randrange(10000,99999,1)


    c = random.choice([1,2,3])



    d = random.choice([3,4,5,6])

    lat = "121."+str(d)+str(a)
    lng = '31.'+str(c)+str(a)


   # print(lat,lng)



    urlDetail = "&location="+lng+","+lat+"&output=json&pois=1&ak=yourak"


    soupDetail = BeautifulSoup(getUrlSrc(url + urlDetail), "html.parser")

    
    data = json.loads(str(soupDetail))



    #print (data['result']['formatted_address'])
    myaddress = data['result']['formatted_address']
    

    #nowtime为当前时间,年月日时分秒形式

    nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
     
    

    sql = 'insert into address2(shaddress,createtime) values ("%s","%s") '%\
          (myaddress,nowtime)

   
    cursor.execute(sql)
    db.commit()
    
    print(myaddress)

    
    count = count + 1



  
