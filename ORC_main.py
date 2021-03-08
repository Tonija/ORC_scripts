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

from getGeneralArticleInfo import *
from getImrdChapters import *
from getNonImrdChapters import *
from getReviewsInfo import *

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

    global article_length
    article_length = countImradWords(root) + countNonImrdWords(root) # + suppl + dataAvailability !!!
    # TODO: add len(supplementary/additional)
    
def merge_tables ():

    partial_info =  pd.DataFrame.merge(createMaterialsInfoDf(current_doi, pdfPagesNum, article_length), createImrdDf(current_doi), on='doi')
    print("\nPARTIAL INFO: ", partial_info)
    
    all_info = pd.DataFrame.merge(get_reviewersInfo(root), partial_info, on='doi')
    #all_info.to_csv (r'C:\Users\Korisnik\Desktop\Welcome_script\all_info.csv', mode='a', index = False, header=False, sep = ';')
    print("\nALL INFO TABLE: ", all_info)
    
    #if len(partial_info) == 0:
    #    article_info.to_csv (r'C:\Umerged_table1sers\Korisnik\Desktop\Welcome_script\partial_info.csv', mode='a', index = False, header=False, sep = ';')

def main():    
    # Go to directory which contains filtered_xml_urls.csv and filtered_pdf_urls.csv files:
    os.chdir("C:\\Users\\Korisnik\\Desktop\\Welcome_script")
    
    xml_urls = []
    global pdfPagesNum
    pdfPagesNum = []
    global current_doi
    current_doi = ""
     
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
    for i in range(0,10): # for testing purpose: test only a sample
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
                merge_tables()
                print('\n----------------------------------------')
                
if __name__ == "__main__":
    main()                