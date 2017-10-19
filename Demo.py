import PrintHelper,Utils
import json,random,string,hashlib,base64

#用户绑定设备
#返回数据格式 {"OpenUserId":1,"Code":200,"Message":"成功"}
result = PrintHelper.userBind('设备编号','您系统的用户编号（自己定义）最好是数字')

# #获取设备状态
# 返回数据格式 {"State":0,"Code":200,"Message":"成功"}
result1 = PrintHelper.getServiceState('设备编号')

#打印内容
# 返回数据格式 {"TaskId":3949406,"Code":200,"Message":"成功"}
content = Utils.strToBase64('要打印的内容')
# 格式详见 https://github.com/systemxgl/dui-api 或 http://www.mstching.com/openapi.pdf
jsonContent="[{\"Alignment\":0,\"BaseText\":\"" + content + "\",\"Bold\":0,\"FontSize\":0,\"PrintType\":0}]"
result2 = PrintHelper.printContent('设备编号',jsonContent,0) #0改成用户设备绑定返回的OpenUserId即可

#获取任务状态
# 返回数据格式 {"State":1,"Code":200,"Message":"成功"}
result3 = PrintHelper.getPrintTaskState(0) #0改成任务编号即可
