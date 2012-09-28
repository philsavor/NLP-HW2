NLP-HomeWork2
=============

[OVERVIEW]
This program implement a bigram language model, which is trained on Corpus.txt.The input of this program is a sentence and a scenarios,which can be without smoothing ,with add-one smoothing and with Good-Turing discounting. The result is the table with the bigram counts and bigram probability and the total probability for the input sentence.

[PLATFORM]
OS:     GNU/Linux
python: 2.7.3

[FILES]:
1.bigram.py:
The main file, implement the algorithms to compute the bigram counts , bigram probabilities and the total probabilities for input sentence.

2.textmanager.py
This file is used to provide word one by one, these word are from Corpus.txt.

3.Corpus.txt
Used to train the bigram language model.

4.README.md
Readme manual.

[HOW TO USE]:
For Linux:
1.Python bigram.py;
2.Input the sentence;
3.Choose the scenarios;

[TEST CASE]
I use two following sentences as test case.
S1.<s>The company chairman said he will increase the profit next year.</s>
S2.<s>The president said he believes the last year profit were good.</s>

Based on the result of the program, the probability of S1 is bigger.

Test Case Result:
-----------------
S1.<s>The company chairman said he will increase the profit next year.</s>


The tables with the bigram counts is:

            the       company   chairman  said      he        will      increase  profit    next      year      
the         0000      0093      0042      0000      0000      0000      0000      0000      0007      0003      
company     0006      0000      0000      0008      0001      0000      0000      0000      0000      0000      
chairman    0004      0000      0001      0024      0002      0001      0000      0000      0000      0000      
said        0035      0000      0000      0000      0021      0000      0000      0000      0000      0000      
he          0000      0000      0000      0005      0000      0007      0000      0000      0000      0000      
will        0000      0000      0000      0000      0001      0000      0000      0000      0000      0000      
increase    0000      0000      0000      0000      0000      0000      0000      0000      0000      0000      
profit      0000      0000      0000      0000      0000      0000      0000      0000      0000      0000      
next        0000      0000      0000      0000      0000      0000      0000      0000      0000      0006      
year        0001      0000      0000      0001      0000      0000      0001      0000      0000      0000      


The table of bigram probabilites without smoothing is:

            the          company      chairman     said         he           will         increase     profit       next         year         
the         0.00e+00     5.87e-02     2.65e-02     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     4.42e-03     1.90e-03     
company     4.05e-02     0.00e+00     0.00e+00     5.41e-02     6.76e-03     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     
chairman    7.01e-03     0.00e+00     1.75e-03     4.20e-02     3.50e-03     1.75e-03     0.00e+00     0.00e+00     0.00e+00     0.00e+00     
said        1.25e-01     0.00e+00     0.00e+00     0.00e+00     7.47e-02     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     
he          0.00e+00     0.00e+00     0.00e+00     4.13e-02     0.00e+00     5.79e-02     0.00e+00     0.00e+00     0.00e+00     0.00e+00     
will        0.00e+00     0.00e+00     0.00e+00     0.00e+00     8.70e-03     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     
increase    0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     
profit      0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     
next        0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     2.86e-01     
year        1.69e-02     0.00e+00     0.00e+00     1.69e-02     0.00e+00     0.00e+00     1.69e-02     0.00e+00     0.00e+00     0.00e+00     


The probabilty computed without smoothing is :
0.00e+00


The table of bigram probabilites with add-one smoothing is:

            the          company      chairman     said         he           will         increase     profit       next         year         
