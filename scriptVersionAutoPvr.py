import json
import tweepy
from random import randrange
from datetime import date
from textFuncs import *
import requests
import numpy as np
import cv2
import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import math
from random import randrange, uniform
from keys import keys

def tranformar():
  if(inp == '+1') :
    extra = True
    versicleAdress = f'{today}:({versicleIndex+1},{versicleIndex+2})'
    finalResult = (
  f"""{dailyVersicle} {next}
_
prv {versicleAdress}""")
  elif(inp == '-1'):
    extra=True
    versicleAdress = f'{today}:({versicleIndex},{versicleIndex+1})'
    finalResult = (
  f"""{before} {dailyVersicle}
_
prv {versicleAdress}""")

  return finalResult


today = date.today().day
mounth = date.today().month

bible = requests.get('https://raw.githubusercontent.com/thiagobodruk/bible/master/json/pt_nvi.json').json()

for book  in bible :
  if (book["abbrev"] == "pv"):
    proverbios = book
    break

cap = proverbios['chapters']

cd = cap[today-1]
limit = len(cd)
versicleIndex = randrange(0,limit)

dailyVersicle = cd[versicleIndex]
versicleAdress = f'({today}:{versicleIndex+1})'

before,next = cd[versicleIndex-1],cd[versicleIndex + 1]

finalResult = (
f"""{dailyVersicle}
_
prv {versicleAdress}""")

print(finalResult)


extra=False


mounth = date.today().month


inp='+1'
finalResult = tranformar()
extra = True
print(finalResult)

# %%
inp='-1'
finalResult = tranformar()
extra = True
print(finalResult)

inp=' '
extra = False #caso em que era melhor com menos contexto

dailyVersicle = cd[versicleIndex]
versicleAdress = f'({today}:{versicleIndex+1})'


finalResult = (
f"""{dailyVersicle}
_
prv {versicleAdress}""")

print(finalResult)

from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)

text= finalResult
patternPath = './fotos maneras'
imgNamePath = os.listdir(patternPath)
print(imgNamePath)
imgPath = patternPath + '/' + imgNamePath[randrange(0,len(imgNamePath))]
img = Image.open(imgPath)
img = img.filter(BLUR).filter(BLUR).filter(BLUR).filter(BLUR)
img = ImageEnhance.Brightness(img).enhance(0.3)
[width, height] = img.size
cantofact = 15
sizeOfCanto = int(width/cantofact)
diminuit = 20 if extra else 15
fontSize=int(width/diminuit)
[initialWidth,initialHeight] = map(lambda x: int(x/cantofact),[width,height])
limitLine = int(1.3*diminuit)
print(limitLine)
convertedText , numberOfLines = divitedText(text,limitLine)
print(img.size)

if (height > width):
  initialHeight =int((initialHeight/2)+(fontSize*numberOfLines*0.8))

idr = ImageDraw.Draw(img)

font = ImageFont.truetype('/home/luis/Downloads/arial.ttf' ,int(fontSize))

idr.text((initialWidth, initialHeight), convertedText, fill=(250, 250, 250), font=font)

dirPath = f'./mainPvrDir/pvrMounth{mounth}'

exist = (os.path.isdir(dirPath))

if not exist:
  os.mkdir(dirPath)

newPath = f'{dirPath}/pvr{today}.jpg'

img.save(newPath)

img2 =cv2.imread(newPath)
cv2.imshow('ei',img2)
cv2.waitKey(0)

if input('its ok') == 'ok':
  auth = tweepy.OAuthHandler(keys['chave1'],keys['chave2'])
  auth.set_access_token(keys['chave3'],keys['chave4'])
  api = tweepy.API(auth)
  
  twet = api.update_with_media(newPath)
