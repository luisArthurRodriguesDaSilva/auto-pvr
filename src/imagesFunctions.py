import os
from random import randrange
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from PIL.ImageFilter import BLUR
import textFuncs as tf

diviter = 15

def raffleImage(dirPath):
  imagesFilenames = os.listdir(dirPath)
  raffledImageAdress = imagesFilenames[randrange(0,len(imagesFilenames))]
  imageAdress = (dirPath + '/' + raffledImageAdress)
  return imageAdress

def getEditedImage(imagePath):
  img = Image.open(imagePath)
  img = img.filter(BLUR).filter(BLUR).filter(BLUR).filter(BLUR)
  img = ImageEnhance.Brightness(img).enhance(0.3)
  return img
    
def getBlocksSizes(pilImage):
  [width, height] = pilImage.size
  [widthBlock,heightBlock] = map(lambda x: int(x/diviter),[width,height])
  return widthBlock , heightBlock


def putTextOnImage(pilImage,text,coordinates):
  img = pilImage
  adaptedText , numberOfLines =  tf.divitedText(text,diviter)
  completeText = tf.putVersicle(adaptedText,coordinates)
  imageDraw = ImageDraw.Draw(img)
  widthBlock,heightBlock = getBlocksSizes(img)

  fontSize = heightBlock if widthBlock > heightBlock else widthBlock 
  font = ImageFont.truetype('./font/arial.ttf' ,int(fontSize))
  imageDraw.text(
    (widthBlock,heightBlock), #initial cordinates
    completeText,
    fill=(250, 250, 250), font=font)
  return img
  
def saveImage(pilImage,cordinates):
    dirPath = './versiculos/imagens-com-versiculos'
    exist = (os.path.isdir(dirPath))
    if not exist:
      os.mkdir(dirPath)
    newPath = f'{dirPath}/{cordinates[0]}{cordinates[1]}{cordinates[2]}.jpg'
    pilImage.save(newPath)
    return {"newPath" : newPath}

