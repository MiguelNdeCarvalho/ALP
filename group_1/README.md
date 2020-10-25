# Exercícios Python + ER

1. Escreva uma função, listWords(fileName) que lê o ficheiro de texto fileName e produz a lista de palavras que ocorrem (sequencialmente) nesse ficheiro. Descarte os símbolos de pontuação e converta as letras para minúsculas. Sugestão: consulte a documentação de str e de string do python.

2. Escreva uma função, symbolsIn(word), que tem como entrada uma string e que devolve uma lista de símbolos. Assuma que, por omissão, os símbolos da string são separados por underscore (_) mas, opcionalmente, a função tem o argumento sep para usar um separador alternativo.

3. Escreva uma função, alphabetFor(word), que tem como argumento uma string e que devolve o menor alfabeto para gerar essa palavra. Assuma que, por omissão, os símbolos da string são separados por underscore (_) mas, opcionalmente, a função tem o argumento sep para usar um separador alternativo.
Note bem que no resultado não devem aparecer elementos repetidos.

4. Escreva uma função, generated(word, alphabet), em que word é uma string e alphabet uma lista de string e que determina se os símbolos de word estão todos em alphabet (isto é, o resultado é booleano). Assuma que, por omissão, os símbolos da string são separados por underscore (_) mas, opcionalmente, a função tem o argumento sep para usar um separador alternativo.
