#coding:UTF-8
#!/usr/bin/env python3
# Recieve a text/img, text -> name:token, content 
# (t/i/t&i)           img  -> name:token, img_name
#                                         shot_img
# /line_text_server lineServer 
#   t_or_i="",to_name"",content="",

import requests, yaml, rospy as rp, roslib
from com_pkg.srv import SendLine, SendLineResponse
file_path1 = roslib.packages.get_pkg_dir('com_pkg') + '/config/'
sys.path.insert(0, file_path1)
url = "https://notify-api.line.me/api/notify"

class LineTextServer():
    def __init__(self):
        rp.loginfo("execute < LineServer >")
        #rp.Service('/line_text_server', lineText, self.sendLineMsg)
        #rp.Service('/line_text_server', lineImg, self.sendLineImg)
        rp.Service('/line_text_server', lineServer, self.execute)

        self.yaml = 'NULL'
        self.to_list = []
        self.to_token = []

    def setFile(self, to_name_list):
        #with open(file_path1+file_name+".yaml", "r") as f
        #    self.yf = yaml.load(f) ## self.yaml file
        #pkg_path = roslib.packages.get_pkgdir(com_pkg)
        #rp.set_param("/config", line)
        with open(file_path1+"/send_line.yaml", "r") as f:
            self.yf = yaml.load(f)
        list_count = len(to_name)  ## list _count
        if to_name_list[0] == "all"
            self.to_list = self.yf["to"]["all"]
        else:
            list_count = len(to_address_list)
            for count in range(list_count):
                self.to_list.append(self.yaml['to'][to_address_list[count]])
                rospy.sleep(0.2)
        rp.loginfo(self.to_list)
        return self.to_list

    #def checkType(self):
        
    def sendMsg(self, message, to_token):
        token = to_token
        headers = {"Authorization" : "Bearer "+ token}
        msg = message
        pyload = {"message" : msg}
        rp = requests.post(url , headers = headers ,params=payload)

    def execute(self, req):
        try:
            self.to_token = self.set_file(req.to_name)
            msg = self.sendMsg(req.message, self.to_token)
            rp.loginfo("sent the message")
            
            return SendLineResponse(res = True)
        except rp.ROSInternalException:
            rp.logger("\n ~~~Interrupt~~~ ")
            return SendLineResponse(res = False)
            

if __name__ == '__main__':
    rp.init_node("line_text_server")
    ls = LineTextServer()
    rp.spin()
