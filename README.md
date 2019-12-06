# basic-sentiment-analysis
Basic Sentiment Analysis Project

to run, use sentimentanalysis.py file.

This program processes the input text file, cleans it up, breaks it into sentences line by line, then into words. It then compares each word to the other two files, 't' which is the positive words file, and 'u' which is the negative words file. 
If the word exists in the positive file, it counts it as a positive word, if the word exists in the negative file, it counts it as a negative word. If the the word is not part of either list, it is considered a neutral word.
The program returns how many times a Negative, Positive, and Neutral word was in the input text. 