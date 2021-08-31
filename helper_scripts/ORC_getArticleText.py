# ARTICLE TEXT
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open research Central (ORC) helper script
Extract article texts
@authors: Antonija Mijatovic (antonija.mijatovic@mefst.hr)
"""
import string
import re
import os
import io
import csv
from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET
from io import BytesIO
import re
import pandas as pd
    
def getArticleBodyWords ():
# Extract article text
# The text is under tag: <article><body>
    
    bodyText = []
    bodyTextChapter = []
    bodyText_str = ""
    brackets = '''()[]{}<>'''

    for a in root.findall('.//body/sec/p'):
        bodyText.append(a.text)
        bodyText.append(a.tail)
    for a in root.findall('.//body/sec/p/underline'):
        bodyText.append(a.text)
        bodyText.append(a.tail)    
    for a in root.findall('.//body/sec/p/italic'):
        bodyText.append(a.text)
        bodyText.append(a.tail)
    for a in root.findall('.//body/sec/p/bold'):
        bodyText.append(a.text)
        bodyText.append(a.tail) 
    for a in root.findall('.//body/sec/p/bold/italic'):
        bodyText.append(a.text)
        bodyText.append(a.tail) 
    for a in root.findall('.//body/sec/p/italic/bold'):
        bodyText.append(a.text)
        bodyText.append(a.tail)        
    for a in root.findall('.//body/sec/p/boxed-text/caption/title'):
        bodyText.append(a.text)
        bodyText.append(a.tail)
    for a in root.findall('.//body/sec/p/boxed-text/p'):
        bodyText.append(a.text)
        bodyText.append(a.tail)  
    for a in root.findall('.//body/sec/p/xref'):
        bodyText.append(a.text)
        bodyText.append(a.tail) 
    for a in root.findall('.//body/sec/p/xref/italic'):
        bodyText.append(a.text)
        bodyText.append(a.tail)         
    for a in root.findall('.//body/sec/p/xref/'):
        if a.text not in bodyText:
            bodyText.append(a.text)
        if a.tail not in bodyText:    
            bodyText.append(a.tail) 
    for a in root.findall('.//body/sec/list/list-item/p'):
        bodyText.append(a.text)
        bodyText.append(a.tail) 
    for a in root.findall('.//body/sec/list/list-item/p/italic'):
        bodyText.append(a.text)
        bodyText.append(a.tail) 
    for a in root.findall('.//body/sec/list/list-item/p/bold'):
        bodyText.append(a.text)
        bodyText.append(a.tail)  
    for a in root.findall('.//body/sec/list/list-item/p/italic/bold'):
        bodyText.append(a.text)
        bodyText.append(a.tail)  
    for a in root.findall('.//body/sec/list/list-item/p/bold/italic'):
        bodyText.append(a.text)
        bodyText.append(a.tail)
    # Subsections:
    for a in root.findall('.//body/sec/sec/p'):
        bodyText.append(a.text)
        bodyText.append(a.tail)
    for a in root.findall('.//body/sec/sec/p/underline'):
        bodyText.append(a.text)
        bodyText.append(a.tail)    
    for a in root.findall('.//body/sec/sec/p/italic'):
        bodyText.append(a.text)
        bodyText.append(a.tail)
    for a in root.findall('.//body/sec/sec/p/bold'):
        bodyText.append(a.text)
        bodyText.append(a.tail) 
    for a in root.findall('.//body/sec/sec/p/bold/italic'):
        bodyText.append(a.text)
        bodyText.append(a.tail) 
    for a in root.findall('.//body/sec/sec/p/italic/bold'):
        bodyText.append(a.text)
        bodyText.append(a.tail)        
    for a in root.findall('.//body/sec/sec/p/boxed-text/caption/title'):
        bodyText.append(a.text)
        bodyText.append(a.tail)
    for a in root.findall('.//body/sec/sec/p/boxed-text/p'):
        bodyText.append(a.text)
        bodyText.append(a.tail) 
    for a in root.findall('.//body/sec/sec/p/boxed-text/p/italic'):
        bodyText.append(a.text)
        bodyText.append(a.tail) 
    for a in root.findall('.//body/sec/sec/p/boxed-text/p/bold'):
        bodyText.append(a.text)
        bodyText.append(a.tail) 
    for a in root.findall('.//body/sec/sec/p/boxed-text/p/italic/bold'):
        bodyText.append(a.text)
        bodyText.append(a.tail)         
    for a in root.findall('.//body/sec/sec/p/boxed-text/p/bold/italic'):
        bodyText.append(a.text)
        bodyText.append(a.tail)         
    for a in root.findall('.//body/sec/sec/p/xref'):
        bodyText.append(a.text)
        bodyText.append(a.tail)
    for a in root.findall('.//body/sec/sec/p/xref/italic'):
        bodyText.append(a.text)
        bodyText.append(a.tail)    
    for a in root.findall('.//body/sec/sec/p/sup'):
        bodyText.append(a.text)
        bodyText.append(a.tail)     
    for a in root.findall('.//body/sec/sec/sup'):
        bodyText.append(a.text)
        bodyText.append(a.tail)             
    for a in root.findall('.//body/sec/sec/p/xref/'):
        if a.text not in bodyText:
            bodyText.append(a.text)
        if a.text == 'et al':
            bodyText.append(a.text)      
        if a.tail not in bodyText:    
            bodyText.append(a.tail) 
    for a in root.findall('.//body/sec/sec/p/sup/ext-link'):
        bodyText.append(a.text)
        bodyText.append(a.tail) 
    for a in root.findall('.//body/sec/sec/p/ext-link'):
        bodyText.append(a.text)
        bodyText.append(a.tail)         
    for a in root.findall('.//body/sec/sec/list/list-item/p'):
        bodyText.append(a.text)
        bodyText.append(a.tail) 
    for a in root.findall('.//body/sec/sec/list/list-item/p/italic'):
        bodyText.append(a.text)
        bodyText.append(a.tail) 
    for a in root.findall('.//body/sec/sec/list/list-item/p/bold'):
        bodyText.append(a.text)
        bodyText.append(a.tail)  
    for a in root.findall('.//body/sec/sec/list/list-item/p/italic/bold'):
        bodyText.append(a.text)
        bodyText.append(a.tail)
    for a in root.findall('.//body/sec/sec/list/list-item/p/bold/italic'):
        bodyText.append(a.text)
        bodyText.append(a.tail)
    for a in root.findall('.//body/sec/sec/p/'):
        if a.text not in bodyText:
            bodyText.append(a.text)
        if a.tail not in bodyText:    
            bodyText.append(a.tail)           
    for a in root.findall('.//body/sec/p/'):
        if a.text not in bodyText:
            bodyText.append(a.text)
        if a.tail not in bodyText:    
            bodyText.append(a.tail)       
            
    for val in bodyText: 
        if val != None : 
            bodyTextChapter.append(val)

    bodyText_str = ''.join(bodyTextChapter)
    bodyText_str = bodyText_str.replace("\n","");
    bodyTextChapter = bodyText_str.split()

    bodyTextChapter = [''.join(c for c in s if c not in string.punctuation) for s in bodyTextChapter]
    bodyTextChapter = [s for s in bodyTextChapter if s]     

    # Additional cleaning:
    article_text = []
    for e in bodyTextChapter:
        if e != '.' and e != ',' and e != '–' and e != '=':
            article_text.append(e)
    
    text_df = pd.DataFrame({'doi':[current_doi],
                            'articleText': [' '.join(article_text)]})
    
    print("\nArticle body text: ", text_df) 
    text_df.to_csv(r'C:\Users\Korisnik\Desktop\ORC_script\article_text.csv', mode='a', index = False, header=False, sep = ';')
    
#def main():    

os.chdir("C:\\Users\\Korisnik\\Desktop\\ORC_script")

global current_doi
current_doi = ""

iteration = 1
for filename in os.listdir(r'C:\Users\Korisnik\Desktop\ORC_script\ORC_xml_files\ORC_xml_files_latest'):
    with open(os.path.join(r'C:\Users\Korisnik\Desktop\ORC_script\ORC_xml_files\ORC_xml_files_latest', filename), encoding="utf-8") as f:
        print("\nFile name: " , filename)
        tree = ET.parse(f)
        global root
        root = tree.getroot()
        print(iteration)    

        temp_report = []
        for elem in root.findall('.//sub-article[@article-type="ref-report"]/'):
            temp_report.append(elem.tag)
        if len(temp_report) == 0:
            print("Article is waiting for review.")
        else:
            for elem in root.find('.//article-id[@pub-id-type="doi"]').iter():
                current_doi = elem.text                  
            
            getArticleBodyWords()
            print('\n----------------------------------------')
    iteration = iteration + 1 