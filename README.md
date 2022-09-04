<h1 align=center > auto-pvr</h1>

<h3>funcionamento:</h3>
<h4>Utilizando o <a href="https://colab.research.google.com/">google colab</a>, para mais velocidade nas execuções, o <a href ="https://github.com/luisArthurRodriguesDaSilva/proverbios-automaticos/blob/main/autoProverbious.ipynb">auto-pvr</a> gera imagens com provérbios bíblicos e às posta automaticamente</h4>

<hr width=5%/>
<p>Em cada dia o script é executado uma vez, sorteando um versículo relativo ao capitulo daquele dia</p>

<p>Exemplos:</p>
<p>Dia 01/08 é sorteado o versículo 15 do capitulo 1</p>
<p>Dia 02/05 é sorteado o versículo 7 do capitulo 2</p>
<p>Dia 07/XX é sorteado o versículo YY do capitulo 7</p>
<hr width=5%/>

<p>Após o sorteio do versículo ocorre a adição dele em uma imagem que também é sorteada, mas sem critério tamanho definidos</p>
<p>Essa variedade de formatos exige uma adequação dos textos para que não saiam da tela como no exemplo a seguir:</p>
<img src="readmeImgs/2Q== (3) copy.jpeg">
<p>visto isso, foram criadas funções para adequar o texto através de um calculo com os espaços e o tamanho da imagem</p>
função responsável por dividir o texto:

```python
def divitedText(text, SizeLine):
  spaces = np.array(getSpaces(text))
  volta = 0
  while 1:
    volta+=1
    local = getBiggestSmallest(spaces,SizeLine*volta)
    if local == 9000:
      break
    text = text[:local] + '\n' + text[local+1:]
  return text , volta
```
<p>Após esse tratamento, a mesma imagem com o mesmo texto fica dessa forma:</p>
<img src="readmeImgs/certa.jpeg">
<p>Dessa forma a imagem está pronta para a postagem que é feita com o <a href="https://github.com/tweepy/tweepy">tweepy</a></p>

<h3>Resultados:</h3>
<img align="center" src="readmeImgs/Captura de tela de 2022-08-14 01-11-51.png">
<img align="center" src="readmeImgs/Captura de tela de 2022-08-14 01-09-41.png">
<img align="center" src="readmeImgs/Captura de tela de 2022-08-14 01-21-27.png">
<a href="https://drive.google.com/drive/folders/19LjFJtHQEBpANqPGECgtkLA9bX49KBCx">pasta com todas as imagens publicadas no mês de agosto</a>
<hr width=27%/>

<h3>principais recursos e bibliotecas utilizadas:</h3>
<ul>
	<li><a href="https://github.com/thiagobodruk/bible/tree/master/json">biblia.json</a></li>
	<li>tweepy</li>
	<li>numpy</li>
	<li>PIL</li>
</ul>
