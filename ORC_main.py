#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open research Central (ORC) document parser
Convert ORC XML documents to a standardized data structure
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
#!pip install PyPDF2
from PyPDF2 import PdfFileReader
import pandas as pd
import urllib
from urllib.request import urlopen

from ORC_getArticleInfo import *
from ORC_getChapters import *
from ORC_getReviewsInfo import *

#################
### VARIABLES ###
#################

reportID_fullNames=pd.DataFrame()
review_info = pd.DataFrame()
article_info = pd.DataFrame()
merged_tables = pd.DataFrame()

#################
### FUNCTIONS ###
#################

def get_totalWordNumber():
# Calculate total number of words in an article

    global imrd_length
    imrd_length = 0
    
    imrd_length = countImrdWords(root)
    print ("Number of imrd words: ", imrd_length)
    
    global article_length
    article_length = 0
    
    article_length = countAllWords(root)
    print ("Total number of words: ", article_length)
    
    # TODO: find out whether an article follows IMRD structure
    # and add into table new column IMRD_structue (True/False)
    
def merge_tables ():

    partial_info =  pd.DataFrame.merge(createMaterialsInfoDf(current_doi, pdfPagesNum, article_length), createImrdDf(current_doi), on='doi')
    print("\nPARTIAL INFO: ", partial_info)
    
    all_info = pd.DataFrame.merge(get_reviewersInfo(root), partial_info, on='doi')
    all_info.to_csv (r'C:\Users\Korisnik\Desktop\ORC_script\all_info.csv', mode='a', index = False, header=False, sep = ';')
    print("\nALL INFO TABLE: ", all_info)
    print("\nall_info table length: ", len(all_info))
    
    if len(all_info) == 0:
        partial_info.to_csv (r'C:\Users\Korisnik\Desktop\ORC_script\partial_info.csv', mode='a', index = False, header=False, sep = ';')

#def main():    
# Go to directory which contains filtered_xml_urls.csv files:
os.chdir("C:\\Users\\Korisnik\\Desktop\\ORC_script")

xml_urls = []
global pdfPagesNum
pdfPagesNum = []
global current_doi
current_doi = ""
global imrdList
imrdList = ['Abstract', 'Introduction', 'Method', 'Methods', 'Materials and methods', 'Subjects and methods', 'Result', 'Results', 
            'Discussion', 'Result and discussion', 'Results and discussion', 'Discussion and conclusion', 'Data availability', 'Conclusion', 'Conclusions', 
            'Conclusions and future directions',
            'Summary', 'Data availability']
 
with open('filtered_xml_urls.csv', 'r') as xml_f:
    reader = csv.reader(xml_f)
    for row in reader:
        xml_urls.append((" ".join(row)))
        
# xml_urls contains only last versions of artcles, add older versions as well:
for x in xml_urls:
    if x.endswith('2'):
        xml_urls.append(x[:-1] + str(1))
    if x.endswith('3'):
        xml_urls.append(x[:-1] + str(2))  
    if x.endswith('4'):
        xml_urls.append(x[:-1] + str(3))  

#for i in range(len(xml_urls)):
for i in range(0,19): # for testing purpose: test only a sample
    try:
        with urlopen(xml_urls[i]) as f:
            tree = ET.parse(f)
            global root
            root = tree.getroot()
            print(i)
            print("\nFile XML: " + xml_urls[i])
            temp_report = []
            isReviewed = False
            for elem in root.findall('.//sub-article[@article-type="ref-report"]/'):
                temp_report.append(elem.tag)
            if len(temp_report) != 0:
                isReviewed = True
            if not isReviewed:
                print("Article is waiting for review.")
            else:   
                pdf_str = xml_urls[i].replace('xml?doi', 'pdf?doi' )
                print("File PDF: ", pdf_str)
                with urllib.request.urlopen(pdf_str) as webFile:
                    remoteFile = webFile.read()
                    memoryFile = BytesIO(remoteFile)
                    pdfFile = PdfFileReader(memoryFile)
                    pdfPagesNum.append(pdfFile.numPages)
            
                for elem in root.find('.//article-id[@pub-id-type="doi"]').iter():
                    current_doi = elem.text                  
                    
                get_ResearchArea(current_doi)
                get_articleInfo(root) 
                get_MaterialsNo(root)
                get_totalWordNumber()
                get_authorsResponses(root)
                get_reviewsInfo(root, current_doi)               
                getChapterTitles(root, imrdList)
                #merge_tables()
                print('\n----------------------------------------')
    except:
        print("\nError")
        
# For HTTP 403 Error files:
for filename in os.listdir(r'C:\Users\Korisnik\Desktop\ORC_script\HTTP_403_files'):
    with open(os.path.join(r'C:\Users\Korisnik\Desktop\ORC_script\HTTP_403_files', filename)) as f:
        try:
            tree = ET.parse(f)
            root = tree.getroot()
            print("\nFile name: " , filename)
            temp_report = []
            isReviewed = False
            for elem in root.findall('.//sub-article[@article-type="ref-report"]/'):
                temp_report.append(elem.tag)
            if len(temp_report) != 0:
                isReviewed = True
            if not isReviewed:
                print("Article is waiting for review.")
            else:                   
                pdfPagesNum.append(-1) # add manually in table
            
                for elem in root.find('.//article-id[@pub-id-type="doi"]').iter():
                    current_doi = elem.text    
                    
                get_ResearchArea(current_doi)
                get_articleInfo(root) 
                get_MaterialsNo(root)
                get_totalWordNumber()
                get_authorsResponses(root)
                get_reviewsInfo(root, current_doi)
                getChapterTitles(root, imrdList)                
                #merge_tables()
                print('\n----------------------------------------')
        except:
            print("\nError with opening file: ", filename)
            print('\n----------------------------------------')                
                
#if __name__ == "__main__":
#    main()                