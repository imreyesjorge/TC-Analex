<div align="center">
<h1>Mio</h1>
<b>🗺 Un lenguaje de programación simple</b>
</div>

<br>
<br>
<br>

<p align="center">
  <img src="https://raw.githubusercontent.com/imreyesjorge/TC-Analex/master/assets/header.png">
</p>

- [Mio](#)
  - [Funcionamiento](#funcionamiento)
  - [Casos de uso](#casos-de-uso)
    - [Caso 1](#caso-1)
    - [Caso 2](#caso-2)
    - [Caso 3](#caso-3)
    - [Caso 4](#caso-4)
  - [Integrantes](#integrantes)


### Funcionamiento

El **Analizador Lexico** toma el archivo `factorial.mio` (o cualquier otro programa `.mio`) y produce 2 archivos temporales, uno que es el factorial.lex el cual contiene todos los tokens, otro es el factorial.sim el cual contiene la tabla de simbolos (los cuales consisten de tres tablas, una de **ID**, una de **texto** y una de **valores**).

El analizador sintatico toma el .lex y checa que el programa se ajuste a la gramatica. Lo cual imprime **compilación exitosa** **compilación fallida**

Se pueden correr diferentes programas usando el siguiente comando:

```sh
python src/app.py [nombreDelPrograma.mio]
```

Entre las consideraciones que se deben tomar en cuenta, al final de cada programa la última linea debe estar vacia para que el programa funcione.

### Casos de uso

##### Caso 1

```py
# Programa que calcula el factorial de un número
PROGRAMA factorial
# VarX acumula los productos por iteración
VarX = 1
# VarY contiene el iterador del factor
VarY = 0
LEE Num
# Aplica Num! = 1 * 2 * 3 * ... * Num
REPITE Num VECES
VarY = VarY + 1
VarX = VarX * VarY
FINREP
IMPRIME "Factorial de "
IMPRIME Num
IMPRIME " es "
IMPRIME VarX
FINPROG
``` 

Salida:

```sh
PROGRAMA
[id] ID01
[id] ID02
=
[val]
[id] ID03
=
[val]
LEE
[id] ID04
REPITE
[id] ID05
VECES
[id] ID06
=
[id] ID07
[op_ar]
[val]
[id] ID08
=
[id] ID09
[op_ar]
[id] ID10
FINREP
IMPRIME
[text] TX01
SI
[id] ID11
<
[val]
ENTONCES
IMPRIME
[id] ID12
SINO
IMPRIME
[text] TX02
FINSI
IMPRIME
[id] ID13
FINPROG

['PROGRAMA']
['#']

['[id]', 'ID01']
['#', 'FINPROG', 'SENTS', '[id]']

['[id]', 'ID02']
['#', 'FINPROG', 'SENTS']

['=']
['#', 'FINPROG', 'ELEM', '=']

['[val]']
['#', 'FINPROG', 'ELEM']

['[id]', 'ID03']
['#', 'FINPROG', 'SENTS']

['=']
['#', 'FINPROG', 'ELEM', '=']

['[val]']
['#', 'FINPROG', 'ELEM']

['LEE']
['#', 'FINPROG', 'SENTS']

['[id]', 'ID04']
['#', 'FINPROG', 'LEE']

['REPITE']
['#', 'FINPROG', 'SENTS']

['[id]', 'ID05']
['#', 'FINPROG', 'FINREP', 'SENTS', 'VECES', 'ELEM']

['VECES']
['#', 'FINPROG', 'FINREP', 'SENTS', 'VECES']

['[id]', 'ID06']
['#', 'FINPROG', 'FINREP', 'SENTS']

['=']
['#', 'FINPROG', 'FINREP', 'ELEM', '=']

['[id]', 'ID07']
['#', 'FINPROG', 'FINREP', 'ELEM']

['[op_ar]']
['#', 'FINPROG', 'FINREP']

['[val]']
['#', 'FINPROG', 'FINREP', 'ELEM']

['[id]', 'ID08']
['#', 'FINPROG', 'FINREP', 'SENTS']

['=']
['#', 'FINPROG', 'FINREP', 'ELEM', '=']

['[id]', 'ID09']
['#', 'FINPROG', 'FINREP', 'ELEM']

['[op_ar]']
['#', 'FINPROG', 'FINREP']

['[id]', 'ID10']
['#', 'FINPROG', 'FINREP', 'ELEM']

['FINREP']
['#', 'FINPROG', 'FINREP']

['IMPRIME']
['#', 'FINPROG', 'SENTS']

['[text]', 'TX01']
['#', 'FINPROG', 'IMPRIME']

['SI']
['#', 'FINPROG', 'SENTS']

['[id]', 'ID11']
['#', 'FINPROG', 'FINSI', 'SENTS', 'ENTONCES', 'COMPARA']

['<']
['#', 'FINPROG', 'FINSI', 'SENTS', 'ENTONCES', '[op_rel]']

['[val]']
['#', 'FINPROG', 'FINSI', 'SENTS', 'ENTONCES', 'ELEM']

['ENTONCES']
['#', 'FINPROG', 'FINSI', 'SENTS', 'ENTONCES']

['IMPRIME']
['#', 'FINPROG', 'FINSI', 'SENTS']

['[id]', 'ID12']
['#', 'FINPROG', 'FINSI', 'IMPRIME']

['SINO']
['#', 'FINPROG', 'FINSI']

['IMPRIME']
['#', 'FINPROG', 'FINSI', 'SENTS']

['[text]', 'TX02']
['#', 'FINPROG', 'FINSI', 'IMPRIME']

['FINSI']
['#', 'FINPROG', 'FINSI']

['IMPRIME']
['#', 'FINPROG', 'SENTS']

['[id]', 'ID13']
['#', 'FINPROG', 'IMPRIME']

['FINPROG']
['#', 'FINPROG']

Compilación exitosa
``` 

##### Caso 2:

```py
# Programa que calcula el factorial de un número
PROGRAMA factorial
# VarX acumula los productos por iteración
VarX = 1
# VarY contiene el iterador del factor
VarY = 0
LEE Num
# Aplica Num! = 1 * 2 * 3 * ... * Num
REPITE Num VECES
VarY = VarY + 1
VarX = VarX * VarY
FINREP
IMPRIME "Factorial de "
SI Num < 4 ENTONCES
IMPRIME Num
SINO
IMPRIME " es "
FINSI
IMPRIME VarX
FINPROG
``` 

Salida:

```sh
PROGRAMA
[id] ID01
[id] ID02
=
[val]
[id] ID03
=
[val]
LEE
[id] ID04
REPITE
[id] ID05
VECES
[id] ID06
=
[id] ID07
[op_ar]
[val]
[id] ID08
=
[id] ID09
[op_ar]
[id] ID10
FINREP
IMPRIME
[text] TX01
SI
[id] ID11
<
[val]
ENTONCES
IMPRIME
[id] ID12
SINO
IMPRIME
[text] TX02
FINSI
IMPRIME
[id] ID13
FINPROG

['PROGRAMA']
['#']

['[id]', 'ID01']
['#', 'FINPROG', 'SENTS', '[id]']

['[id]', 'ID02']
['#', 'FINPROG', 'SENTS']

['=']
['#', 'FINPROG', 'ELEM', '=']

['[val]']
['#', 'FINPROG', 'ELEM']

['[id]', 'ID03']
['[id]', 'ID03']
['#', 'FINPROG', 'SENTS']

['=']
['#', 'FINPROG', 'ELEM', '=']

['[val]']
['#', 'FINPROG', 'ELEM']

['[id]', 'ID03']
['LEE']
['#', 'FINPROG', 'SENTS']

['[id]', 'ID04']
['#', 'FINPROG', 'LEE']

['REPITE']
['REPITE']
['#', 'FINPROG', 'SENTS']

['[id]', 'ID05']
['#', 'FINPROG', 'FINREP', 'SENTS', 'VECES', 'ELEM']

['VECES']
['#', 'FINPROG', 'FINREP', 'SENTS', 'VECES']

['[id]', 'ID06']
['#', 'FINPROG', 'FINREP', 'SENTS']

['=']
['#', 'FINPROG', 'FINREP', 'ELEM', '=']

['[id]', 'ID07']
['#', 'FINPROG', 'FINREP', 'ELEM']

['[op_ar]']
['#', 'FINPROG', 'FINREP']

['[val]']
['#', 'FINPROG', 'FINREP', 'ELEM']

['[id]', 'ID03']
['[id]', 'ID08']
['#', 'FINPROG', 'FINREP', 'SENTS']

['=']
['#', 'FINPROG', 'FINREP', 'ELEM', '=']

['[id]', 'ID09']
['#', 'FINPROG', 'FINREP', 'ELEM']

['[op_ar]']
['#', 'FINPROG', 'FINREP']

['[id]', 'ID10']
['#', 'FINPROG', 'FINREP', 'ELEM']

['FINREP']
['#', 'FINPROG', 'FINREP']

['IMPRIME']
['IMPRIME']
['#', 'FINPROG', 'SENTS']

['[text]', 'TX01']
['#', 'FINPROG', 'IMPRIME']

['SI']
['SI']
['#', 'FINPROG', 'SENTS']

['[id]', 'ID11']
['#', 'FINPROG', 'FINSI', 'SENTS', 'ENTONCES', 'COMPARA']

['<']
['#', 'FINPROG', 'FINSI', 'SENTS', 'ENTONCES', '[op_rel]']

['[val]']
['#', 'FINPROG', 'FINSI', 'SENTS', 'ENTONCES', 'ELEM']

['ENTONCES']
['#', 'FINPROG', 'FINSI', 'SENTS', 'ENTONCES']

['IMPRIME']
['#', 'FINPROG', 'FINSI', 'SENTS']

['[id]', 'ID12']
['#', 'FINPROG', 'FINSI', 'IMPRIME']

['SINO']
['#', 'FINPROG', 'FINSI']

['IMPRIME']
['#', 'FINPROG', 'FINSI', 'SENTS']

['[text]', 'TX02']
['#', 'FINPROG', 'FINSI', 'IMPRIME']

['FINSI']
['#', 'FINPROG', 'FINSI']

['IMPRIME']
['IMPRIME']
['#', 'FINPROG', 'SENTS']

['[id]', 'ID13']
['#', 'FINPROG', 'IMPRIME']

['FINPROG']
['#', 'FINPROG']
```

##### Caso 3

```py
PROGRAMA suma 
VarX = 2
VarY = 3
VarZ = VarX + VarY
FINPROG
``` 

Salida:

```sh
[id] ID03
=
[val]
[id] ID04
=
[id] ID05
[op_ar]
[id] ID06
FINPROG

['PROGRAMA']
['#']

['[id]', 'ID01']
['#', 'FINPROG', 'SENTS', '[id]']

['[id]', 'ID02']
['#', 'FINPROG', 'SENTS']

['=']
 python src/app.py sandbox.mio
PROGRAMA
[id] ID01
[id] ID02
=
[val]
[id] ID03
=
[val]
[id] ID04
=
[id] ID05
[op_ar]
[id] ID06
FINPROG

['PROGRAMA']
['#']

['[id]', 'ID01']
['#', 'FINPROG', 'SENTS', '[id]']

['[id]', 'ID02']
['#', 'FINPROG', 'SENTS']

['=']
['#', 'FINPROG', 'ELEM', '=']

['[val]']
['#', 'FINPROG', 'ELEM']

['[id]', 'ID03']
['[id]', 'ID03']
['#', 'FINPROG', 'SENTS']

['=']
['#', 'FINPROG', 'ELEM', '=']

['[val]']
['#', 'FINPROG', 'EL
``` 

##### Caso 4

```py
PROGRAMA otilio
VarExam = 2
VarTarea = 2
VarCalif = VarExam + VarTarea
SI VarCalif > 6 ENTONCES
IMPRIME "pasaste"
SINO 
IMPRIME "reprobaste"
FINSI
FINPROG
```

Salida:

```sh
PROGRAMA
[id] ID01
[id] ID02
=
[val]
[id] ID03
=
[val]
[id] ID04
=
[id] ID05
[op_ar]
[id] ID06
SI
[id] ID07
>
[val]
ENTONCES
IMPRIME
[text] TX01
SINO
IMPRIME
[text] TX02
FINSI
FINPROG

['PROGRAMA']
['#']

['[id]', 'ID01']
['#', 'FINPROG', 'SENTS', '[id]']

['[id]', 'ID02']
['#', 'FINPROG', 'SENTS']

['=']
['#', 'FINPROG', 'ELEM', '=']

['[val]']
['#', 'FINPROG', 'ELEM']

['[id]', 'ID03']
['[id]', 'ID03']
['#', 'FINPROG', 'SENTS']

['=']
['#', 'FINPROG', 'ELEM', '=']

['[val]']
['#', 'FINPROG', 'ELEM']

['[id]', 'ID03']
['[id]', 'ID04']
['#', 'FINPROG', 'SENTS']

['=']
['#', 'FINPROG', 'ELEM', '=']

['[id]', 'ID05']
['#', 'FINPROG', 'ELEM']

['[op_ar]']
['#', 'FINPROG']

['[id]', 'ID06']
['#', 'FINPROG', 'ELEM']

['SI']
['SI']
['#', 'FINPROG', 'SENTS']

['[id]', 'ID07']
['#', 'FINPROG', 'FINSI', 'SENTS', 'ENTONCES', 'COMPARA']

['>']
['#', 'FINPROG', 'FINSI', 'SENTS', 'ENTONCES', '[op_rel]']

['[val]']
['#', 'FINPROG', 'FINSI', 'SENTS', 'ENTONCES', 'ELEM']

['ENTONCES']
['#', 'FINPROG', 'FINSI', 'SENTS', 'ENTONCES']

['IMPRIME']
['#', 'FINPROG', 'FINSI', 'SENTS']

['[text]', 'TX01']
['#', 'FINPROG', 'FINSI', 'IMPRIME']

['SINO']
['#', 'FINPROG', 'FINSI']

['IMPRIME']
['#', 'FINPROG', 'FINSI', 'SENTS']

['[text]', 'TX02']
['#', 'FINPROG', 'FINSI', 'IMPRIME']

['FINSI']
['#', 'FINPROG', 'FINSI']

['FINPROG']
['#', 'FINPROG']

Compilación exitosa
``` 

### Integrantes

Proyecto para la materia de *Teoría de la Computación*, elaborado por **Jorge Reyes**, **Mario Chan** y **Miguel R. Ávila**.
