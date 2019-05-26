# -*- coding: utf-8 -*-
#! python3
"""
Author: antch
Email: atc00@foxmail.com

date: 2019/5/26 11.03
desc: GUI程序开发.

"""
import sys
import tkinter
import tkinter.messagebox


# reload(sys)
# sys.setdefaultencoding('utf8')


def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color,msg = ('red','Hello world') if flag else ('blue','Goodby world')
        label.config(text=msg,fg=color)
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示','确定要退出么？'):
            top.quit()
    
    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置创就大小
    top.geometry('240x160')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top,text='helllo wordld', font='Arial -32', fg='red')
    label.pack(expand=1)

    # chua创建一个转按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')

    # 开启著时间循环
    tkinter.mainloop()
    
if __name__ == "__main__":
    main()

