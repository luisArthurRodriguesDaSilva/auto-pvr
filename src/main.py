from bibleApi import getVersicle
from versicles import popularVersicles 
import imagesFunctions as imgf

for versicleCordinates in popularVersicles:
  [book,capterNumber,versicleNumber] = versicleCordinates
  print(versicleCordinates)
  versicleText = (getVersicle(book,capterNumber,versicleNumber))

  rawImagePath = imgf.raffleImage('fotos maneras')
  editedImage = imgf.getEditedImage(rawImagePath)
  imgWithText = imgf.putTextOnImage(editedImage,versicleText)
  imgf.saveImage(imgWithText,versicleCordinates)
