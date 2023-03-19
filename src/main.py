from bibleApi import getVersicle
from aprovados import popularVersicles 
import imagesFunctions as imgf
from ttApi import postIt, imageToMyDm , notifyByDm
import os

isProduction = lambda : os.getenv('producao') == 'true' 

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
