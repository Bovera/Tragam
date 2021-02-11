#!/usr/bin/python3
title = input('Filename:\n')
fileFrom = open(title+'.md')
fileTo = open(title+'.tex','x')
fileTo.write('\\documentclass{article}\n\\usepackage{ctex}\n\\title{'+title+'}\n\\begin{document}\n\\maketitle\n')
lines = fileFrom.readlines()
for a in lines:
    if a[0:2] == '# ':
        a = a.replace('# ','\\section{')
        a = a.rstrip()
        a += '}\n'
    elif a[0:3] == '## ':
        a = a.replace('## ','\\subsection{')
        a = a.rstrip()
        a += '}\n'
    elif a[0:4] == '### ':
        a = a.replace('### ','\\subsubsection{')
        a = a.rstrip()
        a += '}\n'    
    fileTo.write(a)
fileTo.write('\\end{document}\n')
fileFrom.close()
fileTo.close()