#!/usr/bin/python -B

import textmanager
tm = textmanager.TextManager()
tm.set_file("Corpus.txt")
print tm.get_next_word()
print tm.get_next_word()
tm.reset()
tm.set_file("Corpus.txt")
while 1:
    word = tm.get_next_word()
    print word
    if word == None:
         break 


tm.reset()
tm.set_file("Corpus.txt")
print tm.get_next_word()
print tm.get_next_word()
