#!/usr/bin/python -B

from __future__ import print_function
import copy
import re
import textmanager

class BiGram:
    """
       Represent a bigram to implement a bigram language model, which is trained       on Corpus.txt.The input of this program is a sentence and a scenarios,          which can be without smoothing ,with add-one smoothing and with Good-Tur-       ing discounting. The result is the probability of input sentence.
    """

    def __init__(self,file_name):
        self.__words = None
        self.__words_no_repeat = None
        self.__scenarios = None
        #useful data
        self.__unicount = []
        self.__bicount = []
        self.__vocabulary = []
        self.__nc = []
     	self.__nc_num = []
        self.__capital_num = 0
        self.__last_num = 0
        #bigram probability
        self.__biprob_no_smoothing = []
        self.__biprob_add_one = []
        self.__biprob_good_turing = []
        #set file
        self.__tm = textmanager.TextManager()
        self.__tm.set_file(file_name)

    def draw_table(self,  value, tag):
        """
           Used to draw a table. 
           tag:0 for decimal, other for integer
        """
        #HEAD for table
        print('' , end = ' ' * 12) 
        for i in range(len(self.__words_no_repeat)):
            char_num = len(self.__words_no_repeat[i])
            #decimal
            if tag == 0:
                print(self.__words_no_repeat[i] , end = ' ' * (13 - char_num)) 
            else:
                print(self.__words_no_repeat[i] , end = ' ' * (10 - char_num)) 
        print('')
        #BODY for table
        for i in range(len(value)):
            char_num = len(self.__words_no_repeat[i])
            print(self.__words_no_repeat[i], end = ' '*(12 - char_num))
            for j in range(len(value)):
                #decimal
                if tag == 0:
                    print( "%.2e" % value[i][j],end=' ' * 5)            
                else:
                    print( "%04d" % value[i][j],end=' ' * 6)            
            print('')

    def receive_sentences_scenarios(self):
        """
           To recetive input sentences and the scenarios,including
           without smoothing,with add-one smoothing and with Good-
           Turing discounting.
        """
        #get sentence
        sentence = raw_input("Please input the sentence:\n")
        self.__words = re.findall(r'\w+', sentence)
        self.__words_no_repeat = re.findall(r'\w+', sentence) 
        #change word to lower case
        for i in range(len(self.__words_no_repeat)):
            self.__words_no_repeat[i] = self.__words_no_repeat[i].lower()
        #delete the repeat token
        words_counts = len(self.__words_no_repeat)
        for i in range(words_counts):
            for j in range(i+1 , words_counts):
                if self.__words_no_repeat[j] == self.__words_no_repeat[i]:
                    self.__words_no_repeat[j] = '*'
        count = 0
        while 1:
            if count >= len(self.__words_no_repeat):
                break
            if self.__words_no_repeat[count] == '*':
                del self.__words_no_repeat[count]
                count -= 1
            count += 1
	#set nc and nc_num
        count = len(self.__words_no_repeat)
        self.__nc     = [[] * count for i in xrange(count)]
        self.__nc_num = [[] * count for i in xrange(count)]
        #get scenarios
        while 1:
            self.__scenarios = raw_input("\nPlease choose the scenarios:\n"\
                                        +"0.All;\n"\
                                        +"1.Without smoothing;\n"\
                                        +"2.With add-one smoothing;\n"\
                                        +"3.With Good-Turing discounting.\n")
            if self.__scenarios not in ['0','1','2','3']:
                print ("\n\nThe valid input is 0,1,2,3\n")
                continue
            else:
                break

    def compute_count(self):
        """
           To compute the bigram count and unigram count for further
           computation for probabilities.
        """
        words_count = len(self.__words_no_repeat)
        self.__unicount = [0] * words_count
        self.__bicount = [[0] * words_count for i in xrange(words_count)]

        bigram_i = None
        last_word = 0
        while 1:
            word = self.__tm.get_next_word()
            #end mark
            if word == None:
                break
            #deal with the situation like 'word </s>'
            if word == self.__words[-1]: 
                last_word = 1
            elif word == '.':
                if last_word == 1:
                    self.__last_num += 1           
                    last_word = 0
                continue
            else:
               last_word = 0
            #get the number of capitalized word
            if word == self.__words[0].title():
                 self.__capital_num += 1
            #change to lower case           
            word = word.lower()
            #set vocabulary
            if word not in self.__vocabulary:
                self.__vocabulary.append(word)
            #set nc ,ncm and bicount
            if bigram_i != None:
        		#set nc and ncm
                temp_bigram = [self.__words_no_repeat[bigram_i],\
         				       word]
                if temp_bigram not in self.__nc[bigram_i]:
                    self.__nc[bigram_i].append(temp_bigram)
                    self.__nc_num[bigram_i].append(1)
                else:
                    for k in range(len(self.__nc[bigram_i])):
                        if self.__nc[bigram_i][k] == temp_bigram:
                            self.__nc_num[bigram_i][k] += 1
                            break
                #set bicount
                for j in range(words_count):
                    if word == self.__words_no_repeat[j]:
                        self.__bicount[bigram_i][j] += 1
                        break
                bigram_i = None
            #set unicount
            for i in range(words_count):
                if word == self.__words_no_repeat[i]:
                    self.__unicount[i] += 1
                    bigram_i = i
                    break
        #initialize bigram probability
        self.__biprob_no_smoothing = copy.deepcopy(self.__bicount)
        self.__biprob_add_one = copy.deepcopy(self.__bicount)
        self.__biprob_good_turing = copy.deepcopy(self.__bicount)
        print ("\n\nThe tables with the bigram counts is:\n")
        self.draw_table(self.__bicount, 1)
        print ("\n")

    def compute_probability(self):
        """
           To compute bigram probabilities,including the following algorithm:
           without smoothing,add-one smoothing,Good_Turing discounting
        """
        #1.without smoothing
        if self.__scenarios == '0' or self.__scenarios == '1':
            for i in range(len(self.__biprob_no_smoothing)) :
                for j in range(len(self.__biprob_no_smoothing)):
                    #1.0 used to change integer to decimal
                    if self.__unicount[i] != 0:
                        self.__biprob_no_smoothing[i][j] /= ( self.__unicount[i] * 1.0 )
                    else:
                        self.__biprob_no_smoothing[i][j] = 0
            print("The table of bigram probabilites without smoothing is:\n")
            self.draw_table( self.__biprob_no_smoothing ,0)
            print("\n")
            #compute the total probability of the input sentence
            prob = 1
            for i in range(len(self.__words)-1):
                for j in range(len(self.__words_no_repeat)):
                    if self.__words[i].lower() == self.__words_no_repeat[j]:
                        break
                for k in range(len(self.__words_no_repeat)):
                    if self.__words[i+1].lower() == self.__words_no_repeat[k]:
                        break
                prob *= self.__biprob_no_smoothing[j][k]
            # the probability of "<s> word"
            if self.__unicount[0] != 0:
                prob_s_word = self.__capital_num * 1.0 / self.__unicount[0]
                prob *= prob_s_word
            # the probability of "word </s>"
            for i in range(len(self.__words_no_repeat)):
                if self.__words[-1].lower() == self.__words_no_repeat[i]:
                    break
            if self.__unicount[i] != 0:
                prob_word_s = self.__last_num * 1.0 / self.__unicount[i]
                prob *= prob_word_s
            print ("The probabilty computed without smoothing is :")
            print ("%.2e" % prob)
            print("\n")

        #2.add-one smoothing
        if self.__scenarios == '0' or self.__scenarios == '2':
            for i in range(len(self.__biprob_add_one)) :
                for j in range(len(self.__biprob_add_one)):
                    #p* = (C(Wn-1Wn)+1)/(C(Wn-1)+V)
                    self.__biprob_add_one[i][j] = (self.__biprob_add_one[i][j]+\
                           1.0) / ( self.__unicount[i] + len(self.__vocabulary) )
            print("The table of bigram probabilites with add-one smoothing is:\n")
            self.draw_table( self.__biprob_add_one, 0)
            print("\n")
            #compute the total probability of the input sentence
            prob = 1
            for i in range(len(self.__words)-1):
                for j in range(len(self.__words_no_repeat)):
                    if self.__words[i].lower() == self.__words_no_repeat[j]:
                        break
                for k in range(len(self.__words_no_repeat)):
                    if self.__words[i+1].lower() == self.__words_no_repeat[k]:
                        break
                prob *= self.__biprob_add_one[j][k]
            # the probability of "<s> word"
            if self.__unicount[0] != 0:
                prob_s_word = self.__capital_num * 1.0 / self.__unicount[0]
                prob *= prob_s_word
            # the probability of "word </s>"
            for i in range(len(self.__words_no_repeat)):
                if self.__words[-1].lower() == self.__words_no_repeat[i]:
                    break
            if self.__unicount[i] != 0:
                prob_word_s = self.__last_num * 1.0 / self.__unicount[i]
                prob *= prob_word_s
            print ("The probabilty computed with add-one smoothing is :")
            print ("%.2e" % prob)
            print("\n")

        #3.Good-Turing Discounting
        if self.__scenarios == '0' or self.__scenarios == '3':
            for i in range(len(self.__biprob_good_turing)) :
                for j in range(len(self.__biprob_good_turing)):
                    #P* = N1/N                    , when c == 0
                    #P* = ((c+1)*N[c+1]/N[c]) / N , when c != 0
                    if self.__biprob_good_turing[i][j] == 0:
                        #compute N1
                        num_n1 = 0
                        for k in range(len(self.__nc_num[i])):
                            if self.__nc_num[i][k] == 1:
                                num_n1 += 1
                        if self.__unicount[i] != 0:
                            self.__biprob_good_turing[i][j] = num_n1 * 1.0 \
                                                      / self.__unicount[i]       
                    else:
                        #compute N[c+1]
                        num_ncp1 = 0
                        for k in range(len(self.__nc_num[i])):
                            if self.__nc_num[i][k] == self.__bicount[i][j] + 1:
                                num_ncp1 += 1
                        #compute N[c]
                        num_nc = 0
                        for k in range(len(self.__nc_num[i])):
                            if self.__nc_num[i][k] == self.__bicount[i][j]:
                                num_nc += 1
                        c_star = (self.__bicount[i][j] + 1) * num_ncp1 / num_nc 
                        self.__biprob_good_turing[i][j] = c_star * 1.0 \
                                                       / self.__unicount[i] 
            print("The table of bigram probabilites with Good-Turing discounting is:\n")
            self.draw_table( self.__biprob_good_turing, 0)
            print("\n")
            #compute the total probability of the input sentence
            prob = 1
            for i in range(len(self.__words)-1):
                for j in range(len(self.__words_no_repeat)):
                    if self.__words[i].lower() == self.__words_no_repeat[j]:
                        break
                for k in range(len(self.__words_no_repeat)):
                    if self.__words[i+1].lower() == self.__words_no_repeat[k]:
                        break
                prob *= self.__biprob_good_turing[j][k]
            # the probability of "<s> word"
            if self.__unicount[0] != 0:
                prob_s_word = self.__capital_num * 1.0 / self.__unicount[0]
                prob *= prob_s_word
            # the probability of "word </s>"
            for i in range(len(self.__words_no_repeat)):
                if self.__words[-1].lower() == self.__words_no_repeat[i]:
                    break
            if self.__unicount[i] != 0:
                prob_word_s = self.__last_num * 1.0 / self.__unicount[i]
                prob *= prob_word_s
            print ("The probabilty computed with Good-Turing discounting is :")
            print ("%.2e" % prob)
            print("\n")

if __name__ == '__main__':
    bg = BiGram("Corpus.txt")
    bg.receive_sentences_scenarios()
    bg.compute_count()
    bg.compute_probability()
