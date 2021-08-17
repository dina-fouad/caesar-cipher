import re
import nltk
from nltk.corpus import words
nltk.download('words',quiet=True)
nltk.download('names',quiet=True)

words_lest=words.words()
name_list=names.words()

def encrypt(string, key):
    encrypted_text = ""

    for char in string:
      if (char.isupper()):
            if char.isalpha() == False:
                encrypted_text +=" "
            else:
                encrypted_text += chr((ord(char) + key-65) % 26 + 65)

    return encrypted_text