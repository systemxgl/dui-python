import json,random,string,hashlib,base64

from urllib import request,parse
import sys,urllib,time,datetime
import PrintConfig
#发送post请求
def sendPost(url,data):
    result = ''
    headers = {'Content-Type':'application/json;charset=utf-8'}
    # data 不支持传string 需改成 bytes
    data = json.dumps(data).encode('utf-8')
    req = request.Request(url=url, data=data, headers=headers)
    try:
        response = request.urlopen(req)
        result = response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        result = e.reason
    return result
#创建通用请求参数
def createParams():
    nonce = getNonce()
    timestamp = getTimestamp()
    signStr = signatureString(PrintConfig.appSecret,timestamp,nonce)
    return '?appid={0}&nonce={1}&timestamp={2}&signature={3}'.format(PrintConfig.appId,nonce,timestamp,signStr)

#获取随机字符串
def getNonce():
    return ''.join(random.sample(string.digits, 9))

#获取时间戳
def getTimestamp():
    return str(int(time.mktime(datetime.datetime.now().timetuple())))

#sha1加密
def signatureString(appSecret,timestamp,nonce):
    arrTmp = [appSecret,timestamp,nonce]
    arrTmp.sort()
    strTmp = ''.join(arrTmp)
    sha1 = hashlib.sha1()
    sha1.update(strTmp.encode('utf-8'))
    return sha1.hexdigest().lower()

#字符串转base64
def strToBase64(content):
   return str(base64.b64encode(content.encode('GBK')),'GBK')

