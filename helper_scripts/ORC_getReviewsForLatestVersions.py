#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open research Central (ORC) helper script
Get article reviews and authors responses
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
from difflib import SequenceMatcher

#################
### VARIABLES ###
#################

review_info = pd.DataFrame()

#################
### FUNCTIONS ###
#################

def get_ResearchArea(current_doi):

    medDOI_file = open("orc_med_doi.csv", "r")
    socDOI_file = open("orc_soc_doi.csv", "r")
    
    global research_area
    research_area = ""     

    for line in medDOI_file:
        values = line.split()
        if current_doi in line:
            print("Subject Area: Medicine and health sciences")
            research_area = "Medical"
                    
    for line in socDOI_file:
        values = line.split()
        if current_doi in line:
            print("Subject Area: Social sciences")
            research_area = "Social"        

    medDOI_file.close()
    socDOI_file.close()
    
def get_allCommResp (): 
# Get all reviewer's comments in an article and merge them into one list
# Get all authors' responses in an article and merge them into one list

    # Get all reviewers' comments:
    global allComments
    allComments = []
    for el in root.findall('.//sub-article[@article-type="ref-report"]/body/p'):
        allComments.append(el.text)
        allComments.append(el.tail)
    for el in root.findall('.//sub-article[@article-type="ref-report"]/body/p/bold'):
        allComments.append(el.text)
        allComments.append(el.tail)
    for el in root.findall('.//sub-article[@article-type="ref-report"]/body/p/italic'):
        allComments.append(el.text)
        allComments.append(el.tail)
    for el in root.findall('.//sub-article[@article-type="ref-report"]/body/p/italic/bold'):
        allComments.append(el.text)
        allComments.append(el.tail)
    for el in root.findall('.//sub-article[@article-type="ref-report"]/body/p/bold/italic'):
        allComments.append(el.text)
        allComments.append(el.tail)     
    for el in root.findall('.//sub-article[@article-type="ref-report"]/body/p/underline'):
        allComments.append(el.text)
        allComments.append(el.tail)    
    for el in root.findall('.//sub-article[@article-type="ref-report"]/body/p/list/list-item/p'):
        allComments.append(el.text)
        allComments.append(el.tail)
    for el in root.findall('.//sub-article[@article-type="ref-report"]/body/p/list/list-item/p/bold'):
        allComments.append(el.text)
        allComments.append(el.tail) 
    for el in root.findall('.//sub-article[@article-type="ref-report"]/body/p/list/list-item/p/italic'):
        allComments.append(el.text)
        allComments.append(el.tail)
    for el in root.findall('.//sub-article[@article-type="ref-report"]/body/p/xref'):
        allComments.append(el.text)
        allComments.append(el.tail) 
    for el in root.findall('.//sub-article[@article-type="ref-report"]/body/sec/sec/p/xref/'):
        if el.text not in allComments:
            allComments.append(el.text)    
        if elem.tail not in allComments:    
            allComments.append(el.tail)                  
    for el in root.findall('.//sub-article[@article-type="ref-report"]/body/p/'):
        if el.text not in allComments:
            allComments.append(el.text)
        if el.tail not in allComments:    
            allComments.append(el.tail)

    # Get all authors' responses:
    global allResponses
    allResponses = []
    for elem in root.findall('.//sub-article[@article-type="response"]/body/p'):
        allResponses.append(elem.text)
        allResponses.append(elem.tail)
    for elem in root.findall('.//sub-article[@article-type="response"]/body/p/bold'):
        allResponses.append(elem.text) 
        allResponses.append(elem.tail)
    for elem in root.findall('.//sub-article[@article-type="response"]/body/p/italic'):
        allResponses.append(elem.text) 
        allResponses.append(elem.tail)
    for elem in root.findall('.//sub-article[@article-type="response"]/body/p/italic/underline'):
        allResponses.append(elem.text) 
        allResponses.append(elem.tail)                
    for elem in root.findall('.//sub-article[@article-type="response"]/body/p/list/list-item/p'):
        allResponses.append(elem.text) 
        allResponses.append(elem.tail) 
    for elem in root.findall('.//sub-article[@article-type="response"]/body/p/list/list-item/p/bold'):
        allResponses.append(elem.text) 
        allResponses.append(elem.tail) 
    for elem in root.findall('.//sub-article[@article-type="response"]/body/p/list/list-item/p/italic'):
        allResponses.append(elem.text) 
        allResponses.append(elem.tail)
    for elem in root.findall('.//sub-article[@article-type="response"]/body/p/ext-link'):
        allResponses.append(elem.text) 
        allResponses.append(elem.tail)    
    for elem in root.findall('.//sub-article[@article-type="response"]/body/sec/sec/p/xref'):
        allResponses.append(elem.text)    
        allResponses.append(elem.tail)      
    for elem in root.findall('.//sub-article[@article-type="response"]/body/sec/sec/p/xref/'):
        if elem.text not in allResponses:
            allResponses.append(elem.text)    
        if elem.tail not in allResponses:   
            allResponses.append(elem.tail)             
    for elem in root.findall('.//sub-article[@article-type="response"]/body/p/'):
        if elem.text not in allResponses:
            allResponses.append(elem.text)
        if elem.tail not in allResponses:    
            allResponses.append(elem.tail)

    # Find matching sentences (remove reviewers' comments from authors' responses):
    simmilarity = []
    for com in allComments:
        for res in allResponses:
            if (SequenceMatcher(None, com, res).ratio() > 0.9):
                simmilarity.append(res)               
    responses_new = []
    for val in allResponses:
        if val not in simmilarity:
            responses_new.append(val)

    # Clean the reviews text:
    allComm = []
    for val in allComments: 
        if val != None : 
            allComm.append(val)

    allComm_str = ""
    allComm_str = ''.join(allComm)
    allComm = allComm_str.split()

    allComm = [''.join(c for c in s if c not in string.punctuation) for s in allComm]
    allComm = [s for s in allComm if s]     

    # Additional cleaning:
    allComm_clean = []
    for e in allComm:
        if e != '.' and e != ',' and e != '–' and e != '=':
            allComm_clean.append(e)  
    
    # Clean the responses text:    
    allResp = []
    for val in responses_new: 
        if val != None : 
            allResp.append(val)

    allResp_str = ""
    allResp_str = ''.join(allResp)
    allResp_str = allResp_str.replace("\n","");
    allResp = allResp_str.split()

    allResp = [''.join(c for c in s if c not in string.punctuation) for s in allResp]
    allResp = [s for s in allResp if s]     

    # Additional cleaning:
    allResp_clean = []
    for e in allResp:
        if e != '.' and e != ',' and e != '–' and e != '=':
            allResp_clean.append(e) 

    comments_df = pd.DataFrame({'doi': [current_doi],
                                'research_area': [research_area],
                                'comments': [' '.join(allComm_clean)],
                                'responses': [' '.join(allResp_clean)]})
    
    print("\nAll reviews and responses: ", comments_df) 
    comments_df.to_csv(r'C:\Users\Korisnik\Desktop\ORC_script\comments_latestVer_new.csv', mode='a', index = False, header=False, sep = ';')        
             

#def main():
os.chdir("C:\\Users\\Korisnik\\Desktop\\ORC_script")

global current_doi
current_doi = ""

iteration = 1
for filename in os.listdir(r'C:\Users\Korisnik\Desktop\ORC_script\ORC_xml_files_latest'):
    with open(os.path.join(r'C:\Users\Korisnik\Desktop\ORC_script\ORC_xml_files_latest', filename), encoding="utf-8") as f:
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
            get_allCommResp()
            print('\n----------------------------------------')
    iteration = iteration + 1

#if __name__ == "__main__":
#    main()       