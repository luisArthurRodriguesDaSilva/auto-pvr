from versicles import popularVersicles 
from bibleApi import getVersicle

aprovados = []
for v in popularVersicles[50:60]:
  [book,capterNumber,versicleNumber] = v
  versicleText = (getVersicle(book,capterNumber,versicleNumber))
  print(versicleText)
  aprovados.append(v) if input('aprovado?') == 's' else None

with open("src/aprovados.py", 'w') as file:
    file.write(f"""aprovados =  {aprovados}
""")
