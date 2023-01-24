# Este programa separa palabras escritas en camelCase, colocando un espacio entre ellas.
# La complejidad es O(n) siendo n el size del string

s = 'camelCasing'
#s = 'giveBigImportant'
#s = 'importantDifferentWeekCaseLittle'

camelBreak = ''

for c in s:
    if c.isupper():
        camelBreak += ' '
    camelBreak += c

print(camelBreak)
