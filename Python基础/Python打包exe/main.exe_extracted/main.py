#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from tkinter import messagebox
print("这是一个弹出提示框")
messagebox.showinfo("提示","我是一个提示框")



# pyinstaller -F main.exe              //打包main.exe 生产不依赖环境可执行文件
# python pyinstxtractor.py test.exe    //解包main.exe
