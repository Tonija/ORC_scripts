import xml.etree.ElementTree as ET
import string
import re
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
from urllib.request import urlopen
#from functools import reduce

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
# Reset variables to default values and empty lists
    global research_area
    research_area = []
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
    
def get_ResearchArea ():

    medDOI_file = open("orc_med_doi.csv", "r")
    socDOI_file = open("orc_soc_doi.csv", "r")

    for line in medDOI_file:
        values = line.split()
        if current_doi in values:
            print("Subject Area: Medicine and health sciences")
            research_area.append("Medical")
                    
    for line in socDOI_file:
        values = line.split()
        if current_doi in values:
            print("Subject Area: Social sciences")
            research_area.append("Social")

    medDOI_file.close()
    socDOI_file.close()
    
def get_MaterialsNo ():
# Get number of figures, tables and supplementary material:
    figures = []
    for elem in root.findall('.//fig[@fig-type="figure"]/label'):
        figures.append(elem.text)
    global noFig
    noFig = len(figures)

    # Get number of Tables
    tables = []
    for elem in root.findall('.//table-wrap/label'):
        tables.append(elem.text)
    global noTables    
    noTables = len(tables)
    
    supplementary = []
    # Get number of Supplementary material
    for elem in root.findall('.//sec[@sec-type="supplementary-material"]/p/bold'):
        if elem.text.startswith('Supplementary File'):
            supplementary.append(elem.text)
    for elem in root.findall('.//sec/title'):
        if elem.text != None:
            if elem.text.startswith('Appendix'):
                supplementary.append(elem.text)
            if elem.text.startswith('Data availability'):
                supplementary.append(elem.text)       
    global noSuppl        
    noSuppl = len(supplementary)

