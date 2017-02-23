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

#graph.delete_all()

review = pd.read_csv('C:/Users/darsh/OneDrive/Documents/GitHub/CIS8045-Term-Project/Airline_data_partial.csv')
review.columns.values
print(review['reviewdate'])
review_index = 0
len(review)

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
    

for k in range(0, len(review)):
    graph.run("""MATCH (au{name:review.loc[review_index, 'authorname']}),(ai{name:review.loc[review_index, 'airlinename']}) 
                WITH au, ai
                CREATE (au)-[:RATED{authorcountry: review.loc[review_index, 'authorcountry'], 
                                    aircraft: review.loc[review_index, 'aircraft'],
                                    route: review.loc[review_index, 'route'],
                                    travellertype: review.loc[review_index, 'travellertype'],
                                    cabin: review.loc[review_index, 'cabin'],
                                    rating_cabinstaff: review.loc[review_index, 'rating_cabinstaff'],
                                    rating_foodbeverage: review.loc[review_index, 'rating_foodbeverage'],
                                    rating_inflightEnt: review.loc[review_index, 'rating_inflightEnt'],
                                    rating_overall: review.loc[review_index, 'rating_overall'],
                                    rating_seatcomfort: review.loc[review_index, 'rating_seatcomfort'],
                                    rating_valuemoney: review.loc[review_index, 'rating_valuemoney'],
                                    recommended: review.loc[review_index, 'recommended'],
                                    reviewcontent: review.loc[review_index, 'reviewcontent'],
                                    reviewdate: review.loc[review_index, 'reviewdate']}]->(ai)""")
    review_index += 1

