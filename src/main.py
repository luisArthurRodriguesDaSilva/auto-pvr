from bibleApi import getVersicle
from aprovados import popularVersicles 
import imagesFunctions as imgf
from ttApi import postIt, imageToMyDm , notifyByDm
import os
import time

isProduction = lambda : os.getenv('producao') == 'true' 
while 1 :
  for versicleCordinates in popularVersicles:
    try:
      [book,capterNumber,versicleNumber] = versicleCordinates
      print(versicleCordinates)
      versicleText = (getVersicle(book,capterNumber,versicleNumber))
  
      rawImagePath = imgf.raffleImage('fotos maneras')
      editedImage = imgf.getEditedImage(rawImagePath)
      imgWithText = imgf.putTextOnImage(editedImage,versicleText,versicleCordinates)
      finalImagePath = imgf.saveImage(imgWithText,versicleCordinates)["newPath"]
      
      postIt(finalImagePath) if isProduction() else imageToMyDm(finalImagePath)
    
    except Exception as e:
      notifyByDm(e)
    print('to sleepando')
    time.sleep(int(os.getenv('interval')))
    print('sleepei')
  