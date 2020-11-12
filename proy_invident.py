# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 11:01:12 2020

@author: ali_5
"""

# Importamos la libreria Pillow
from PIL import Image

import io

# Importamos Pytesseract
import pytesseract

code_table = {
    ',':'⠠',
    '/':'⠌',
    #' el ':' ⠮ ',
    #' y ':' ⠯ ',
    #' de ': ' ⠷ ',
    #' con ': ' ⠾ ',
    #' en ': ' ⠔ ',
    #' o ': ' ⠖ ',
    #' para ': ' ⠿ ',
    '?':'⠹',
    '.':'⠨',
    'á': '⠁',
    'é': '⠑',
    'í': '⠊',
    'ó': '⠕',
    'ú': '⠥',
    'a': '⠁',
    'b': '⠃',
    'c': '⠉',
    'd': '⠙',
    'e': '⠑',
    'f': '⠋',
    'g': '⠛',
    'h': '⠓',
    'i': '⠊',
    'j': '⠚',
    'k': '⠅',
    'l': '⠇',
    'm': '⠍',
    'n': '⠝',
    'o': '⠕',
    'p': '⠏',
    'q': '⠟',
    'r': '⠗',
    's': '⠎',
    't': '⠞',
    'u': '⠥',
    'v': '⠧',
    'w': '⠺',
    'x': '⠭',
    'y': '⠽',
    'z': '⠵',
    'A': '⠁',
    'B': '⠃',
    'C': '⠉',
    'D': '⠙',
    'E': '⠑',
    'F': '⠋',
    'G': '⠛',
    'H': '⠓',
    'I': '⠊',
    'J': '⠚',
    'K': '⠅',
    'L': '⠇',
    'M': '⠍',
    'N': '⠝',
    'O': '⠕',
    'P': '⠏',
    'Q': '⠟',
    'R': '⠗',
    'S': '⠎',
    'T': '⠞',
    'U': '⠥',
    'V': '⠧',
    'W': '⠺',
    'X': '⠭',
    'Y': '⠽',
    'Z': '⠵',
    '#': '⠼',
    '1': '⠂',
    '2': '⠆',
    '3': '⠲',
    '4': '⠲',
    '5': '⠢',
    '6': '⠖',
    '7': '⠶',
    '8': '⠦',
    '9': '⠔',
    '0': '⠴',
    ' ': ' '}


# Abrimos la imagen
im = Image.open("imagen.jpg")

# Utilizamos el método "image_to_string"
# Le pasamos como argumento la imagen abierta con Pillow






pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # your path may be different
texto = pytesseract.image_to_string(im)

#intab = asciicodes  # ...add the full alphabet and other characters
#outtab = brailles # and the characters you want them translated to
transtab = str.maketrans(code_table)

strg = texto

# Mostramos el resultado
f = io.open("output.txt", 'w', encoding='utf8')
f.write(strg.translate(transtab))
f.close()