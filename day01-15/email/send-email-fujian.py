#!/usr/bin/env python
# coding=UTF-8
#! python3
''''

Author: atch
Email: atc00@foxmail.com
Date: 2019-05-28 09:47:19
LastEditors: antch
LastEditTime: 2019-05-28 09:47:19
Description: 发送带附件的邮件.

'''

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib

def main():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()

    # 创建文本内容
    text_content = MIMEText('附件中有本月数据请查收', 'plain', 'utf-8')
    message['Subject'] = Header('本月数据', 'utf-8')
    # 将文本内容添加到邮件消息对象中
    message.attach(text_content)
    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('1.jpg','rb') as f :
        img = MIMEImage(f.read())
        
        img['Content-Type'] = 'image/*'
        img['Content-Disposition'] = 'attachment; filename=1.jpg'
        message.attach(img)
    
    # 创建 SMTP对象
    smtper = SMTP('smtp.qq.com')
    sender='861710865@qq.com'
    receivers = ['atc00@foxmail.com']
 
    message['From'] = Header('小安','utf-8')
    message['To'] = Header('小安r', 'utf-8')
    # gypdwvllpdgbbejf
    message['Subject'] = Header('示例代码实验邮件携带附件', 'utf-8')
    
    # 请自行修改下面的登录口令
    smtper.login(sender, 'gypdwvllpdgbbejf')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')

if __name__=='__main__':
    main()


