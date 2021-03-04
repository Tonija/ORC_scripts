import string
import re
import os
import io
from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET
from io import BytesIO
#!pip install PyPDF2
from PyPDF2 import PdfFileReader
import pandas as pd
from urllib.request import urlopen
import itertools

import getImrdChapters
#import getNonImrdChapters
import getReviewsInfo
import getGeneralArticleInfo

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

def reset_variables ():
# Empty the lists

    global ref_names
    ref_names = []
    global ref_surnames
    ref_surnames = []
    global ref_fullName
    ref_fullName = []
    global gender_prob
    gender_prob = []
    global versionNo
    versionNo = []
    global refRecomm
    refRecomm = []
    global recomm_day
    recomm_day = []
    global recomm_month
    recomm_month = []
    global recomm_year
    recomm_year = []
    global day_accepted
    day_accepted = []
    global month_accepted
    month_accepted = []
    global year_accepted
    year_accepted = []
    global day_published
    day_published = []
    global month_published
    month_published = []
    global year_published
    year_published = []
    
def get_MaterialsNo ():
# Get number of figures, tables and supplementary material:

    # Get number of figures:
    global noFig
    noFig = 0
    for elem in root.findall('.//fig[@fig-type="figure"]/label'):
        noFig = noFig + 1

    # Get number of Tables:
    global noTables    
    noTables = 0
    for elem in root.findall('.//table-wrap/label'):
        noTables = noTables + 1
    
    # Get number of formulas:
    global noFormulas
    noFormulas = 0
    for elem in root.findall('.//inline-formula'):
        noFormulas = noFormulas + 1
    
    # Get number of "Data Availability" section and 
    # number of its subsections:
    global noDataAvail
    noDataAvail = 0
    for elem in root.findall('.//sec/title'):
        if elem.text != None:
            if elem.text.startswith('Data availability'):
                noDataAvail = noDataAvail + 1
            if noDataAvail:    
                if elem.text.startswith('Underlying data'):
                    noDataAvail = noDataAvail + 1
                if elem.text.startswith('Extended data'):
                    noDataAvail = noDataAvail + 1
                if elem.text.startswith('Reporting guidelines'):
                    noDataAvail = noDataAvail + 1 

    # Get number of Supplementary material (Appendix also included):
    global noSuppl
    noSuppl = 0
    for elem in root.findall('.//sec/title'):
        if elem.text != None:
            if elem.text.startswith('Supplementary'):
                noSuppl = noSuppl + 1        
            if elem.text.startswith('Appendix'): 
                noSuppl = noSuppl + 1

def countNonImradWords ():
    print("TODO: count nonImradWords")
    
def get_totalWordNumber():
# Calculate total number of words in an article

    global article_length
    article_length = (abstract_length +  introduction_length + methods_length + 
                      results_length + discussion_length + conclusion_length)
    # TODO: add len(nonImradChapters) and supplementary/additional data words
    
def get_authorsResponses (): 
# Get authors' responses to reviewers:

    global responseID_responses
    responseID_responses = []
    for element in root.findall('.//sub-article[@article-type="response"]'):
            responseID_responses.append(element.attrib)
            for elem in element.findall('.//body/p'):
                responseID_responses.append(elem.text)
                responseID_responses.append(elem.tail)
            for elem in element.findall('.//body/p/bold'):
                responseID_responses.append(elem.text) 
                responseID_responses.append(elem.tail)
            for elem in element.findall('.//body/p/italic'):
                responseID_responses.append(elem.text) 
                responseID_responses.append(elem.tail)
            for elem in element.findall('.//body/p/list/list-item/p'):
                responseID_responses.append(elem.text) 
                responseID_responses.append(elem.tail) 
            for elem in element.findall('.//body/p/list/list-item/p/bold'):
                responseID_responses.append(elem.text) 
                responseID_responses.append(elem.tail) 
            for elem in element.findall('.//body/p/list/list-item/p/italic'):
                responseID_responses.append(elem.text) 
                responseID_responses.append(elem.tail)     
            for elem in element.findall('.//body/p/'):
                if elem.text not in responseID_responses:
                    responseID_responses.append(elem.text)
                if elem.tail not in responseID_responses:    
                    responseID_responses.append(elem.tail)

    idxs = []
    for idx, item in enumerate(responseID_responses):
        if "article-type" in item:
            idxs.append(idx)

    for i in range(len(idxs)):
        responseID_responses[idxs[i]] = str(responseID_responses[idxs[i]])        

    temp_list1 = []
    temp_list2 = []
    for el in responseID_responses:
        newstr = el.replace("{'article-type': 'response', 'id': '", '' )
        temp_list1.append(newstr)

    newstr = ""    
    for el in temp_list1:
        newstr = el.replace("'}", '' )
        newstr = newstr.replace("\n", '' )
        newstr = newstr.replace("\xa0", '' )
        temp_list2.append(newstr)

    responses_indeces = []
    responses_indeces = [ i for i, word in enumerate(temp_list2) if re.search("^comment\d", word)]

    global responses_separated
    responses_separated = []
    for i in range(len(responses_indeces)):
        if i < (len(responses_indeces)-1):
            responses_separated.append([' '.join(temp_list2[responses_indeces[i]+1 : responses_indeces[i+1]])]) 
        else:
            responses_separated.append([' '.join(temp_list2[responses_indeces[i]+1 : len(temp_list2)])])

    print(len(responses_separated))
    
def merge_tables ():
    merged_tables_1 = pd.DataFrame.merge(reportID_fullNames, review_info, on='reportID')
    merged_tables_2 = pd.DataFrame.merge(article_info, merged_tables_1)
    merged_tables_2.to_csv (r'C:\Users\Korisnik\Desktop\Welcome_script\merged_tables_2.csv', mode='a', index = False, header=False, sep = ';')
    print("\nMerged tables 2: \n")
    print(merged_tables_2)
    if len(merged_tables_2) == 0:
        article_info.to_csv (r'C:\Users\Korisnik\Desktop\Welcome_script\merged_tables_additional.csv', mode='a', index = False, header=False, sep = ';')
    
# Go to directory which contains filtered_xml_urls.csv and filtered_pdf_urls.csv files:
os.chdir("C:\\Users\\Korisnik\\Desktop\\Welcome_script")
xml_urls = []
global pdfPagesNum
pdfPagesNum = []
 
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
for i in range(0,5): # for testing purpose: test only a sample
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
                global current_doi
                current_doi = elem.text    
                
            reset_variables()
            get_ResearchArea()
            get_MaterialsNo()
            countImradWords()
            #countNonImradWords()
            get_totalWordNumber()
            get_authorsResponses()
            get_reviewsInfo()
            get_reviewersInfo()
            get_articleInfo()
            #merge_tables()
            print('----------------------------------------')