import os


spisok = []
a = 0


def poisk(path, name, level=1):
    global a
    if name in os.listdir(path):
        print(spisok[-1])
        a = 1
    for i in os.listdir(path):
        if a == 1:
            break
        if os.path.isdir(path+'\\'+i):
            spisok.append(path + '\\' + i)
            poisk(path + '\\' + i, name, level + 1)


poisk("D:\Гияс", "Текст5.docx")
