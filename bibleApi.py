import json
import requests

bible = json.loads(requests.get('https://raw.githubusercontent.com/thiagobodruk/bible/master/json/pt_nvi.json').text.encode().decode('utf-8-sig'))


def getBook(bookAbrev):
  for book  in bible :
    if (book["abbrev"] == bookAbrev):
      return book
      

def getCap(bookAbrev,capterNumber):
  capIndex = capterNumber - 1
  book = getBook(bookAbrev)
  capters = book["chapters"]
  return capters[capIndex]

def getVersicle(bookAbrev,capterNumber,versicleNumber):
  versicleIndex = versicleNumber - 1
  capter = getCap(bookAbrev,capterNumber)
  return capter[versicleIndex]

print(getVersicle('pv',6,6))
