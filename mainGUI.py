from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import os
from images import Images

class MainGui:
    folderPath = ""
    folderEndPath = ""
    sFolderPath = ""
    sFolderEndPath = ""
    files = []
    imgLbls = []
    window = None
    lbl_1 = None
    lbl_2 = None
    lbl_3 = None
    lbl_4 = None
    dirBtn = None
    convertBtn = None
    finishLbl = None
    isFinishPlased = False

    def __init__(self):
        self.files = []
        self.imgLbls = []
        self.folderPath = ""
        self.folderEndPath = ""
        self.sFolderPath = ""
        self.sFolderEndPath = ""
        self.window = Tk()
        self.lbl_1 = Label(self.window, text="Конвертер изображений", font=("Arial Bold", 25))
        self.lbl_2 = Label(self.window, text="Количество изображений в папке: " + str(len(self.files)), font=("Arial Bold", 10))
        self.lbl_3 = Label(self.window, text="Активный каталог: " + self.sFolderPath, font=("Arial Bold", 10))
        self.lbl_4 = Label(self.window, text="Каталог назначения: " + self.sFolderEndPath, font=("Arial Bold", 10))
        self.dirBtn = Button(text="Каталог исходный", command=self.openFolder, width=20)
        self.dirEndBtn = Button(text="Каталог назначения", command=self.openEndFolder, width=20)
        self.convertBtn = Button(text="Конвертировать", command=self.convertFolder)
        self.finishLbl = None
        self.isFinishPlased = False
    
    def openFolder(self):
        if self.isFinishPlased: self.finishLbl.destroy()
        self.folderPath = filedialog.askdirectory()
        self.files = os.listdir(self.folderPath)
        splArr = self.folderPath.split('/')
        self.sFolderPath = '.../' + splArr[-2] + '/' + splArr[-1] + '/'
        #print(self.files)
        self.updateLbls()
        print (self.folderPath)
    
    def openEndFolder(self):
        self.folderEndPath = filedialog.askdirectory()
        splArr = self.folderEndPath.split('/')
        self.sFolderEndPath = '.../' + splArr[-2] + '/' + splArr[-1] + '/'
        #print(self.files)
        self.updateLbls()
        
    
    def convertFolder(self):
        if self.isFinishPlased : self.finishLbl.destroy()
        i = Images(self.folderPath, self.folderEndPath)
        us = i.convertWebpToJpeg()
        if (us):
            if (self.isFinishPlased): self.finishLbl.destroy
            self.finishLbl = Label(self.window, text="Сконвертировано", font=("Arial Bold", 15), fg='#058503')
            self.finishLbl.place(x = 220, y = 270)
            self.isFinishPlased = True
        else:
            if (self.isFinishPlased): self.finishLbl.destroy
            self.finishLbl = Label(self.window, text="Невозможно сконвертировать", font=("Arial Bold", 15), fg='#bd0202')
            self.finishLbl.place(x = 160, y = 270)
            self.isFinishPlased = True

    def updateLbls(self):
        self.lbl_2.destroy()
        self.lbl_3.destroy()
        self.lbl_2 = Label(self.window, text="Количество изображений в папке: " + str(len(self.files)), font=("Arial Bold", 10))
        self.lbl_3 = Label(self.window, text="Активный каталог: " + self.sFolderPath, font=("Arial Bold", 10))
        self.lbl_4 = Label(self.window, text="Каталог назначения: " + self.sFolderEndPath, font=("Arial Bold", 10))
        self.lbl_2.place(x = 210, y = 150)
        self.lbl_3.place(x = 210, y = 180)
        self.lbl_4.place(x = 210, y = 210)
    
    def showWindow(self):
        self.window.geometry('600x400')
        self.window.title("MultiConverter")
        self.lbl_1.place(x = 120, y = 10)
        self.dirBtn.place(x = 230, y = 80)
        self.dirEndBtn.place(x = 230, y = 110)
        self.lbl_2.place(x = 210, y = 150)
        self.lbl_3.place(x = 210, y = 180)
        self.lbl_4.place(x = 210, y = 210)
        self.convertBtn.place(x = 250, y = 240)
        self.window.mainloop()
    

if __name__ == "__main__":
    el = MainGui()
    el.showWindow()

  

  

  