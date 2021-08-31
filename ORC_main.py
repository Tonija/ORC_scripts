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
import pandas as pd

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
    
def merge_tables ():

    partial_info = pd.DataFrame()
    all_info = pd.DataFrame()

    partial_info = pd.DataFrame.merge(createMaterialsInfoDf(current_doi, article_length), createImrdDf(current_doi), on='doi').merge(getChapterTitles(root, current_doi), on='doi')
    print("\nPartial table:\n", partial_info)
    
    # ONLY FOR articleInfo for latest versions of articles:
    partial_info.to_csv (r'C:\Users\Korisnik\Desktop\ORC_script\ORC_results\articleInfo_latestVer.csv', mode='a', index = False, header=False, sep = ';')
    
    # ALL INFO (including reviewers' info)
    #all_info = pd.DataFrame.merge(partial_info, get_reviewersInfo(root), on='doi')
    #all_info.to_csv (r'C:\Users\Korisnik\Desktop\ORC_script\problem_previousVer.csv', mode='a', index = False, header=False, sep = ';')
    #print("\nALL INFO TABLE:\n", all_info)
    #print("\nall_info table length: ", len(all_info))
    
    #if len(all_info) == 0:
    #    partial_info.to_csv (r'C:\Users\Korisnik\Desktop\ORC_script\problem_previousVer.csv', mode='a', index = False, header=False, sep = ';')                
                       
############
### MAIN ###
############

#def main():    

#pd.options.display.max_colwidth = 200

# Go to directory which contains filtered_xml_urls.csv files:
os.chdir("C:\\Users\\Korisnik\\Desktop\\ORC_script")

global current_doi
current_doi = ""
global imrdList

iteration = 1
for filename in os.listdir(r'C:\Users\Korisnik\Desktop\ORC_script\ORC_xml_files\ORC_xml_files_latest'):
    with open(os.path.join(r'C:\Users\Korisnik\Desktop\ORC_script\ORC_xml_files\ORC_xml_files_latest', filename),"rt",encoding="utf-8") as f:
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
                
            get_ResearchArea(current_doi)
            get_articleInfo(root) 
            get_MaterialsNo(root)
            get_totalWordNumber()
            get_authorsResponses(root)
            get_reviewsInfo(root, current_doi)
            merge_tables()
            print('\n----------------------------------------')
    iteration = iteration + 1
    
#if __name__ == "__main__":
#    main()                