def get_articleNumWords ():
# Count the word number of each article section
# Count the total word number
  
    # Abstract
    abstr = []
    abstract = []
    for a in root.findall('.//abstract/p/'):
        abstr.append(a.text)
        abstr.append(a.tail)
    for a in root.findall('.//abstract/p/bold/'):
        abstr.append(a.text)
        abstr.append(a.tail) 
    for a in root.findall('.//abstract/p/italic'):
        abstr.append(a.text)
        abstr.append(a.tail)
    for a in root.findall('.//abstract/p/bold/italic'):
        abstr.append(a.text)
        abstr.append(a.tail)    
    # Remove None values: 
    for val in abstr: 
        if val != None : 
            abstract.append(val)
    # Convert to string: 
    abstr_str = ''.join(abstract)
    # Split string into words:    
    abstract = abstr_str.split()
    global abstract_length
    abstract_length = len(abstract)

    # Introduction 
    intro = []
    introduction = []
    for a in root.findall('.//sec[@sec-type="intro"]/'):
        intro.append(a.text)
        intro.append(a.tail)
    for a in root.findall('.//sec[@sec-type="intro"]/p/'):
        intro.append(a.text)
        intro.append(a.tail)  
    for a in root.findall('.//sec[@sec-type="intro"]/p/italic'):
        intro.append(a.text)
        intro.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="intro"]/p/bold'):
        intro.append(a.text)
        intro.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="intro"]/p/bold/italic'):
        intro.append(a.text)
        intro.append(a.tail)    
    for val in intro: 
        if val != None : 
            introduction.append(val) 
    intro_str = ''.join(introduction)    
    introduction = intro_str.split()
    global introduction_length
    introduction_length = len(introduction)

    # Methods
    met = []
    methods = []
    try:
        for a in root.findall('.//sec[@sec-type="methods"]/'):
            met.append(a.text)
            met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="methods"]/sec/'):
            met.append(a.text)
            met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="methods"]/sec/title'):
            met.append(a.text)
            met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="methods"]/sec/p/italic'):
            met.append(a.text)
            met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="methods"]/sec/p/bold'):
            met.append(a.text)
            met.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="methods"]/sec/p/bold/italic'):
            met.append(a.text)
            met.append(a.tail)     
        for val in met: 
            if val != None : 
                methods.append(val) 
        met_str = ''.join(methods)
        methods = met_str.split()
        global methods_length
        methods_length = len(methods)
    except:
        print("methods error")

    # Results
    res = []
    results = []
    try:
        for a in root.findall('.//sec[@sec-type="results"]/'):
            res.append(a.text)
            res.append(a.tail)
        for a in root.findall('.//sec[@sec-type="results"]/sec/'):
            res.append(a.text)
            res.append(a.tail)    
        for a in root.findall('.//sec[@sec-type="results"]/sec/title'):
            res.append(a.text)
            res.append(a.tail)
        for a in root.findall('.//sec[@sec-type="results"]/sec/p/italic'):
            res.append(a.text)
            res.append(a.tail)
        for a in root.findall('.//sec[@sec-type="results"]/sec/p/bold'):
            res.append(a.text)
            res.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="results"]/sec/p/bold/italic'):
            res.append(a.text)
            res.append(a.tail)   
        if len(results) == 0:        
            for a in root.findall('.//sec[@sec-type="results | discussion"]/'):
                res.append(a.text)
                res.append(a.tail)
            for a in root.findall('.//sec[@sec-type="results | discussion"]/sec/'):
                res.append(a.text)
                res.append(a.tail)    
            for a in root.findall('.//sec[@sec-type="results | discussion"]/sec/title'):
                res.append(a.text)
                res.append(a.tail)
            for a in root.findall('.//sec[@sec-type="results | discussion"]/sec/p/italic'):
                res.append(a.text)
                res.append(a.tail)
            for a in root.findall('.//sec[@sec-type="results | discussion"]/sec/p/bold'):
                res.append(a.text)
                res.append(a.tail) 
            for a in root.findall('.//sec[@sec-type="results | discussion"]/sec/p/bold/italic'):
                res.append(a.text)
                res.append(a.tail) 
        for val in res: 
            if val != None : 
                results.append(val)        
        res_str = ''.join(results)
        results = res_str.split()
        global results_length
        results_length = len(results)
    except:
        print("results error")  
         
    # Discussion
    discuss = []
    for a in root.findall('.//sec[@sec-type="discussion"]/'):
        discuss.append(a.text) 
        discuss.append(a.tail)
    for a in root.findall('.//sec[@sec-type="discussion"]/sec/'):
        discuss.append(a.text) 
        discuss.append(a.tail)
    for a in root.findall('.//sec[@sec-type="discussion"]/sec/title'):
        discuss.append(a.text) 
        discuss.append(a.tail)    
    for a in root.findall('.//sec[@sec-type="discussion"]/sec/p/italic'):
        discuss.append(a.text) 
        discuss.append(a.tail)
    for a in root.findall('.//sec[@sec-type="discussion"]/sec/p/bold'):
        discuss.append(a.text) 
        discuss.append(a.tail)
    for a in root.findall('.//sec[@sec-type="discussion"]/sec/p/bold/italic'):
        discuss.append(a.text) 
        discuss.append(a.tail)    
    discussion = [] 
    for val in discuss: 
        if val != None : 
            discussion.append(val)    
    discuss_str = ''.join(discussion)
    discussion = discuss_str.split()  
    global discussion_length
    discussion_length = len(discussion)
          
    # Conclusion
    concl = []
    conclusion = []
    for a in root.findall('.//sec[@sec-type="conclusions"]/'):
        concl.append(a.text)
        concl.append(a.tail)
    for a in root.findall('.//sec[@sec-type="conclusions"]/sec/'):
        concl.append(a.text)
        concl.append(a.tail)
    for a in root.findall('.//sec[@sec-type="conclusions"]/sec/p'):
        concl.append(a.text)
        concl.append(a.tail)    
    for a in root.findall('.//sec[@sec-type="conclusions"]/sec/p/italic'):
        concl.append(a.text)
        concl.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="conclusions"]/sec/p/bold'):
        concl.append(a.text)
        concl.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="conclusions"]/sec/p/bold/italic'):
        concl.append(a.text)
        concl.append(a.tail)    
    for val in concl: 
        if val != None : 
            conclusion.append(val)
    concl_str = ''.join(conclusion)
    conclusion = concl_str.split()  
    global conclusion_length
    conclusion_length = len(conclusion)

    # Total number of words in an article:
    global article_length
    article_length = len(abstract) +  len(introduction) + len(introduction) + len(methods) + len(results) + len(discussion) + len(conclusion)                                   

