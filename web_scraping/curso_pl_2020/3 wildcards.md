### Comodines
#### Expresiones de XPath
En la consola en Chrome al estar en la página:
[To Scrape - Quotes](https://quotes.toscrape.com/)

Cuando no sabemos exactamente qué nodo traerse.

Todos los hijos de HTML
```
$x('/html/*')
```
Todos los elementos del DOM
```
$x('//*')
```
Traerse todos los atributos de los span con clase text
```
$x('//span[@class="text"]/@*')
```
Traerse todos los nodos (no solo nodos con tags) hijos que hay dentro de
los span que cumplen ambas condiciones.
```
$x('//span[@class="text" and @itemprop="text"]/node()')
```
