### Búsqueda en texto
#### Expresiones de XPath
En la consola en Chrome al estar en la página:
[To Scrape - Quotes](https://quotes.toscrape.com/)


Todos los autores que comienzan con 'A'
```
$x('//small[@class="author" and start-with(., "A")]/text()').map(x => x.wholeText)
```

Todos los autores que contienen "Ro" en su full name.
```
$x('//small[@class="author" and contains(., "Ro")]/text()').map(x => x.wholeText)
```