def get_reviewsInfo ():
# Get reviewers' recommendations, comments and dates 
# for each version of an article

    # Get version of an article:
    for elem in root.findall('.//sub-article[@article-type="ref-report"]/front-stub/title-group/article-title'):
        versionNo.append(elem.text)
    # Get recommendations:
    for elem in root.findall('.//sub-article[@article-type="ref-report"]/front-stub/custom-meta-group/custom-meta/meta-value'):
        refRecomm.append(elem.text) 
       
    # Combine a recommendation with appropriate article version:
    ver_recomm = []
    for v, r in zip(versionNo, refRecomm):
        ver_recomm.append(v + " : " + r) 
 
    # Get reviewers' comments and join each comment with appropriate ref-report ID 
    reportID_comments = []
    reportIDs = []
    for elem in root.findall('.//sub-article[@article-type="ref-report"]'):
        reportID_comments.append(elem.attrib)
        reportIDs.append(elem.attrib)
        for el in elem.findall('.//body/p'):
            reportID_comments.append(el.text)
            reportID_comments.append(el.tail)
        for el in elem.findall('.//body/p/bold'):
            reportID_comments.append(el.text)
            reportID_comments.append(el.tail)
        for el in elem.findall('.//body/p/italic'):
            reportID_comments.append(el.text)
        for el in elem.findall('.//body/p/list/list-item/p'):
            reportID_comments.append(el.text)
            reportID_comments.append(el.tail)

    idxs = []
    for idx, item in enumerate(reportID_comments):
        if "article-type" in item:
            idxs.append(idx)
            
    for i in range(len(idxs)):
        reportID_comments[idxs[i]] = str(reportID_comments[idxs[i]])        
            
    temp_list1 = []
    temp_list2 = []
    for el in reportID_comments:
        newstr = el.replace("{'article-type': 'ref-report', 'id': '", '' )
        temp_list1.append(newstr)
        
    for el in temp_list1:
        newstr = el.replace("'}", '' )
        temp_list2.append(newstr)

    review_indeces = []
    review_indeces = [ i for i, word in enumerate(temp_list2) if word.startswith("report")]
    
    global comments_separated
    comments_separated = []
    for i in range(len(review_indeces)):
        if i < (len(review_indeces)-1):
            comments_separated.append([' '.join(temp_list2[review_indeces[i]+1 : review_indeces[i+1]])]) 
        else:
            comments_separated.append([' '.join(temp_list2[review_indeces[i]+1 : len(temp_list2)])])
    
    global reportIDs_separated
    reportIDs_separated = []        
    for i in range(len(review_indeces)):
        reportIDs_separated.append(temp_list2[review_indeces[i]])
                                  
    # Get date of each review:                              
    for elem in root.findall('.//sub-article[@article-type="ref-report"]/front-stub/pub-date'):
        for el in elem.findall('.//day'):
            recomm_day.append(el.text) 
        for el in elem.findall('.//month'):
            recomm_month.append(el.text) 
        for el in elem.findall('.//year'):
            recomm_year.append(el.text)
          
    rev_to_date = pd.DataFrame({'day':recomm_day,
                                'month':recomm_month,
                                'year':recomm_year})    

    # Convert to datetime:
    rev_to_date['date'] = pd.to_datetime(rev_to_date[['day','month','year']])

    # From element 'Reviewer response n ' get the number n
    # This number represents article version number       
    verNo = str(versionNo)
    verNo = list(''.join(list(filter(lambda x: x.isdigit(), verNo)))) 

    partialDoi_fill = []
    for i in range(len(refRecomm)):
        partialDoi_fill.append(current_doi[:-2])
    
    fullDoi_fill = []
    # Join appropriate partialDOI with the Version No:
    for partDOI, ver in zip(partialDoi_fill, verNo):
        fullDoi_fill.append(partDOI + "." + ver)   
    
    # Create a DataFrame table containing info on reviewers and reviews 
    global review_info
    review_info = pd.DataFrame({'dateReviewed':rev_to_date['date'],
                                'Version':verNo,
                                'doi':fullDoi_fill,
                                'Recommendation':refRecomm,
                                'reportID':reportIDs_separated,
                                'comments':comments_separated})                              

    print("\nReview information: \n")
    print(review_info)

