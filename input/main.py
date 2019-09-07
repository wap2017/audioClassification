#!/usr/bin/python
import itchat, time
from itchat.content import *


a = 6

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    global a
    print(msg.fileName)
    msg.download("do"+str(a)+".mp3")
    a += 1
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

    # itchat.send_msg(m, msg.fromUserName)


# itchat.auto_login(enableCmdQR=0, hotReload=True) # 如果是在window上或者有可视化界面的ubuntu系统上，可以用这个
itchat.auto_login(enableCmdQR=0, hotReload=True)  # enableCmdQR=1是在控制台输出微信登录二维码
itchat.run()