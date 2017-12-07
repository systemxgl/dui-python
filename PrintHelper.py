
import PrintConfig
from Utils import sendPost,createParams

#用户设备绑定
#uuid:设备编号
#userId:与对对机平台关联的用户唯一标示（你自己系统定义的）
def userBind(uuid,userId):
    url = PrintConfig.baseUrl +'/home/userbind'+createParams()
    data = {
        'Uuid':uuid,
        'UserId':userId
    }
    return sendPost(url,data)

#获取设备状态
#uuid:设备编号
def getServiceState(uuid):
    url = PrintConfig.baseUrl+'/home/getdevicestate'+createParams()
    data = {
        'Uuid':uuid
    }
    return sendPost(url, data)

#打印内容
def printContent(uuid,content,openUserId):
    url = PrintConfig.baseUrl+'/home/printcontent2'+createParams()
    data = {
        'Uuid':uuid,
        'PrintContent':content,
        'OpenUserId':openUserId
    }
    return sendPost(url,data)
#打印网页信息
def printHtmlContent(uuid,printUrl,openUserId):
    url = PrintConfig.baseUrl + '/home/printhtmlcontent' + createParams()
    data = {
        'Uuid': uuid,
        'PrintUrl':printUrl,
        'OpenUserId': openUserId
    }
    return sendPost(url, data)
#获取任务状态
def getPrintTaskState(taskId):
    url = PrintConfig.baseUrl + '/home/getprinttaskstate' + createParams()
    data = {
        'TaskId': taskId
    }
    return sendPost(url, data)
