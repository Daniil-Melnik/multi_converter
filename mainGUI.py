from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import os
from images import Images

class MainGui:
    folderPath = ""
    files = []
    window = None
    lbl_1 = None
    lbl_2 = None
    dirBtn = None

    def __init__(self):
        self.files = []
        self.folderPath = ""
        self.window = Tk()
        self.lbl_1 = Label(self.window, text="Конвертер изображений", font=("Arial Bold", 35))
        self.lbl_2 = Label(self.window, text="Количество изображений в папке: " + str(len(self.files)), font=("Arial Bold", 15))
        self.dirBtn = Button(text="Открыть файл", command=self.openFolder)
    
    def openFolder(self):
        self.folderPath = filedialog.askdirectory()
        self.files = os.listdir(self.folderPath)
        print(self.files)
        self.updateLbls()
        print (self.folderPath)

    def updateLbls(self):
        self.lbl_2.destroy()
        self.lbl_2 = Label(self.window, text="Количество изображений в папке: " + str(len(self.files)), font=("Arial Bold", 15))
        self.lbl_2.pack(anchor="w", padx=30, pady=110)
    
    def showWindow(self):
        self.window.geometry('800x500')
        self.window.title("MultiConverter")
        self.lbl_1.pack(anchor="n", padx=30, pady=30)
        self.dirBtn.pack(anchor="s")
        self.lbl_2.pack(anchor="w", padx=30, pady=110)
        self.window.mainloop()
    

if __name__ == "__main__":
    el = MainGui()
    el.showWindow()

  

  

  