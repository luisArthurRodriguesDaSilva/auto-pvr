import os
from random import randrange
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from PIL.ImageFilter import BLUR

diviter = 15

def raffleImage(dirPath):
  imgNamePath = os.listdir(dirPath)
  raffledImageAdress = imgNamePath[randrange(0,len(imgNamePath))]
  return (dirPath + '/' + raffledImageAdress)

def getEditedImage(imagePath):
  img = Image.open(imagePath)
  img = img.filter(BLUR).filter(BLUR).filter(BLUR).filter(BLUR)
  img = ImageEnhance.Brightness(img).enhance(0.3)
  return img
    
def getBlocksSizes(pilImage):
  [width, height] = pilImage.size
  [widthBlock,heightBlock] = map(lambda x: int(x/diviter),[width,height])
  return widthBlock , heightBlock


# def putTextOnImage(imagePath,text):

