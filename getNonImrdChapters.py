import pandas as pd

def countNonImrdWords (root):

    # NonIMRD chapters
    nonImrd = []
    nonImrdChapter = []
    nonImrd_str = ""
    brackets = '''()[]{}<>'''

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

    for a in root.findall('.//sec[title="Summary"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Summary"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Summary"]/p/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Summary"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//sec[title="Summary"]/p/'):
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
            
    for a in root.findall('.//sec[title="Significant unknowns"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Significant unknowns"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Significant unknowns"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)      
    for a in root.findall('.//sec[title="Significant unknowns"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)   

    for a in root.findall('.//sec[title="Risk factors for placental malaria"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Risk factors for placental malaria"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Risk factors for placental malaria"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)      
    for a in root.findall('.//sec[title="Risk factors for placental malaria"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)  
            
    for a in root.findall('.//sec[title="Serum levels of leptin and IGF-1"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Serum levels of leptin and IGF-1"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Serum levels of leptin and IGF-1"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)      
    for a in root.findall('.//sec[title="Serum levels of leptin and IGF-1"]/p/'):
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

    for a in root.findall('.//sec[title="Selection of participants"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Selection of participants"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Selection of participants"]/p/xref'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)  
    for a in root.findall('.//sec[title="Selection of participants"]/p/list/list-item/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//sec[title="Selection of participants"]/p/'):
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

    for a in root.findall('.//sec[title="COVID-19, the NHS and high-risk patients"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="COVID-19, the NHS and high-risk patients"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="COVID-19, the NHS and high-risk patients"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="COVID-19, the NHS and high-risk patients"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    #for a in root.findall('.//sec[title="The NHS in “Contain and Delay""]/title'):
    #    nonImrd.append(a.text)
     #   nonImrd.append(a.tail)   
    #for a in root.findall('.//sec[title="The NHS in “Contain and Delay""]/p'):
    #    nonImrd.append(a.text)
    #    nonImrd.append(a.tail)
    #for a in root.findall('.//sec[title="The NHS in “Contain and Delay""]/p/italic'):
      #  nonImrd.append(a.text)
       # nonImrd.append(a.tail)
    #for a in root.findall('.//sec[title="The NHS in “Contain and Delay""]/p/'):
     #   if a.text not in nonImrd:
     #       nonImrd.append(a.text)
     #   if a.tail not in nonImrd:    
     #       nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Ambiguities of risk and vulnerability"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Ambiguities of risk and vulnerability"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Ambiguities of risk and vulnerability"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Ambiguities of risk and vulnerability"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)
            
    for a in root.findall('.//sec[title="Historicising NHS attachment and its existential threats"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Historicising NHS attachment and its existential threats"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Historicising NHS attachment and its existential threats"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Historicising NHS attachment and its existential threats"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)        
            
    for a in root.findall('.//sec[title="Other factors"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Other factors"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Other factors"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Other factors"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)
            
    for a in root.findall('.//sec[title="Proposed Research"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Proposed Research"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Proposed Research"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Proposed Research"]/list/list-item/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//sec[title="Proposed Research"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)        

    for a in root.findall('.//sec[title="Case studies"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Case studies"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Case studies"]/sec/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Case studies"]/sec/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Case studies"]/sec/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Case studies"]/sec/p/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//sec[title="Case studies"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:  
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Highlights"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Highlights"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Highlights"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Highlights"]/list/list-item/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//sec[title="Highlights"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="List of Symbols and Abbreviations"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="List of Symbols and Abbreviations"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="List of Symbols and Abbreviations"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="List of Symbols and Abbreviations"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Data sources and collections"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Data sources and collections"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Data sources and collections"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Data sources and collections"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Procedures"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Procedures"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Procedures"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Procedures"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Statistical methods"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Statistical methods"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Statistical methods"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Statistical methods"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)
            
    for a in root.findall('.//sec[title="Statistical analysis"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Statistical analysis"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Statistical analysis"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Statistical analysis"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="CHIM framework"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="CHIM framework"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="CHIM framework"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="CHIM framework"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)
            
    for a in root.findall('.//sec[title="Evaluation of content"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Evaluation of content"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Evaluation of content"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Evaluation of content"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)
            
    for a in root.findall('.//sec[title="Feasibility and timing"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Feasibility and timing"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Feasibility and timing"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Feasibility and timing"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Feasibility of incorporation into ANC system"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Feasibility of incorporation into ANC system"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Feasibility of incorporation into ANC system"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Feasibility of incorporation into ANC system"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="An extension of the Alma-Ata definition of primary health care for underserved populations in light of 21st evidence and realities"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="An extension of the Alma-Ata definition of primary health care for underserved populations in light of 21st evidence and realities"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="An extension of the Alma-Ata definition of primary health care for underserved populations in light of 21st evidence and realities"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="An extension of the Alma-Ata definition of primary health care for underserved populations in light of 21st evidence and realities"]/p/boxed-text/caption/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="An extension of the Alma-Ata definition of primary health care for underserved populations in light of 21st evidence and realities"]/p/boxed-text/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)     
    for a in root.findall('.//sec[title="An extension of the Alma-Ata definition of primary health care for underserved populations in light of 21st evidence and realities"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Further elaboration on this extended definition of primary health care"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Further elaboration on this extended definition of primary health care"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Further elaboration on this extended definition of primary health care"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Further elaboration on this extended definition of primary health care"]/list/list-item/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//sec[title="Further elaboration on this extended definition of primary health care"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="How can a core package of PHC services that are appropriate for the local context be defined?"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="How can a core package of PHC services that are appropriate for the local context be defined?"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="How can a core package of PHC services that are appropriate for the local context be defined?"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="How can a core package of PHC services that are appropriate for the local context be defined?"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)
            
    for a in root.findall('.//sec[title="The neglected demand-side approach to strengthening primary health care"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="The neglected demand-side approach to strengthening primary health care"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="The neglected demand-side approach to strengthening primary health care"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="The neglected demand-side approach to strengthening primary health care"]/list/list-item/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="The neglected demand-side approach to strengthening primary health care"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Roles of higher- and lower-level personnel"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Roles of higher- and lower-level personnel"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Roles of higher- and lower-level personnel"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Roles of higher- and lower-level personnel"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Remuneration and other incentives for frontline workers"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Remuneration and other incentives for frontline workers"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Remuneration and other incentives for frontline workers"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Remuneration and other incentives for frontline workers"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Impact of global trends on the evolution of primary health care for the disadvantaged in low-income countries"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Impact of global trends on the evolution of primary health care for the disadvantaged in low-income countries"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Impact of global trends on the evolution of primary health care for the disadvantaged in low-income countries"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Impact of global trends on the evolution of primary health care for the disadvantaged in low-income countries"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Towards a rebirth and revision of primary health care"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Towards a rebirth and revision of primary health care"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Towards a rebirth and revision of primary health care"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Towards a rebirth and revision of primary health care"]/list/list-item/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Towards a rebirth and revision of primary health care"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Blood pressure"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Blood pressure"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Blood pressure"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Blood pressure"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Haemoglobin level"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Haemoglobin level"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Haemoglobin level"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Haemoglobin level"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Biochemical and hormonal studies"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Biochemical and hormonal studies"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Biochemical and hormonal studies"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Biochemical and hormonal studies"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Echocardiographic findings"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Echocardiographic findings"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Echocardiographic findings"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Echocardiographic findings"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Limitations of the study"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Limitations of the study"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Limitations of the study"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Limitations of the study"]/list/list-item/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Limitations of the study"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Patients’ consent"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Patients’ consent"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Patients’ consent"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Patients’ consent"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)
            
    for a in root.findall('.//sec[title="Giemsa-stained blood smears for light microscopy"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Giemsa-stained blood smears for light microscopy"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Giemsa-stained blood smears for light microscopy"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Giemsa-stained blood smears for light microscopy"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Placental histology"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Placental histology"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Placental histology"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Placental histology"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Mendelian randomization assumptions and assessing causal intrauterine effects"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Mendelian randomization assumptions and assessing causal intrauterine effects"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)      
    for a in root.findall('.//sec[title="Mendelian randomization assumptions and assessing causal intrauterine effects"]/sec/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Mendelian randomization assumptions and assessing causal intrauterine effects"]/sec/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Mendelian randomization assumptions and assessing causal intrauterine effects"]/sec/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//sec[title="Mendelian randomization assumptions and assessing causal intrauterine effects"]/sec/p/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//sec[title="Mendelian randomization assumptions and assessing causal intrauterine effects"]/sec/p/bold/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)  
    for a in root.findall('.//sec[title="Mendelian randomization assumptions and assessing causal intrauterine effects"]/sec/p/italic/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Mendelian randomization assumptions and assessing causal intrauterine effects"]/sec/boxed-text/caption/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Mendelian randomization assumptions and assessing causal intrauterine effects"]/sec/boxed-text/list/list-item/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)     
    for a in root.findall('.//sec[title="Mendelian randomization assumptions and assessing causal intrauterine effects"]/sec/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Mendelian randomization assumptions and assessing causal intrauterine effects"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)
            
    for a in root.findall('.//sec[title="Methods for assessing and limiting potential violations of the exclusion restriction criteria in MR studies of maternal pregnancy (intrauterine) effects"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Methods for assessing and limiting potential violations of the exclusion restriction criteria in MR studies of maternal pregnancy (intrauterine) effects"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)      
    for a in root.findall('.//sec[title="Methods for assessing and limiting potential violations of the exclusion restriction criteria in MR studies of maternal pregnancy (intrauterine) effects"]/sec/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Methods for assessing and limiting potential violations of the exclusion restriction criteria in MR studies of maternal pregnancy (intrauterine) effects"]/sec/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Methods for assessing and limiting potential violations of the exclusion restriction criteria in MR studies of maternal pregnancy (intrauterine) effects"]/sec/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//sec[title="Methods for assessing and limiting potential violations of the exclusion restriction criteria in MR studies of maternal pregnancy (intrauterine) effects"]/sec/p/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//sec[title="Methods for assessing and limiting potential violations of the exclusion restriction criteria in MR studies of maternal pregnancy (intrauterine) effects"]/sec/p/bold/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)  
    for a in root.findall('.//sec[title="Methods for assessing and limiting potential violations of the exclusion restriction criteria in MR studies of maternal pregnancy (intrauterine) effects"]/sec/p/italic/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Methods for assessing and limiting potential violations of the exclusion restriction criteria in MR studies of maternal pregnancy (intrauterine) effects"]/sec/boxed-text/caption/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Methods for assessing and limiting potential violations of the exclusion restriction criteria in MR studies of maternal pregnancy (intrauterine) effects"]/sec/boxed-text/list/list-item/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)     
    for a in root.findall('.//sec[title="Methods for assessing and limiting potential violations of the exclusion restriction criteria in MR studies of maternal pregnancy (intrauterine) effects"]/sec/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Methods for assessing and limiting potential violations of the exclusion restriction criteria in MR studies of maternal pregnancy (intrauterine) effects"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)        

    for a in root.findall('.//sec[title="Illustrative example using real data"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Illustrative example using real data"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)      
    for a in root.findall('.//sec[title="Illustrative example using real data"]/sec/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Illustrative example using real data"]/sec/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Illustrative example using real data"]/sec/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//sec[title="Illustrative example using real data"]/sec/p/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//sec[title="Illustrative example using real data"]/sec/p/bold/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)  
    for a in root.findall('.//sec[title="Illustrative example using real data"]/sec/p/italic/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)     
    for a in root.findall('.//sec[title="Illustrative example using real data"]/sec/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Illustrative example using real data"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="Conclusions and additional comment"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Conclusions and additional comment"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)      
    for a in root.findall('.//sec[title="Conclusions and additional comment"]/sec/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Conclusions and additional comment"]/sec/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Conclusions and additional comment"]/sec/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//sec[title="Conclusions and additional comment"]/sec/p/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//sec[title="Conclusions and additional comment"]/sec/p/bold/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)  
    for a in root.findall('.//sec[title="Conclusions and additional comment"]/sec/p/italic/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)     
    for a in root.findall('.//sec[title="Conclusions and additional comment"]/sec/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Conclusions and additional comment"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)

    for a in root.findall('.//sec[title="ELISA for measuring leptin and IGF-1 levels"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="ELISA for measuring leptin and IGF-1 levels"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)      
    for a in root.findall('.//sec[title="ELISA for measuring leptin and IGF-1 levels"]/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="ELISA for measuring leptin and IGF-1 levels"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)
            
    for a in root.findall('.//sec[title="Community benefits and risks"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Community benefits and risks"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)      
    for a in root.findall('.//sec[title="Community benefits and risks"]/sec/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Community benefits and risks"]/sec/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Community benefits and risks"]/sec/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//sec[title="Community benefits and risks"]/sec/p/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//sec[title="Community benefits and risks"]/sec/p/bold/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)  
    for a in root.findall('.//sec[title="Community benefits and risks"]/sec/p/italic/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)     
    for a in root.findall('.//sec[title="Community benefits and risks"]/sec/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Community benefits and risks"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)
     
    for a in root.findall('.//sec[title="Participant motivations and risks"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Participant motivations and risks"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)      
    for a in root.findall('.//sec[title="Participant motivations and risks"]/sec/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Participant motivations and risks"]/sec/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Participant motivations and risks"]/sec/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//sec[title="Participant motivations and risks"]/sec/p/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//sec[title="Participant motivations and risks"]/sec/p/bold/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)  
    for a in root.findall('.//sec[title="Participant motivations and risks"]/sec/p/italic/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)     
    for a in root.findall('.//sec[title="Participant motivations and risks"]/sec/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Participant motivations and risks"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)
      
    for a in root.findall('.//sec[title="Barriers and challenges"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Barriers and challenges"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)      
    for a in root.findall('.//sec[title="Barriers and challenges"]/sec/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Barriers and challenges"]/sec/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Barriers and challenges"]/sec/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//sec[title="Barriers and challenges"]/sec/p/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//sec[title="Barriers and challenges"]/sec/p/bold/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)  
    for a in root.findall('.//sec[title="Barriers and challenges"]/sec/p/italic/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)     
    for a in root.findall('.//sec[title="Barriers and challenges"]/sec/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Barriers and challenges"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)
            
    for a in root.findall('.//sec[title="Perceived psychological benefits"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Perceived psychological benefits"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)      
    for a in root.findall('.//sec[title="Perceived psychological benefits"]/sec/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Perceived psychological benefits"]/sec/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Perceived psychological benefits"]/sec/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//sec[title="Perceived psychological benefits"]/sec/p/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//sec[title="Perceived psychological benefits"]/sec/p/bold/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)  
    for a in root.findall('.//sec[title="Perceived psychological benefits"]/sec/p/italic/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)     
    for a in root.findall('.//sec[title="Perceived psychological benefits"]/sec/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Perceived psychological benefits"]/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)
            
    for a in root.findall('.//sec[title="Perceived physical benefits"]/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Perceived physical benefits"]/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)      
    for a in root.findall('.//sec[title="Perceived physical benefits"]/sec/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Perceived physical benefits"]/sec/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//sec[title="Perceived physical benefits"]/sec/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//sec[title="Perceived physical benefits"]/sec/p/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//sec[title="Perceived physical benefits"]/sec/p/bold/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)  
    for a in root.findall('.//sec[title="Perceived physical benefits"]/sec/p/italic/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)     
    for a in root.findall('.//sec[title="Perceived physical benefits"]/sec/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)   
    for a in root.findall('.//sec[title="Perceived physical benefits"]/p/'):
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

    return(len(nonImrdChapter))