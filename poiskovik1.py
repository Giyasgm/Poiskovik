import os


spisfile = []
spispapka = []


def predmetfile(func):
    def wrapper(path, name):
        func(path, name)
        q1 = [j for i in spisfile for j in i]

        if name in q1:
            print("Он тут")

    return wrapper


def predmetpapka(func):
    def wrapper(path, name):
        func(path, name)

        if name in spispapka:
            print("Он здесь")

    return wrapper


@predmetfile
def poiskfile(path, name, level=1):
    ol = os.listdir(path)
    for i in ol:
        if os.path.isdir(path+'\\'+i):
            poiskfile(path+'\\'+i, level+1)
        if ol not in spisfile:
            spisfile.append(ol)


@predmetpapka
def poiskpapka(path, name, level=1):
    ol = os.listdir(path)
    for i in ol:
        if os.path.isdir(path+'\\'+i):
            poiskpapka(path+'\\'+i, level+1)
        if "." not in i and i not in spispapka:
            spispapka.append(i)


poiskfile("D:\Гияс", "SynapseNT1.png")
poiskpapka("D:\Гияс", "5ф")
