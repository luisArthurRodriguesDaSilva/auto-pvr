from bibleApi import getVersicle
from versicles import popularVersicles 
import imagesFunctions as imgf
import ttApi as api

for versicleCordinates in popularVersicles[-10:]:
  [book,capterNumber,versicleNumber] = versicleCordinates
  print(versicleCordinates)
  versicleText = (getVersicle(book,capterNumber,versicleNumber))

  rawImagePath = imgf.raffleImage('fotos maneras')
  editedImage = imgf.getEditedImage(rawImagePath)
  imgWithText = imgf.putTextOnImage(editedImage,versicleText,versicleCordinates)
  newPath = imgf.saveImage(imgWithText,versicleCordinates)["newPath"]
  api.imageToMyDm(newPath)
