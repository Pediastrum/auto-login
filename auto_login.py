import os
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#读取config.json以获取用户名密码
def read_config():
    with open(r"config.json") as json_file:
        config = json.load(json_file)
    return config

config = read_config()
Username = config["username"]
Password = config["password"]
Sleeptime = config["sleeptime"]

def ping(domain):
    response = os.system("ping " + domain)
    if response == 0:
        return True
    else:
        return False

while True:
    if ping('baidu.com') == False:
        #ping返回False，断网
        print("\n网络已断开，登录程序启动\n")
        driver = webdriver.Edge(executable_path='msedgedriver.exe')
        driver.get('http://172.16.253.3/')
        #打开登录网页
        UsernameBlock = driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[3]/div[8]/form/input[3]')
        PasswordBlock = driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[3]/div[8]/form/input[4]')
        #寻找用户名密码元素
        UsernameBlock.send_keys(Username)
        time.sleep(0.2)
        PasswordBlock.send_keys(Password)
        time.sleep(0.2)
        #登录
        PasswordBlock.send_keys(Keys.ENTER)
        time.sleep(1.75)
        driver.close()

    else:
        #ping返回True，未断网
        print('\n目前网络正常\n')
        time.sleep(Sleeptime)

