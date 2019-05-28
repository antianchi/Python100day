#!/usr/bin/env python
# coding=UTF-8
#! python3
'''
@Author: atch
@Email: atc00@foxmail.com
@Date: 2019-05-28 09:13:44
@LastEditors: antch
@LastEditTime: 2019-05-28 09:16:49
@Description: 使用Python发送电子邮件.
'''

from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP


def main():
    sender='861710865@qq.com'
    receivers = ['atc00@foxmail.com']
    message = MIMEText('Python发送邮件','plain','utf-8')
    message['From'] = Header('小安','utf-8')
    message['To'] = Header('小安r', 'utf-8')
    # gypdwvllpdgbbejf
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.qq.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'gypdwvllpdgbbejf')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')

if __name__=='__main__':
    main()
