### Predicados
#### Expresiones de XPath
En la consola en Chrome al estar en la página:
[To Scrape - Quotes](https://quotes.toscrape.com/)

Obtener el primer div, de la lista que regresa.
```
$x('/html/body/div/div[1]')
```
...ahora el último
```
$x('/html/body/div/div[last()]')
```
Todos los textos de los span con clase 'text'
```
$x('//span[@class="text"]/text()').map(x => x.wholeText)
```
