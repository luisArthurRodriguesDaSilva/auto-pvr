import requests
bible =(requests.get('https://raw.githubusercontent.com/thiagobodruk/bible/master/json/pt_nvi.json').json())
for book  in bible :
  if (book["abbrev"] == "pv"):
    proverbius = book
    break

print(proverbius['chapters'][0])