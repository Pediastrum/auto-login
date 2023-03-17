# auto-login

一个用于挂在后台自动登录安徽大学校园网的python程序，基于selenium
适合无人值守情况下使用，如希望保持宿舍中设备持续在线以维持远程连接等。

本程序开发环境为python==3.8

# 使用方法

本程序需要edge浏览器及其驱动，可以在edge://version/查看当前edge版本，
访问https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
以下载适合你edge版本的driver，并将压缩包中的msedgedriver.exe解压到程序主目录。

在config.json中输入你登录校园网时使用的用户名及密码。
