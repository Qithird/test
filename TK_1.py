#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 11:51
# @Author  : Py.qi
# @File    : TK_1.py
# @Software: PyCharm

from tkinter import *

class application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel=Label(self,text='hello world')
        self.helloLabel.pack()
        self.quitButton=Button(self,text='quit',command=self.quit)
        self.quitButton.pack()

app=application()
app.master.title('hello world')
app.mainloop()