def get_reviewersInfo ():
# Get reviewers' full names and match with the report ID
# even in cases when more reviewers comment together as a team

    ref_names_check = []
    for elem in root.findall('.//sub-article[@article-type="ref-report"]/front-stub/contrib-group/contrib/name/given-names'):
        ref_names_check.append(elem.text)
    
    ref_surnames_check = []
    for elem in root.findall('.//sub-article[@article-type="ref-report"]/front-stub/contrib-group/contrib/name/surname'):
        ref_surnames_check.append(elem.text)    
                         
    # Match report ID and surname
    reportID_surname = []
    for elem in root.findall('.//sub-article[@article-type="ref-report"]'):
        reportID_surname.append(elem.attrib)
        for el in elem.findall('.//surname'):
            if el.text in ref_surnames_check:
                reportID_surname.append(el.text)

    idxs = []
    for idx, item in enumerate(reportID_surname):
        if "article-type" in item:
            idxs.append(idx)
            
    for i in range(len(idxs)):
        reportID_surname[idxs[i]] = str(reportID_surname[idxs[i]])        
            
    temp_list = []
    temp_surnames = []
    for el in reportID_surname:
        newstr = el.replace("{'article-type': 'ref-report', 'id': '", '' )
        temp_list.append(newstr)

    for el in temp_list:
        newstr = el.replace("'}", '' )
        temp_surnames.append(newstr)

    for i in range(0,2):     
        for i in range(0,len(temp_surnames),2):
            if "report" not in temp_surnames[i]:
                temp_surnames = temp_surnames[0:i] + [temp_surnames[i-2]] + temp_surnames[i:]

    # Match report ID and given-name
    reportID_name = []
    for elem in root.findall('.//sub-article[@article-type="ref-report"]'):
        reportID_name.append(elem.attrib)
        for el in elem.findall('.//given-names'):
            if el.text in ref_names_check:
                 reportID_name.append(el.text)

    idxs = []
    for idx, item in enumerate(reportID_name):
        if "article-type" in item:
            idxs.append(idx)
            
    for i in range(len(idxs)):
        reportID_name[idxs[i]] = str(reportID_name[idxs[i]])        
            
    temp_list = []
    temp_names = []
    for el in reportID_name:
        newstr = el.replace("{'article-type': 'ref-report', 'id': '", '' )
        temp_list.append(newstr)

    for el in temp_list:
        newstr = el.replace("'}", '' )
        temp_names.append(newstr)

    for i in range(0,2):
        for i in range(0,len(temp_names),2):
            if "report" not in temp_names[i]:
                temp_names = temp_names[0:i] + [temp_names[i-2]] + temp_names[i:]
    
    global reportID_fullNames 
    reportID_fullNames = pd.DataFrame({'reportID':[temp_surnames[i] for i in range(len(temp_surnames)) if i % 2 != 1],
                                   'surname':temp_surnames[1::2],
                                   'name':temp_names[1::2]}) 
    
    print("\nReviewers information: \n")
    print(reportID_fullNames)
    
