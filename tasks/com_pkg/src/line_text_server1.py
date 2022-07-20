#coding:UTF-8
#!/usr/bin/env python3
# Recieve a text/img, text -> name:token, content 
# (t/i/t&i)           img  -> name:token, img_name
#                                         shot_img
# /line_text_server lineServer 
#   t_or_i="",to_name"",content=""
#                                                          ,shot()
import requests, yaml, rospy as rp, roslib
from com_pkg.srv import lineText, lineTextResponse
file_path1 = roslib.packages.get_pkg_dir('com_pkg') + '/config/'
sys.path.insert(0, file_path1)
url = "https://notify-api.line.me/api/notify"

class LineServer():
    def __init__(self):
        rp.loginfo("execute < LineServer >")
        rp.Service('/line_text_server', lineText, self.sendLineMsg)
        rp.Service('/line_text_server', lineImg, self.sendLineImg)
        #rp.Service('/line_text_server', lineServer, self.execute)

        self.yaml = 'NULL'
        self.to_list = []
        self.to_token = []

    def setFile(self, """file_name,""" to_name_list):
        #with open(file_path1+file_name+".yaml", "r") as f
        #    self.yf = yaml.load(f) ## self.yaml file
        pkg_path = roslib.packages.get_pkgdir(com_pkg)
        rp.set_param("/config", line)

        f = open("/set_edu_map.yaml")
        location_dict = load(f)
        f.close()
        list_count = len(to_name)  ## list _count
        if to_name_list[0]

    def checkType(self):

    def setMsg(self, req):
        try:
            #self.to_address = self.loadFile(req.file_name, req.to_address)
            msg = sef.setMsg(req.)

            return lineTextResponse(res = True)
        except rp.ROSInternalException:
            rp.logger("!!Interrupt!!")
            return lineTextResponse(res = False)

    def setImg(self, req):
        try:
            #self.to_address = self.loadFile(req.file_name, req.to_address)
            msg = sef.setMsg(req.)

            return lineTextResponse(res = True)
        except rp.ROSInternalException:
            rp.logger("!!Interrupt!!")
            return lineTextResponse(res = False)

    def execute(self, req):
        try:
            self.to_token = self.set_file(req.to_name)
            msg = self.setMsg(req.)

        except rp.ROSInternalException:
            rp.logger("!!Interrupt!!")
            return lineTextResponse(res = False)

def sendImg():
    #url = "https://notify-api.line.me/api/notify"
    #token = "P11NKOH4qMErOE8U0dV5eWdTcP3bFrjqwTy9fcNUkqQ"
    token = ""
    headers = {"Authorization" : "Bearer "+ token}
# OAuthに限らずトークンを利用して認証する機構の一部としてのヘッダを使えるヘッダでトークンを送る API 
# https://datatracker.ietf.org/doc/html/rfc7235
    message = 'おいっ'
    payload = {"message" :  message}
    files = {"imageFile":open('~/Pictures/wallpaper/closingEyesMan3.jpg','rb')}
    #readBynaryFil
    post = requests.post(url ,headers = headers ,params=payload,files=files)
def sendMsg():
    url = "https://notify-api.line.me/api/notify"
    token = "P11NKOH4qMErOE8U0dV5eWdTcP3bFrjqwTy9fcNUkqQ"
    headers = {"Authorization" : "Bearer "+ token}
    message = 'おいっ！'
    payload = {"message" :  message}
    r = requests.post(url ,headers = headers ,params=payload)

if __name__ == '__main__':
    rp.init_node("line_server")
    ls = LineServer()
    rp.spin()