the         1.52e-04     1.43e-02     6.54e-03     1.52e-04     1.52e-04     1.52e-04     1.52e-04     1.52e-04     1.22e-03     6.08e-04     
company     1.36e-03     1.95e-04     1.95e-04     1.75e-03     3.89e-04     1.95e-04     1.95e-04     1.95e-04     1.95e-04     1.95e-04     
chairman    8.99e-04     1.80e-04     3.60e-04     4.49e-03     5.39e-04     3.60e-04     1.80e-04     1.80e-04     1.80e-04     1.80e-04     
said        6.83e-03     1.90e-04     1.90e-04     1.90e-04     4.17e-03     1.90e-04     1.90e-04     1.90e-04     1.90e-04     1.90e-04     
he          1.96e-04     1.96e-04     1.96e-04     1.17e-03     1.96e-04     1.56e-03     1.96e-04     1.96e-04     1.96e-04     1.96e-04     
will        1.96e-04     1.96e-04     1.96e-04     1.96e-04     3.92e-04     1.96e-04     1.96e-04     1.96e-04     1.96e-04     1.96e-04     
increase    2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     
profit      2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     
next        1.99e-04     1.99e-04     1.99e-04     1.99e-04     1.99e-04     1.99e-04     1.99e-04     1.99e-04     1.99e-04     1.40e-03     
year        3.96e-04     1.98e-04     1.98e-04     3.96e-04     1.98e-04     1.98e-04     3.96e-04     1.98e-04     1.98e-04     1.98e-04     


The probabilty computed with add-one smoothing is :
8.83e-34


The table of bigram probabilites with Good-Turing discounting is:

            the          company      chairman     said         he           will         increase     profit       next         year         
the         3.24e-01     0.00e+00     0.00e+00     3.24e-01     3.24e-01     3.24e-01     3.24e-01     3.24e-01     1.90e-03     1.26e-03     
company     0.00e+00     3.18e-01     3.18e-01     0.00e+00     0.00e+00     3.18e-01     3.18e-01     3.18e-01     3.18e-01     3.18e-01     
chairman    5.25e-03     1.28e-01     0.00e+00     0.00e+00     0.00e+00     0.00e+00     1.28e-01     1.28e-01     1.28e-01     1.28e-01     
said        0.00e+00     2.81e-01     2.81e-01     2.81e-01     0.00e+00     2.81e-01     2.81e-01     2.81e-01     2.81e-01     2.81e-01     
he          3.39e-01     3.39e-01     3.39e-01     2.48e-02     3.39e-01     0.00e+00     3.39e-01     3.39e-01     3.39e-01     3.39e-01     
will        2.70e-01     2.70e-01     2.70e-01     2.70e-01     0.00e+00     2.70e-01     2.70e-01     2.70e-01     2.70e-01     2.70e-01     
increase    4.29e-01     4.29e-01     4.29e-01     4.29e-01     4.29e-01     4.29e-01     4.29e-01     4.29e-01     4.29e-01     4.29e-01     
profit      8.00e-01     8.00e-01     8.00e-01     8.00e-01     8.00e-01     8.00e-01     8.00e-01     8.00e-01     8.00e-01     8.00e-01     
next        4.29e-01     4.29e-01     4.29e-01     4.29e-01     4.29e-01     4.29e-01     4.29e-01     4.29e-01     4.29e-01     0.00e+00     
year        0.00e+00     4.75e-01     4.75e-01     0.00e+00     4.75e-01     4.75e-01     0.00e+00     4.75e-01     4.75e-01     4.75e-01     


The probabilty computed with Good-Turing discounting is :
0.00e+00

===============================================================

S2.<s>The president said he believes the last year profit were good.</s>


The tables with the bigram counts is:

            the       president said      he        believes  last      year      profit    were      good      
the         0000      0004      0000      0000      0000      0004      0003      0000      0000      0000      
president   0002      0000      0002      0000      0000      0000      0000      0000      0000      0000      
said        0035      0000      0000      0021      0000      0000      0000      0000      0000      0000      
he          0000      0000      0005      0000      0001      0000      0000      0000      0000      0000      
believes    0001      0000      0000      0000      0000      0000      0000      0000      0000      0000      
last        0000      0000      0000      0000      0000      0000      0004      0000      0000      0000      
year        0001      0000      0001      0000      0000      0000      0000      0000      0000      0000      
profit      0000      0000      0000      0000      0000      0000      0000      0000      0000      0000      
were        0001      0000      0000      0000      0000      0001      0000      0000      0000      0000      
good        0000      0000      0000      0000      0000      0000      0000      0000      0000      0000      


The table of bigram probabilites without smoothing is:

            the          president    said         he           believes     last         year         profit       were         good         