def get_articleInfo ():
        
    # Get date when an article version was accepted:     
    for elem in root.findall('.//history/date[@date-type="accepted"]/day'):
        day_accepted.append(elem.text)
    for elem in root.findall('.//history/date[@date-type="accepted"]/month'):
        month_accepted.append(elem.text)
    for elem in root.findall('.//history/date[@date-type="accepted"]/year'):
        year_accepted.append(elem.text)

    # Get date when an article version was published    
    for elem in root.findall('.//article-meta/pub-date[@pub-type="epub"]/day'):
        day_published.append(elem.text)
    for elem in root.findall('.//article-meta/pub-date[@pub-type="epub"]/month'):
        month_published.append(elem.text)
    for elem in root.findall('.//article-meta/pub-date[@pub-type="epub"]/year'):
        year_published.append(elem.text)

    # Get version number from publication status
    pub_status = []
    for elem in root.findall('.//fn-group[@content-type="pub-status"]/fn/p'):
        pub_status.append(elem.text)    
    pub_status = [word for word in pub_status if word not in string.punctuation]    
    pub_status = ' '.join([str(elem) for elem in pub_status])  
    version = pub_status.split()[1][0] # pub_status.split()[1] will return '1;' 
                                       # pub_status.split()[1][0] will return '1'

    # Create an DataFrame table for accepted   
    df_accpt = pd.DataFrame({'day':day_accepted,
                            'month':month_accepted,
                            'year':year_accepted})

    #convert to datetime
    df_accpt['date'] = pd.to_datetime(df_accpt[['day','month','year']])

    # Create an DataFrame table for published   
    df_publ = pd.DataFrame({'day':day_published,
                            'month':month_published,
                            'year':year_published})

    #convert to datetime
    df_publ['date'] = pd.to_datetime(df_publ[['day','month','year']])

    # Create a DataFrame table containing relevant article information:
    global article_info
    article_info = pd.DataFrame({'doi':[current_doi],
                                 'version':[version],
                                 'researchArea':research_area,
                                 'dateAccepted':[df_accpt['date'][0]],
                                 'datePublished':[df_publ['date'][0]],
                                 'NoFigures':[noFig],
                                 'NoTables':[noTables],
                                 'NoSupplementary': [noSuppl],
                                 'abstractSize':[abstract_length],
                                 'introductionSize':[introduction_length],
                                 'methodsSize':[methods_length],
                                 'resultsSize':[results_length],
                                 'discussionSize':[discussion_length],
                                 'conclusionSize':[conclusion_length],
                                 'totalArticleSize':[article_length]})
    
    #article_info.to_csv (r'C:\Users\Korisnik\Desktop\Welcome_script\articleInfo_dataframe.csv', mode='a', index = False, header=False, sep = ';')
    print("\nArticle information: \n")
    print(article_info)
    
def merge_tables ():
    merged_tables = pd.DataFrame.merge(reportID_fullNames, review_info, on='reportID')
    print("\nMerged tables 1: \n")
    merged_tables.to_csv (r'C:\Users\Korisnik\Desktop\Welcome_script\merged_tables.csv', mode='a', index = False, header=False, sep = ';')
    merged_tables_new = pd.DataFrame.merge(article_info, merged_tables, on='doi')
    merged_tables_new.to_csv (r'C:\Users\Korisnik\Desktop\Welcome_script\merged_tables_new.csv', mode='a', index = False, header=False, sep = ';')
    print("\nMerged tables 2: \n")
    print(merged_tables_new)
    
# Go to directory which contains filtered_xml_urls.csv and filtered_pdf_urls.csv files:
os.chdir("C:\\Users\\Korisnik\\Desktop\\Welcome_script")
xml_urls = []
waiting_review = []
#with open('filtered_xml_urls_copy.csv', 'r') as xml_f: # REMOVE LATER
with open('filtered_xml_urls.csv', 'r') as xml_f:
    reader = csv.reader(xml_f)
    for row in reader:
        xml_urls.append((" ".join(row)))

for i in range(len(xml_urls)):
#for i in range(0,1): # for testing purpose: test only a sample
    with urlopen(xml_urls[i]) as f:
        tree = ET.parse(f)
        global root
        root = tree.getroot()
        print(i)
        print("\nFile URL: " + xml_urls[i])
        temp_report = []
        isReviewed = False
        for elem in root.findall('.//sub-article[@article-type="ref-report"]/'):
            temp_report.append(elem.tag)
        if len(temp_report) != 0:
            isReviewed = True
        if not isReviewed:
            print("Article is awaiting for review.")
            waiting_review.append(xml_urls[i])
        else:    
            for elem in root.find('.//article-id[@pub-id-type="doi"]').iter():
                global current_doi
                current_doi = elem.text           
            reset_variables()
            get_ResearchArea()
            get_MaterialsNo()
            get_articleNumWords()
            get_reviewsInfo()
            get_reviewersInfo()
            get_articleInfo()
            merge_tables()
            print('----------------------------------------')
            # TODO: merged_table should contain all necessary data

#with open('filtered_pdf_urls.csv', 'r') as xml_f: 
    #Get number of pdf pages