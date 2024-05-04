
import re

def search_word_position(txt, word):
    # Search for the given word at the beginning of a word, and print its position:
    x = re.search(r"\b" + word, txt)
    return x


def find_all_words(txt):
    
    x = re.findall("he.?o" , txt)
    return x

def search_item( txt):
    
  x = re.search("\s", txt)
  return x.start()