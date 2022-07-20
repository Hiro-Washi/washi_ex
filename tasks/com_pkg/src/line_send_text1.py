#coding:UTF-8
#!/usr/bin/env python3
import requests, os
import rospy

def sendImg():
    url = "https://notify-api.line.me/api/notify"
    token = "P11NKOH4qMErOE8U0dV5eWdTcP3bFrjqwTy9fcNUkqQ"
    headers = {"Authorization" : "Bearer "+ token}
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
    sendMsg()
