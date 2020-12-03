### Operadores
#### Expresiones de XPath
En la consola en Chrome al estar en la página:
[To Scrape - Quotes](https://quotes.toscrape.com/)

Todos los textos de los span con clase distinta a 'text'
```
$x('//span[@class!="text"]/text()')
```

Todos los div con posición mayor a 1
```
$x('/html/body/div/div[position() > 1]')
```

Todos los span con clase 'text' y clase "tag-item"
```
$x('//span[@class="text" and @class="tag-item"]')
```

Todos los  span que no tienen el atributo class
```
$x('//span[not(@class)]')
```
