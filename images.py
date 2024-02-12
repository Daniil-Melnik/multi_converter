import os

from PIL import Image

class Images:
  dirName = r""
  files = []
  dirFiles = []
  newPath = ""

  def __init__(self, dir):
    self.dirName = dir
    self.newPath = self.dirName + '\\' + 'converted'
    self.files = self.listOfDir()
    self.dirFiles = []

  def listOfDir(self):
    files = os.listdir(self.dirName)
    return files
  
  def getMainAllNames(self):
    for el in self.files:
      self.dirFiles.append(self.dirName + '\\' + el)
  
  def convertWebpToJpeg(self):
    self.getMainAllNames()
    os.mkdir(self.newPath)
    for el in self.dirFiles:
      #print(el)
      with Image.open(el) as img:
          img = img.convert('RGB')
          img.save(self.newPath + '\\' + el.split('\\')[-1].split('.')[-2]+'.jpeg', 'JPEG', quality=90)
          print (self.newPath + '\\' + el.split('\\')[-1].split('.')[-2]+'.jpeg')
    

if __name__ == "__main__":
  el = Images(r"C:\Users\danii\OneDrive\Рабочий стол\lib_perl\cgi-bin\cgi-bin_2\perl\core_data.tar\картинки сигейм\Флешка 2\АиСД\фото_метро\ТОЭ\y\n\1")
  el.convertWebpToJpeg()
  