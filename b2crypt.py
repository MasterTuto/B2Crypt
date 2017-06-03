# -*- coding: utf-8 -*-

# Todos os imports
import argparse

__name__ = "B2Crypt"
__version__ = 1.0
__author__ = "Lord13"
__notes__ = "Visite fsociety.org!"

print """
 ______   _______  _______  _______           _______ _________
(  ___ \ / ___   )(  ____ \(  ____ )|\     /|(  ____ )\__   __/
| (   ) )\/   )  || (    \/| (    )|( \   / )| (    )|   ) (   
| (__/ /     /   )| |      | (____)| \ (_) / | (____)|   | |   
|  __ (    _/   / | |      |     __)  \   /  |  _____)   | |   
| (  \ \  /   _/  | |      | (\ (      ) (   | (         | |   
| )___) )(   (__/\| (____/\| ) \ \__   | |   | )         | |   
|______/ \_______/(_______/|/   \__/   \_/   |/          )_(   
                                                      by Lord13
"""

def encrypt(texto, key):
    num = 16
    novotexto = ''

    for i in texto.upper():
        if i == " ":
            pos = 27
        else:
            pos = ord(i) - 64
        while num != 0:
            if pos - num >= 0:
                pos -= num
                novotexto += key[str(num)]
                num /= 2
            else:
                num /= 2
        novotexto += key['final']
        num = 16
    
    return novotexto

def decrypt(texto, key):
    novakey = {}

    for i in key:
        if i != 'final':
            novakey[key[i]] = i
        else:
            novakey[i] = key[i]

    texto = texto.split(novakey['final'])
    novotexto = []
    num = 0

    for i in texto:
        for k in i:
            num += int(novakey[k])
        num = num if num < 27 else -32
        novotexto.append(chr(num+64))
        num = 0
    return ''.join(novotexto)[:-1]

def pass_analyser(key):
    values = {}
    try:
        assert len(key) == 6
        values['1'] = key[0]
        values['2'] = key[1]
        values['4'] = key[2]
        values['8'] = key[3]
        values['16'] = key[4]
        values['final'] = key[5]
    except AssertionError:
        raise KeyError("\"Key\" lenght must be equal to 6")
    if len(list(set([a for a in key]))) < 6:
        raise KeyError('Repeated key values')

    return values

def arg_parse_analysis():
    argparse2 = argparse.ArgumentParser(
        description='Encrypts a word'
        )
    argparse2.add_argument('-e', action="store_true", help="encrypt the word", dest="yes_or_no")
    argparse2.add_argument('-d', action="store_false", help="decrypt the word", dest="yes_or_no")
    argparse2.add_argument('-w', action="store", dest="word", help='word to be encrypted or decrypted')
    argparse2.add_argument('-k', action="store", dest="key", help='key (must be used for both encryption or decryption)', default=".,!#$*")
    parser = argparse2.parse_args()
    word = parser.word
    decrypt_or_encrypt = parser.yes_or_no
    key = parser.key
    return word, decrypt_or_encrypt, key

word, decrypt_or_encrypt, key = arg_parse_analysis()
values = pass_analyser(key)

if decrypt_or_encrypt is True:
    print """
    [*]++++++++++++++++++++++++++++[*]
       Encrypted: {}
    [*]++++++++++++++++++++++++++++[*]
    """.format(encrypt(word, values))
else:
    print """
    [*]++++++++++++++++++++++++++++[*]
       Decrypted: {}
    [*]++++++++++++++++++++++++++++[*]
    """.format(decrypt(word, values))

