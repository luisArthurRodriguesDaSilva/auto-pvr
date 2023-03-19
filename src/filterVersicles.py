from versicles import popularVersicles 
from bibleApi import getVersicle

aprovados = []
for v in popularVersicles[20:50]:
  [book,capterNumber,versicleNumber] = v
  versicleText = (getVersicle(book,capterNumber,versicleNumber))
  print('\n\n',versicleText,'\n')
  aprovados.append(v) if input('aprovado?') == 's' else None

with open("src/aprovados.py", 'w') as file:
    file.write(f"""popularVersicles =  {aprovados}
""")
