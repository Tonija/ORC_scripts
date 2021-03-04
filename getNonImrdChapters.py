# NonIMRD chapters
nonImrd = []
nonImrdChapter = []
nonImrd_str = ""
brackets = '''()[]{}<>'''

#def countNonImradWords ():

for a in root.findall('.//sec[@sec-type="Consent and ethical approval"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[@sec-type="Consent and ethical approval"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[@sec-type="Consent and ethical approval"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[@sec-type="Consent and ethical approval"]/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[@sec-type="Consent and ethical approval"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail) 
        
for a in root.findall('.//sec[title="Ethical approval"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Ethical approval"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Ethical approval"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Ethical approval"]/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Ethical approval"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail) 
        
for a in root.findall('.//sec[title="Consent"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Consent"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Consent"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Consent"]/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Consent"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail) 
        
for a in root.findall('.//sec[title="Ethical considerations"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Ethical considerations"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Ethical considerations"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Ethical considerations"]/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Ethical considerations"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)         
 
for a in root.findall('.//sec[title="Ethical statement"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Ethical statement"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Ethical statement"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Ethical statement"]/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Ethical statement"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)  

for a in root.findall('.//sec[title="Ethics and consent"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Ethics and consent"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Ethics and consent"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Ethics and consent"]/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Ethics and consent"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)
        
for a in root.findall('.//sec[title="Ethics compliance"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Ethics compliance"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Ethics compliance"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Ethics compliance"]/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Ethics compliance"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)        
  
for a in root.findall('.//sec[title="Ethics approval and consent"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Ethics approval and consent"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Ethics approval and consent"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Ethics approval and consent"]/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Ethics approval and consent"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)
        
for a in root.findall('.//sec[title="Ethics approval and consent to participate"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Ethics approval and consent to participate"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Ethics approval and consent to participate"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)

for a in root.findall('.//sec[title="Lay summary"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Lay summary"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Lay summary"]/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Lay summary"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Lay summary"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)  

for a in root.findall('.//sec[title="Author information"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Author information"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Author informations"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail) 
        
for a in root.findall('.//sec[title="F1000 Research Statement of Endorsement"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="F1000 Research Statement of Endorsement"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="F1000 Research Statement of Endorsement"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)         
 
for a in root.findall('.//sec[title="Definition of trust"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Definition of trust"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Definition of trust"]/sec/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Definition of trust"]/sec/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="Definition of trust"]/sec/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Definition of trust"]/sec/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Definition of trust"]/sec/p/bold/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Definition of trust"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail) 
        
for a in root.findall('.//sec[title="Framework – antecedents of employee trust in remote and virtual teams"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Framework – antecedents of employee trust in remote and virtual teams"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Framework – antecedents of employee trust in remote and virtual teams"]/sec/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Framework – antecedents of employee trust in remote and virtual teams"]/sec/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="Framework – antecedents of employee trust in remote and virtual teams"]/sec/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Framework – antecedents of employee trust in remote and virtual teams"]/sec/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Framework – antecedents of employee trust in remote and virtual teams"]/sec/p/bold/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Framework – antecedents of employee trust in remote and virtual teams"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)         
        
for a in root.findall('.//sec[title="Key historical moments and tensions at the heart of the Global Burden of Disease study"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Key historical moments and tensions at the heart of the Global Burden of Disease study"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Key historical moments and tensions at the heart of the Global Burden of Disease study"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Key historical moments and tensions at the heart of the Global Burden of Disease study"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail) 
        
for a in root.findall('.//sec[title="Ethical issues"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="Ethical issues"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Ethical issues"]/sec/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Ethical issues"]/sec/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="Ethical issues"]/sec/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Ethical issues"]/sec/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Ethical issues"]/sec/p/bold/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="Ethical issues"]/sec/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Ethical issues"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)
 
for a in root.findall('.//sec[title="What is co-production?"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="What is co-production?"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="What is co-production?"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="What is co-production?"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail) 
        
for a in root.findall('.//sec[title="Challenges of creating meaningful co-production"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Challenges of creating meaningful co-production"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Challenges of creating meaningful co-production"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Challenges of creating meaningful co-production"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)  

for a in root.findall('.//sec[title="A set of pragmatic principles for co-production"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="A set of pragmatic principles for co-production"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="A set of pragmatic principles for co-production"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="A set of pragmatic principles for co-production"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)      

for a in root.findall('.//sec[title="An Illustration: Establishing a Young Peoples’ Health Research Group"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="An Illustration: Establishing a Young Peoples’ Health Research Group"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="An Illustration: Establishing a Young Peoples’ Health Research Group"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="An Illustration: Establishing a Young Peoples’ Health Research Group"]/sec/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="An Illustration: Establishing a Young Peoples’ Health Research Group"]/sec/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="An Illustration: Establishing a Young Peoples’ Health Research Group"]/sec/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="An Illustration: Establishing a Young Peoples’ Health Research Group"]/sec/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="An Illustration: Establishing a Young Peoples’ Health Research Group"]/sec/p/bold/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="An Illustration: Establishing a Young Peoples’ Health Research Group"]/sec/p/list/list-item/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="An Illustration: Establishing a Young Peoples’ Health Research Group"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)         

for a in root.findall('.//sec[title="Learning points"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Learning points"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Learning points"]/p/list/list-item/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Learning points"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail) 
        
for a in root.findall('.//sec[title="What is the GCLP standard?"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="What is the GCLP standard?"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="What is the GCLP standard?"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail) 
        
for a in root.findall('.//sec[title="The Kenya Medical Research Institute – Centre for Microbiology and Research (KEMRI-CMR)"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="The Kenya Medical Research Institute – Centre for Microbiology and Research (KEMRI-CMR)"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="The Kenya Medical Research Institute – Centre for Microbiology and Research (KEMRI-CMR)"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)         
 
for a in root.findall('.//sec[title="Career Course Thematic Analysis"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Career Course Thematic Analysis"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Career Course Thematic Analysis"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Career Course Thematic Analysis"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail) 
        
for a in root.findall('.//sec[title="Study 1 – Preparing Science Professionals (PSP) course"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Study 1 – Preparing Science Professionals (PSP) course"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Study 1 – Preparing Science Professionals (PSP) course"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail) 

for a in root.findall('.//sec[title="Study 2 – Hope is Not a Plan (HINAP) course"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Study 2 – Hope is Not a Plan (HINAP) course"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Study 2 – Hope is Not a Plan (HINAP) course"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)         

for a in root.findall('.//sec[title="General Discussion and Recommendations for Future Course Implementation"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="General Discussion and Recommendations for Future Course Implementation"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="General Discussion and Recommendations for Future Course Implementation"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)         
                
for a in root.findall('.//sec[title="Other published results"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="Other published results"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Other published results"]/sec/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Other published results"]/sec/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="Other published results"]/sec/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Other published results"]/sec/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Other published results"]/sec/p/bold/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)      
for a in root.findall('.//sec[title="Other published results"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="Other published results"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)        
        
for a in root.findall('.//sec[title="Respondents"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Respondents"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Respondents"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)
        
for a in root.findall('.//sec[title="Data"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Data"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Data"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Data"]/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Data"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)

for a in root.findall('.//sec[title="Limitations"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Limitations"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Limitations"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="Limitations"]/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Limitations"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail) 
        
for a in root.findall('.//sec[title="Translational outlook, limitations and future directions"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Translational outlook, limitations and future directions"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Translational outlook, limitations and future directions"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Translational outlook, limitations and future directions"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)        

for a in root.findall('.//sec[title="Limitations and Future Directions"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Limitations and Future Directions"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Limitations and Future Directions"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Limitations and Future Directions"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)  
        
for a in root.findall('.//sec[title="Addendum"]/title'): 
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Addendum"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)      
for a in root.findall('.//sec[title="Addendum"]/sec/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Addendum"]/sec/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Addendum"]/sec/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Addendum"]/sec/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="Addendum"]/sec/p/bold/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[titlee="Addendum"]/sec/p/italic/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Addendum"]/sec/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Addendum"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail) 
        

for a in root.findall('.//sec[title="World Health Organization recommendations and fiscal policies"]/title'): 
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="World Health Organization recommendations and fiscal policies"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)      
for a in root.findall('.//sec[title="World Health Organization recommendations and fiscal policies"]/sec/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="World Health Organization recommendations and fiscal policies"]/sec/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="World Health Organization recommendations and fiscal policies"]/sec/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="World Health Organization recommendations and fiscal policies"]/sec/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="World Health Organization recommendations and fiscal policies"]/sec/p/bold/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[titlee="World Health Organization recommendations and fiscal policies"]/sec/p/italic/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="World Health Organization recommendations and fiscal policies"]/sec/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="World Health Organization recommendations and fiscal policies"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail) 
        
for a in root.findall('.//sec[title="2 Overview of existing funding models"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="2 Overview of existing funding models"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="2 Overview of existing funding models"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="2 Overview of existing funding models"]/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="2 Overview of existing funding models"]/p/list/list-item/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="2 Overview of existing funding models"]/p/list/list-item/p/list/list-item/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="2 Overview of existing funding models"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)
        
for a in root.findall('.//sec[title="3 Funding situation of the UniProt knowledgebase, past and present"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="3 Funding situation of the UniProt knowledgebase, past and present"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="3 Funding situation of the UniProt knowledgebase, past and present"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="3 Funding situation of the UniProt knowledgebase, past and present"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)  

for a in root.findall('.//sec[title="4 Application of the models to the UniProt case"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="4 Application of the models to the UniProt case"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="4 Application of the models to the UniProt case"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="4 Application of the models to the UniProt case"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail) 

for a in root.findall('.//sec[title="5 Discussion and proposal for a long-term sustainable funding model for knowledgebases"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="5 Discussion and proposal for a long-term sustainable funding model for knowledgebases"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="5 Discussion and proposal for a long-term sustainable funding model for knowledgebases"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="5 Discussion and proposal for a long-term sustainable funding model for knowledgebases"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)           
        
for a in root.findall('.//sec[title="Lessons learned and recommendations"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Lessons learned and recommendations"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Lessons learned and recommendations"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="Lessons learned and recommendations"]/p/list/list-item/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="Lessons learned and recommendations"]/p/list/list-item/p/list/list-item/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Lessons learned and recommendations"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)
        
for a in root.findall('.//sec[title="Conclusions and future directions"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Conclusions and future directions"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Conclusions and future directions"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Conclusions and future directions"]/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Conclusions and future directions"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail) 
  
for a in root.findall('.//sec[title="Background"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Background"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Background"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Background"]/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Background"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)  
        
for a in root.findall('.//sec[title="Plain language summary"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Plain language summary"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Plain language summary"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)        
        
for a in root.findall('.//sec[title="Survey selection"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Survey selection"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Survey selection"]/p/xref'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="Survey selection"]/p/list/list-item/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Survey selection"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)   
        
for a in root.findall('.//sec[title="Strengths and limitations"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Strengths and limitations"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Strengths and limitations"]/sec/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Strengths and limitations"]/sec/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Strengths and limitations"]/sec/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Strengths and limitations"]/sec/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Strengths and limitations"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)  

for a in root.findall('.//sec[title="Implications for research/policy"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Implications for research/policy"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Implications for research/policy"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)  

for a in root.findall('.//sec[title="Policy implications"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Policy implications"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Policy implications"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)
        
for a in root.findall('.//sec[title="Program development"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Program development"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)      
for a in root.findall('.//sec[title="Program development"]/sec/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Program development"]/sec/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Program development"]/sec/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Program development"]/sec/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="Program development"]/sec/p/bold/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="Program development"]/sec/p/italic/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Program development"]/sec/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Program development"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)         

for a in root.findall('.//sec[title="Objective"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Objective"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="Objective"]/sec/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Objective"]/sec/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="Objective"]/sec/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Objective"]/sec/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Objective"]/sec/p/bold/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Objective"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)   
    
for a in root.findall('.//sec[title="Objectives of the study"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Objectives of the study"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="Objectives of the study"]/sec/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Objectives of the study"]/sec/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="Objectives of the study"]/sec/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Objectives of the study"]/sec/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Objectives of the study"]/sec/p/bold/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Objectives of the study"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)   
    
for a in root.findall('.//sec[title="Recommendations"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Recommendations"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Recommendations"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Recommendations"]/sec/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Recommendations"]/sec/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="Recommendations"]/sec/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Recommendations"]/sec/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Recommendations"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)   

for a in root.findall('.//sec[title="Delay"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Delay"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Delay"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Delay"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)          

for a in root.findall('.//sec[title="Containment"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Containment"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Containment"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Containment"]/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Containment"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)
        
for a in root.findall('.//sec[title="Mitigation – on not being able to touch"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Mitigation – on not being able to touch"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Mitigation – on not being able to touch"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Mitigation – on not being able to touch"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)        
        
for a in root.findall('.//sec[title="Theory and Hypotheses"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Theory and Hypotheses"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Theory and Hypotheses"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)
        
for a in root.findall('.//sec[title="Abbreviations"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Abbreviations"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Abbreviations"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Abbreviations"]/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Abbreviations"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)
        
for a in root.findall('.//sec[title="List of abbreviations:"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="List of abbreviations:"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="List of abbreviations:"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="List of abbreviations:"]/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
    
for a in root.findall('.//sec[title="Literature review"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="Literature review"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Literature review"]/sec/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Literature review"]/sec/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="Literature review"]/sec/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Literature review"]/sec/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Literature review"]/sec/p/bold/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="Literature review"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)  
        
for a in root.findall('.//sec[title="Theoretical review"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="Theoretical review"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Theoretical review"]/sec/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Theoretical review"]/sec/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="Theoretical review"]/sec/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Theoretical review"]/sec/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Theoretical review"]/sec/p/bold/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="Theoretical review"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)          
        
for a in root.findall('.//sec[title="Data availability"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="Data availability"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Data availability"]/sec/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Data availability"]/sec/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="Data availability"]/sec/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Data availability"]/sec/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Data availability"]/sec/p/bold/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="Data availability"]/sec/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)    
for a in root.findall('.//sec[title="Data availability"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)
        
for a in root.findall('.//sec[title="Background"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="Background"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Background"]/sec/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Background"]/sec/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="Background"]/sec/p/bold'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)     
for a in root.findall('.//sec[title="Background"]/sec/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="Background"]/sec/p/bold/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)      
for a in root.findall('.//sec[title="Background"]/sec/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)  
for a in root.findall('.//sec[title="Background"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail)

for a in root.findall('.//sec[title="DISCERN Instrument"]/title'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)   
for a in root.findall('.//sec[title="DISCERN Instrument"]/p'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail)
for a in root.findall('.//sec[title="DISCERN Instrument"]/p/italic'):
    nonImrd.append(a.text)
    nonImrd.append(a.tail) 
for a in root.findall('.//sec[title="DISCERN Instrument"]/p/'):
    if a.text not in nonImrd:
        nonImrd.append(a.text)
    if a.tail not in nonImrd:    
        nonImrd.append(a.tail) 
        
        
        
        
        
        
        
for val in nonImrd: 
    if val != None : 
        nonImrdChapter.append(val)

nonImrd_str = ''.join(nonImrdChapter)
nonImrd_str = nonImrd_str.replace("\n","");
for ele in nonImrd_str:  
    if ele in brackets:  
        nonImrd_str = nonImrd_str.replace(ele, " ")
nonImrdChapter = nonImrd_str.split()

try:
    nonImrdChapter.remove(',')
except:
    pass

#global conclusion_length
#conclusion_length = len(nonImrdChapter)