NLP-HomeWork2
=======

[OVERVIEW]
This program implement a bigram language model, which is trained on Corpus.txt.The input of this program is a sentence and a scenarios,which can be without smoothing ,with add-one smoothing and with Good-Turing discounting. The result is the table with the bigram counts and bigram probability and the total probability for the input sentence.

[PLATFORM]
OS:     GNU/Linux
python: 2.7.3

[TEST CASE]
I use two following sentences as test case.
S1.The company chairman said he will increase the profit next year.
S2.The president said he believes the last year profit were good.

Based on the result of the program, the probability of S1 is bigger.

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

