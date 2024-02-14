import os

from PIL import Image

class Images:
  dirName = r""
  files = []
  dirFiles = []
  newPath = ""

  def __init__(self, dir, endDir):
    self.dirName = dir
    self.newPath = endDir + '\\' + self.dirName.split('/')[-1] + '_' + 'converted'
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
    try:
      os.mkdir(self.newPath)
      for el in self.dirFiles:
        #print(el)
        with Image.open(el) as img:
            img = img.convert('RGB')
            img.save(self.newPath + '\\' + el.split('\\')[-1].split('.')[-2]+'.jpeg', 'JPEG', quality=90)
            print (self.newPath + '\\' + el.split('\\')[-1].split('.')[-2]+'.jpeg')
      return True
    except FileExistsError:
      return False
    

if __name__ == "__main__":
  el = Images(r"C:\Users\danii\OneDrive")
  el.convertWebpToJpeg()
  