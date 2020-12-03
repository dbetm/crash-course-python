### XPath Axes
#### Expresiones de XPath
En la consola en Chrome al estar en la página:
[To Scrape - Quotes](https://quotes.toscrape.com/)


Todos los hijos de un elemento div
```
$x('/html/body/div/child::div')
```
Todos los nietos inferiores y al nodo en sí de un elemento div
```
$x('/html/body/div/descendant-or-self::div')
```
