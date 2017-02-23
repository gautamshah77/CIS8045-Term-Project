# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:01:30 2017

@author: darsh
"""

import pandas as pd
import csv
from collections import Counter
import operator
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

import py2neo
from py2neo import Graph, Node, Relationship

py2neo.authenticate("localhost:7474", "neo4j", "termproject")

graph = Graph("http://localhost:7474/db/data/")

review = pd.read_csv('Desktop/Airline_data_partial.csv')
review.columns.values
print(review['reviewdate'])
review_index = 0

setAuthor = set(review['authorname'])
setAirline = set(review['airlinename'])
print(setAuthor)
print(setAirline)

for i in setAuthor:
    i = Node("Author", name=i)
    graph.create(i)
    
for j in setAirline:
    j = Node("Airline", name=j)
    graph.create(j)
    


'''
for i in range(0, len(review)):
    author
    review_index += 1 #Increases the row index
'''