the         0.00e+00     2.53e-03     0.00e+00     0.00e+00     0.00e+00     2.53e-03     1.90e-03     0.00e+00     0.00e+00     0.00e+00     
president   2.06e-02     0.00e+00     2.06e-02     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     
said        1.25e-01     0.00e+00     0.00e+00     7.47e-02     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     
he          0.00e+00     0.00e+00     4.13e-02     0.00e+00     8.26e-03     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     
believes    1.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     
last        0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     1.21e-01     0.00e+00     0.00e+00     0.00e+00     
year        1.69e-02     0.00e+00     1.69e-02     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     
profit      0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     
were        2.08e-02     0.00e+00     0.00e+00     0.00e+00     0.00e+00     2.08e-02     0.00e+00     0.00e+00     0.00e+00     0.00e+00     
good        0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     0.00e+00     


The probabilty computed without smoothing is :
0.00e+00


The table of bigram probabilites with add-one smoothing is:

            the          president    said         he           believes     last         year         profit       were         good         
the         1.52e-04     7.60e-04     1.52e-04     1.52e-04     1.52e-04     7.60e-04     6.08e-04     1.52e-04     1.52e-04     1.52e-04     
president   5.90e-04     1.97e-04     5.90e-04     1.97e-04     1.97e-04     1.97e-04     1.97e-04     1.97e-04     1.97e-04     1.97e-04     
said        6.83e-03     1.90e-04     1.90e-04     4.17e-03     1.90e-04     1.90e-04     1.90e-04     1.90e-04     1.90e-04     1.90e-04     
he          1.96e-04     1.96e-04     1.17e-03     1.96e-04     3.91e-04     1.96e-04     1.96e-04     1.96e-04     1.96e-04     1.96e-04     
believes    4.01e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     
last        1.99e-04     1.99e-04     1.99e-04     1.99e-04     1.99e-04     1.99e-04     9.95e-04     1.99e-04     1.99e-04     1.99e-04     
year        3.96e-04     1.98e-04     3.96e-04     1.98e-04     1.98e-04     1.98e-04     1.98e-04     1.98e-04     1.98e-04     1.98e-04     
profit      2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     
were        3.97e-04     1.98e-04     1.98e-04     1.98e-04     1.98e-04     3.97e-04     1.98e-04     1.98e-04     1.98e-04     1.98e-04     
good        2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     2.00e-04     


The probabilty computed with add-one smoothing is :
0.00e+00


The table of bigram probabilites with Good-Turing discounting is:

            the          president    said         he           believes     last         year         profit       were         good         
the         3.24e-01     2.53e-03     3.24e-01     3.24e-01     3.24e-01     2.53e-03     1.26e-03     3.24e-01     3.24e-01     3.24e-01     
president   0.00e+00     2.16e-01     0.00e+00     2.16e-01     2.16e-01     2.16e-01     2.16e-01     2.16e-01     2.16e-01     2.16e-01     
said        0.00e+00     2.81e-01     2.81e-01     0.00e+00     2.81e-01     2.81e-01     2.81e-01     2.81e-01     2.81e-01     2.81e-01     
he          3.39e-01     3.39e-01     2.48e-02     3.39e-01     0.00e+00     3.39e-01     3.39e-01     3.39e-01     3.39e-01     3.39e-01     
believes    0.00e+00     1.00e+00     1.00e+00     1.00e+00     1.00e+00     1.00e+00     1.00e+00     1.00e+00     1.00e+00     1.00e+00     
last        3.94e-01     3.94e-01     3.94e-01     3.94e-01     3.94e-01     3.94e-01     0.00e+00     3.94e-01     3.94e-01     3.94e-01     
year        0.00e+00     4.75e-01     0.00e+00     4.75e-01     4.75e-01     4.75e-01     4.75e-01     4.75e-01     4.75e-01     4.75e-01     
profit      8.00e-01     8.00e-01     8.00e-01     8.00e-01     8.00e-01     8.00e-01     8.00e-01     8.00e-01     8.00e-01     8.00e-01     
were        0.00e+00     7.50e-01     7.50e-01     7.50e-01     7.50e-01     0.00e+00     7.50e-01     7.50e-01     7.50e-01     7.50e-01     
good        1.00e+00     1.00e+00     1.00e+00     1.00e+00     1.00e+00     1.00e+00     1.00e+00     1.00e+00     1.00e+00     1.00e+00     


The probabilty computed with Good-Turing discounting is :
0.00e+00




-
