import re
import sys

class TextManager :
    """ 
    To get word one by one 
    """
    def __init__(self) :     
        self.file = None 
        self.lines = None 
        self.line_count = 0
        self.word_count = 0 
        self.max_line_count = 0 
        self.max_word_count = 0 
        #represent each line
        self.line = None   
        #It is a list containing each word from a certain line
        self.words = None 

    def reset(self):
        self.file = None 
        self.lines = None 
        self.line_count = 0
        self.word_count = 0 
        self.max_line_count = 0 
        self.max_word_count = 0 
        #represent each line
        self.line = None   
        #It is a list containing each word from a certain line
        self.words = None 
        
    
    def set_file(self, file_name):
        """
        set_file used to set the file for the class and do some
        initial things.
        """
        try:
            self.file = open(file_name)
            self.lines = self.file.readlines()
            self.max_line_count = len(self.lines)
        except IOError as e:
            print ("I/O error({0}): {1}".format(e.errno, e.strerror))
            print ("Please try again!!!\n")
            raise

    def test_put_out(self) :
        """
        just for test
        """
        line_string = self.lines[self.line_count] 
        if line_string != '\n' : 
             print (line_string)
        words = re.findall(r'\w+', line_string)
        for word in words :
            print (word)
        self.line_count += 1
  
    def _get_next_line(self) :
         """
         To get a new line, if there is no new line return None,
         else return the string fo the new line.
         """
         while 1:
             if self.line_count == self.max_line_count:
                 return None 
             else:
                 line = self.lines[self.line_count]
                 self.line_count += 1
                 if line == "\n":
                     continue
                 else:
                     return line

    def get_next_word(self) :
         """
         To get a new word, if there is no new word ,return None.
         """
         if self.file == None:
              return "ERROR:you should tell me the file name"
         #initial state
         if self.line == None: 
              self.line = self._get_next_line()
              if self.line == None:
                  return None
              self.words = re.findall(r'\w+', self.line)
              self.max_word_count = len(self.words)
         if self.word_count != self.max_word_count:
              word = self.words[self.word_count] 
              self.word_count += 1
              return word
         else:
              self.line = self._get_next_line()
              if self.line == None:
                  return None 
              self.words = re.findall(r'\w+', self.line)
              #reset the max_wor_count & word_count value
              self.max_word_count = len(self.words)  
              self.word_count = 0
              word = self.words[self.word_count]
              self.word_count += 1
              return word
              #return '\n'

