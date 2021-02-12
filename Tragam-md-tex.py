#!/usr/bin/python3
import os

# 打开文件
title = input("Filename:")
language = input("Need to use Chinese?(y/n)")
fileFrom = open(title+'.md')
fileTo = open(title+".tex","x")

# 撰写文件头
fileTo.write("\\documentclass{article}\n")
if language == 'y':
    fileTo.write("\\usepackage{ctex}\n")
lines = fileFrom.readlines()
count = len(lines)
num1 = 0
for num in range(0,count):
    get = lines[num]
    if get[0:2] == "# " :
        num1 += num1
        num2 = num
        get = get.replace("# ","")
        get = get.rstrip()
        title2 = get
if num1 == 1:
    fileTo.write("\\title{"+ title2 +"}\n\\begin{document}\n\\maketitle\n")
    del lines[num2]
else:
    fileTo.write("\\title{"+ title +"}\n\\begin{document}\n\\maketitle\n")

# 替换函数
def listFuc(par):
    global get
    if get[0:2] == par:
        get = get.replace(par,'\\item ')
def titleFuc(par):
    global get
    global num1
    muty = ""
    muty2 = ""
    for i in range(1,par):
        muty = muty + "#"
    if num1 == 1:    
        for i in range(3,par):
            muty2 = muty2 + "sub"
    else:
        for i in range(2,par):
            muty2 = muty2 + "sub"
    if get[0:par] == muty + " ":
        get = get.replace(muty + " ","\\" + muty2 + "section{")
        get = get.rstrip()
        get += '}\n'

# 执行替换
count = len(lines)
for num in range(0,count):
    get = lines[num]
    if not(num1 == 1):
        titleFuc(2)
    titleFuc(3)
    titleFuc(4)
    if num1 == 1:
        titleFuc(5)
    listFuc("+ ")
    listFuc("- ")
    listFuc("* ")
    lines[num] = get

# 写入替换
for get in lines:
    fileTo.write(get)
fileTo.write('\n\\end{document}\n')
fileFrom.close()
fileTo.close()

# 翻译成 PDF
transToPDF = input("Need to translate to PDF?(y/n)")
if transToPDF == 'y':
    os.system('pdflatex '+title+".tex")