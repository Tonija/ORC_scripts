#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open research Central (ORC) helper script for
creating WordEmbeddings for article reviews
@authors: Antonija Mijatovic (antonija.mijatovic@mefst.hr)
"""
#!pip install --upgrade gensim
import os
import sys
import gensim
import numpy as np
from nltk import sent_tokenize, word_tokenize
import csv
from gensim.test.utils import datapath
from nltk.corpus import stopwords

file_name = r'C:\Users\Korisnik\Desktop\ORC_script\ORC_results\commentsAndResponses_clean.xlsx'

df_all = pd.read_excel(io=file_name)
df = df_all.replace(np.nan, 'No data', regex=True)
print(df.head(15))

# Extract the reviews from the table:
comm_soc = df.loc[df["Area"] == 'Social', "Comments"]
comm_med = df.loc[df["Area"] == 'Medical', "Comments"]
social_comments = comm_soc.tolist()
medical_comments = comm_med.tolist()

# Tokenize the text and remove stopwords:
tokenized_med = [word_tokenize(i) for i in medical_comments]
tokenized_soc = [word_tokenize(i) for i in social_comments]

print(model.most_similar(positive=['data', 'source'], topn=5))

filtered_med = [] 
for j in tokenized_med:
    for w in j:
        if w not in stopwords.words('english') and w != 'I': 
            filtered_med.append(w) 
            
filtered_soc = [] 
for j in tokenized_soc:
    for w in j:
        if w not in stopwords.words('english') and w != 'I': 
            filtered_soc.append(w)

# Upload a pre-trained model:            
model = gensim.models.KeyedVectors.load_word2vec_format(datapath(r'C:\Users\Korisnik\Downloads\en_wiki_word2vec_300\en_wiki_word2vec_300.txt'), binary=False) 

# Create Word Embeddings for medical and social science article reviews separatelly
# and import the vectors to a TSV file 
with open('med_embeddings.tsv', 'w') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')
    for word in filtered_med:
        try:
            vector = model.get_vector(word).tolist()
            writer.writerow(vector)
        except:
            pass
            
with open('soc_embeddings.tsv', 'w') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')
    for word in filtered_soc:
        try:
            vector = model.get_vector(word).tolist()
            writer.writerow(vector)
        except:
            pass

# Create metadeta for medical and social science article reviews separatelly
# and import the data to a TSV file             
with open('soc_meta.tsv', 'w') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')
    writer.writerow('Social')
    for word in filtered_soc:
        try:
            vector = model.get_vector(word).tolist()
            print(word)
            writer.writerow([word])
        except:
            pass

with open('med_meta.tsv', 'w') as tsvfile:
    writer = csv.writer(tsvfile, delimiter='\t')
    writer.writerow('Medical')
    for word in filtered_med:
        try:
            vector = model.get_vector(word).tolist()
            print(word)
            writer.writerow([word])
        except:
            pass            