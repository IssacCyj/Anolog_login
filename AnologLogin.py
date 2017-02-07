# -*-coding:utf8-*-
import  requests
from lxml import etree
import re
import time
import sys
from PIL import Image
#
# reload(sys)
# sys.setdefaultencoding("utf-8")
# hea = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 '
#                     '(KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}



def login():
    # capture the captcha
    url1 ='http://login.weibo.cn/login/?ns=1&revalid=2&backURL=http%3A%2F%2Fweibo.cn%2F&' \
          'backTitle=%CE%A2%B2%A9&vt='
    pic = s.get(url1).content
    picurl1 = re.findall(r'<br/><img src="(.*?)" alt="',pic,re.S)
    picurl = ''.join(picurl1)
    picContent = s.get(picurl)
    #show the captcha and input manually
    y = open('captcha.gif','wb')
    y.write(picContent.content)
    y.close()
    i = Image.open('yzm.gif').show()
    yzm = raw_input('input yzm:')
    #analog log in
        # get info in the sheet that need to be posted
    vk = ''.join(re.findall('name="vk" value="(.*?)" />',pic))
    capId = ''.join(re.findall('name="capId" value="(.*?)" />',pic))
    password = ''.join(re.findall('<input type="password" name="(.*?)" size',pic))
    #package capture(using chrome directly)
    data = {
        "mobile":'13070111636',
        password:'Aptx-4869',
        'code':yzm,
        #'remember':'on',
        'backURL':'http%3A%2F%2Fweibo.cn%2F',
        'backTitle':'手机新浪网',
        'tryCount':'',
        'vk':vk,
        'capId':capId,
        'submit':'登录'
    }
    page = s.post(url1,data=data)
    #content after logging in
    page1 = s.get('http://weibo.cn/?vt=4')
    print page1.content


if __name__ == '__main__':
    s = requests.session()
    login()









