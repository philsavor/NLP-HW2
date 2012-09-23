#!/usr/bin/python -B

import text_manager
tm = text_manager.TextManager()
tm.set_file("NLPCorpusTreebank2Parts.txt")
print tm.get_next_word()
print tm.get_next_word()
tm.reset()
tm.set_file("NLPCorpusTreebank2Parts.txt")
while 1:
    word = tm.get_next_word()
    print word
    if word == None:
         break 


tm.reset()
tm.set_file("NLPCorpusTreebank2Parts.txt")
print tm.get_next_word()
print tm.get_next_word()
