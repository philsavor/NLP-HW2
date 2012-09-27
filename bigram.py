import copy
import re
import textmanager

class BiGram:
    """
       represent a bigram
    """

    def __init__(self,file_name):
        self.__words = None
        self.__words_no_repeat = None
        self.__scenarios = None
        self.__unicount = []
        self.__bicount = []
        self.__vocabulary = []
        self.__nc = []
     	self.__nc_num = []
        #bigram probability
        self.__biprob_no_smoothing = []
        self.__biprob_add_one = []
        self.__biprob_good_turing = []
        #set file
        self.__tm = textmanager.TextManager()
        self.__tm.set_file(file_name)

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
        self.__scenarios = raw_input("please choose the scenarios:\n"\
                                    +"0.All;\n"\
                                    +"1.Without smoothing;\n"\
                                    +"2.With add-one smoothing;\n"\
                                    +"3.With Good-Turing discounting.\n")

    def compute_count(self):
        """
           To compute the bigram count and unigram count for further
           computation for probabilities.
        """
        words_count = len(self.__words_no_repeat)
        self.__unicount = [0] * words_count
        self.__bicount = [[0] * words_count for i in xrange(words_count)]

        bigram_i = None
        while 1:
            word = self.__tm.get_next_word()
            #end mark
            if word == None:
                break
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
        #test
        print self.__unicount
        print self.__bicount

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
            print self.__biprob_no_smoothing 
            #compute the total probability of the input sentence
            ###TODO:<s>,</s>
            prob = 1
            for i in range(len(self.__words)-1):
                for j in range(len(self.__words_no_repeat)):
                    if self.__words[i] == self.__words_no_repeat[j]:
                        break
                for k in range(len(self.__words_no_repeat)):
                    if self.__words[i+1] == self.__words_no_repeat[k]:
                        break
                print self.__words[i]
                print self.__biprob_no_smoothing[j][k]
                prob *= self.__biprob_no_smoothing[j][k]
            print prob

        #2.add-one smoothing
        if self.__scenarios == '0' or self.__scenarios == '2':
            for i in range(len(self.__biprob_add_one)) :
                for j in range(len(self.__biprob_add_one)):
                    #p* = (C(Wn-1Wn)+1)/(C(Wn-1)+V)
                    self.__biprob_add_one[i][j] = (self.__biprob_add_one[i][j]+\
                           1.0) / ( self.__unicount[i] + len(self.__vocabulary) )
            print self.__biprob_add_one
            #compute the total probability of the input sentence
            ###TODO:<s>,</s>
            prob = 1
            for i in range(len(self.__words)-1):
                for j in range(len(self.__words_no_repeat)):
                    if self.__words[i] == self.__words_no_repeat[j]:
                        break
                for k in range(len(self.__words_no_repeat)):
                    if self.__words[i+1] == self.__words_no_repeat[k]:
                        break
                print self.__words[i]
                print self.__biprob_add_one[j][k]
                prob *= self.__biprob_add_one[j][k]
            print prob

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
            print self.__biprob_good_turing
            #compute the total probability of the input sentence
            ###TODO:<s>,</s>
            prob = 1
            for i in range(len(self.__words)-1):
                for j in range(len(self.__words_no_repeat)):
                    if self.__words[i] == self.__words_no_repeat[j]:
                        break
                for k in range(len(self.__words_no_repeat)):
                    if self.__words[i+1] == self.__words_no_repeat[k]:
                        break
                print self.__words[i]
                print self.__biprob_good_turing[j][k]
                prob *= self.__biprob_good_turing[j][k]
            print prob

if __name__ == '__main__':
    bg = BiGram("Corpus.txt")
    bg.receive_sentences_scenarios()
    bg.compute_count()
    bg.compute_probability()
