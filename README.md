# B2Crypt
B2Crypt é uma criptografia simples que tranforma base2 (1, 2, 4, 8, 16) em caracteres.

### Como usar

Parâmetro **-w**: indica a palavra a ser encriptada ou decriptada.

Parâmetro **-e**: Encripta a palavra dada no parâmetro *-w*

Parâmetro **-d**: Decripta a palavra encriptada devolvida ao usar *b2crypt -e -w [PALAVRA]*

Parâmetro **-k**: Define a chave para encriptar o desencriptar, ela deve conter 6 caracteres e não se deve repetir eles, por conta do algoritmo de criptografia.

### Observações

Por enquanto, o script somente encripta letras e espaços, atribuir caracteres especiais ou números retorna um erro.
Também por enquanto, ele devolve o texto (independente do valor entrado) toda em maiúsculas. Exemplo:

> b2crypt.py -e -w criptografia

Retorna

>,.\*$,\*#.\*$\*$!\*#!,.\*!,.\*$,\*.\*!,\*#.\*.\*

Mas se eu decriptar usando:

> b2crypt.py -d -w ,.*$,*#.*$*$!*#!,.*!,.*$,*.*!,*#.*.*

Ele retorna ***CRIPTOGRAFIA***

