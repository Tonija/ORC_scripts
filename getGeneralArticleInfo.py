import ORC_main
import string
import pandas as pd

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

df_accpt = pd.DataFrame()
df_publ = pd.DataFrame()

def get_ResearchArea(current_doi):

    medDOI_file = open("orc_med_doi.csv", "r")
    socDOI_file = open("orc_soc_doi.csv", "r")
    
    global research_area
    research_area = ""

    for line in medDOI_file:
        values = line.split()
        if current_doi in values:
            print("Subject Area: Medicine and health sciences")
            research_area = "Medical"
                    
    for line in socDOI_file:
        values = line.split()
        if current_doi in values:
            print("Subject Area: Social sciences")
            research_area = "Social"

    medDOI_file.close()
    socDOI_file.close()

def get_MaterialsNo (root):
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

def get_articleInfo (root):

            
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

def createMaterialsInfoDf (current_doi, pdfPagesNum, article_length):

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
    global materials_info
    materials_info = pd.DataFrame({'doi':[current_doi],
                                 #'version':[version],
                                 'researchArea':[research_area],
                                 'NoPdfPages':pdfPagesNum[-1],
                                 'dateAccepted':[df_accpt['date'][0]],
                                 'datePublished':[df_publ['date'][0]],
                                 'NoFigures':[noFig],
                                 'NoTables':[noTables],
                                 'NoFormulas':noFormulas,
                                 'NoSupplementary': [noSuppl],
                                 'NoDataAvailability':[noDataAvail],
                                 'totalArticleSize':[article_length]})
    print("\nMaterials information: \n")
    print(materials_info)
    
    return(materials_info)