import ORC_main

import re
import pandas as pd
from difflib import SequenceMatcher
import string
from genderizer.genderizer import Genderizer

def get_authorsResponses (root): 
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
            for elem in element.findall('.//body/p/italic/underline'):
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
            for elem in element.findall('.//body/p/ext-link'):
                responseID_responses.append(elem.text) 
                responseID_responses.append(elem.tail)    
            for elem in root.findall('.//body/sec/sec/p/xref'):
                responseID_responses.append(elem.text)    
                responseID_responses.append(elem.tail)      
            for elem in root.findall('.//body/sec/sec/p/xref/'):
                if elem.text not in responseID_responses:
                    responseID_responses.append(elem.text)    
                if elem.tail not in responseID_responses:    
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
    

def get_reviewsInfo (root, current_doi):
# Get reviewers' recommendations, comments and dates 
# for each version of an article
    
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
 
    # Get authors' responses:
    aut_responses = []
    for elem in root.findall('.//sub-article[@article-type="response"]/body/p'):
        aut_responses.append(elem.text)
    for elem in root.findall('.//sub-article[@article-type="response"]/body/p/bold'):
        aut_responses.append(elem.text)
    for elem in root.findall('.//sub-article[@article-type="response"]/body/p/italic'):
        aut_responses.append(elem.text)

    # Get reviewers' comments and join each comment with appropriate ref-report ID 
    global reportID_comments # remove later
    reportID_comments = []
    reportIDs = []
    for elem in root.findall('.//sub-article[@article-type="ref-report"]'):
        reportID_comments.append(elem.attrib)
        reportIDs.append(elem.attrib)
        for el in elem.findall('.//body/p'):
            # Ensure that reviewers' and author's responses don't mix:
            if el.text not in responseID_responses: 
                reportID_comments.append(el.text)
                reportID_comments.append(el.tail)
        for el in elem.findall('.//body/p/bold'):
            if el.text not in responseID_responses:
                reportID_comments.append(el.text)
                reportID_comments.append(el.tail)
        for el in elem.findall('.//body/p/italic'):
            if el.text not in responseID_responses:
                reportID_comments.append(el.text)
                reportID_comments.append(el.tail)        
        for el in elem.findall('.//body/p/list/list-item/p'):
            if el.text not in responseID_responses:
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
    review_indeces = [ i for i, word in enumerate(temp_list2) if re.search("^report\d", word)]
    
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
    
            
    # Check for case when there are no responses to some reviewers' comments:
    if len(responses_separated) < len(comments_separated):
        for i in range(len(comments_separated)-len(responses_separated)):
            responses_separated.append("No response")    
            
    print("No comments: ", len(comments_separated))        
    print("No responses: ", len(responses_separated))
        
    # Create a DataFrame table containing info on reviewers and reviews 
    global review_info
    review_info = pd.DataFrame({'dateReviewed':rev_to_date['date'],
                                    'Version':verNo,
                                    'doi':fullDoi_fill,
                                    'Recommendation':refRecomm,
                                    'reportID':reportIDs_separated})
                                    #'comments':comments_separated})                           

    print("\nReview information: \n")
    print(review_info)
 
def get_allCommResp (root, current_doi): 
# get all reviewer's comments and merge them into one list
# get all authors' responses and merge them into one list

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

    # Clean the comments text:
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

    comments_responses_df = pd.DataFrame({'doi': [current_doi],
                                          'comments': [' '.join(allComm_clean)],
                                          'responses': [' '.join(allResp_clean)]})
    
    print("\nAll comments and responses: ", comments_responses_df) 
    return(comments_responses_df)    

def get_reviewersInfo (root):
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
    
    
    reviews_all = pd.DataFrame.merge(reportID_fullNames, review_info, on='reportID')
    print("\nMERGED REVIEW TABLE\n", reviews_all)
    
    return (reviews_all)