"""
Open research Central (ORC) document parser
Convert ORC XML documents to a standardized data structure
@authors: Antonija Mijatovic (antonija.mijatovic@mefst.hr)
"""
import string
import pandas as pd

def countImrdWords (root):
# Count the raw number of words in each IMRaD chapter per article
# Return the total raw number of words in all IMRaD chapters per article
  
    brackets = '''()[]{}<>'''
    
    # Abstract
    global abstr
    abstr = []
    abstract = []
    intro_str = ""
    global abstract_length
    abstract_length = 0
    
    for a in root.findall('.//abstract/title'):
        abstr.append(a.text)
        abstr.append(a.tail)
    for a in root.findall('.//abstract/p'):
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
    for a in root.findall('.//abstract/p/italic/bold'):
        abstr.append(a.text)
        abstr.append(a.tail) 
    for a in root.findall('.//abstract/sec/title'):
        abstr.append(a.text)
        abstr.append(a.tail)
    for a in root.findall('.//abstract/sec/p'):
        abstr.append(a.text)
        abstr.append(a.tail)    
    for a in root.findall('.//abstract/p/'):
        if a.text not in abstr:
            abstr.append(a.text)
        if a.tail not in abstr:
            abstr.append(a.tail)
        
    # Remove None values: 
    for val in abstr: 
        if val != None : 
            abstract.append(val)       
    # Convert to string: 
    abstr_str = ''.join(abstract)
    # Remove new line tags:
    abstr_str = abstr_str.replace("\n","");
    for ele in abstr_str:  
        if ele in brackets:  
            abstr_str = abstr_str.replace(ele, " ") 
    # Split string into words:    
    abstract = abstr_str.split()
    
    # Remove comma if it appears as separated list element
    # in order to avoid counting it as a word:
    abstract = [''.join(c for c in s if c not in string.punctuation) for s in abstract]
    abstract = [s for s in abstract if s]

    # Additional cleaning:
    abstract_clean = []
    for e in abstract:
        if e != '.' and e != ',' and e != '–' and e != '=':
            abstract_clean.append(e)     
    
    abstract_length = len(abstract_clean)

    # Introduction 
    intro = []
    introduction = []
    intro_str = ""
    global introduction_length
    introduction_length = 0

    for a in root.findall('.//sec[@sec-type="intro"]/title'):
        intro.append(a.text)
        intro.append(a.tail)
    for a in root.findall('.//sec[@sec-type="intro"]/p'):
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
    for a in root.findall('.//sec[@sec-type="intro"]/p/italic/bold'):
        intro.append(a.text)
        intro.append(a.tail)
    for a in root.findall('.//sec[@sec-type="intro"]/p/underline'):
        intro.append(a.text)
        intro.append(a.tail)     
    for a in root.findall('.//sec[@sec-type="intro"]/p/xref'):
        intro.append(a.text)
        intro.append(a.tail)
    for a in root.findall('.//sec[@sec-type="intro"]/p/xref/italic'):
        intro.append(a.text)
        intro.append(a.tail)
    for a in root.findall('.//sec[@sec-type="intro"]/p/xref/'):
        if a.text not in intro:
            intro.append(a.text)
        if a.text == 'et al':
            intro.append(a.text)      
        if a.tail not in intro:
            intro.append(a.tail)    
    for a in root.findall('.//sec[@sec-type="intro"]/list/list-item/p'):
        intro.append(a.text)
        intro.append(a.tail)
    for a in root.findall('.//sec[@sec-type="intro"]/p/boxed-text/p'):
        intro.append(a.text)
        intro.append(a.tail)    
    # Subsections:        
    for a in root.findall('.//sec[@sec-type="intro"]/sec/title'):
        intro.append(a.text)
        intro.append(a.tail)         
    for a in root.findall('.//sec[@sec-type="intro"]/sec/p'):
        intro.append(a.text)
        intro.append(a.tail)  
    for a in root.findall('.//sec[@sec-type="intro"]/sec/p/underline'):
        intro.append(a.text)
        intro.append(a.tail)     
    for a in root.findall('.//sec[@sec-type="intro"]/sec/p/italic'):
        intro.append(a.text)
        intro.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="intro"]/sec/p/bold'):
        intro.append(a.text)
        intro.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="intro"]/sec/p/italic/bold'):
        intro.append(a.text)
        intro.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="intro"]/sec/p/bold/italic'):
        intro.append(a.text)
        intro.append(a.tail)     
    for a in root.findall('.//sec[@sec-type="intro"]/sec/list/list-item/p'):
        intro.append(a.text)
        intro.append(a.tail)  
    for a in root.findall('.//sec[@sec-type="intro"]/sec/p/boxed-text/caption/title'):
        intro.append(a.text)
        intro.append(a.tail)
    for a in root.findall('.//sec[@sec-type="intro"]/sec/p/boxed-text/p'):
        intro.append(a.text)
        intro.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="intro"]/sec/p/boxed-text/p/italic'):
        intro.append(a.text)
        intro.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="intro"]/sec/p/xref'):
        intro.append(a.text)
        intro.append(a.tail)  
    for a in root.findall('.//sec[@sec-type="intro"]/sec/p/xref/italic'):
        intro.append(a.text)
        intro.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="intro"]/sec/p/xref/'):
        if a.text not in intro:
            intro.append(a.text)
        if a.text == 'et al':
            intro.append(a.text)      
        if a.tail not in intro:
            intro.append(a.tail)          
    for a in root.findall('.//sec[@sec-type="intro"]/sec/p/'):
        if a.text not in intro:
            intro.append(a.text)
        if a.tail not in intro:
            intro.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="intro"]/p/'):
        if a.text not in intro:
            intro.append(a.text)
        if a.tail not in intro:
            intro.append(a.tail)        
        
    for val in intro: 
        if val != None : 
            introduction.append(val)
            
    intro_str = ''.join(introduction) 
    intro_str = intro_str.replace("\n","");
    for ele in intro_str:  
        if ele in brackets:  
            intro_str = intro_str.replace(ele, " ")
    introduction = intro_str.split()
    
    introduction = [''.join(c for c in s if c not in string.punctuation) for s in introduction]
    introduction = [s for s in introduction if s]

    # Additional cleaning:
    introduction_clean = []
    for e in introduction:
        if e != '.' and e != ',' and e != '–' and e != '=':
            introduction_clean.append(e)
            
    introduction_length = len(introduction_clean)

    # Methods
    met = []
    methods = []
    met_str = ""
    global methods_length
    methods_length = 0
    
    for a in root.findall('.//sec[@sec-type="methods"]/title'):
        met.append(a.text)
        met.append(a.tail)
    for a in root.findall('.//sec[@sec-type="methods"]/p'):
        met.append(a.text)
        met.append(a.tail)
    for a in root.findall('.//sec[@sec-type="methods"]/p/italic'):
        met.append(a.text)
        met.append(a.tail)
    for a in root.findall('.//sec[@sec-type="methods"]/p/bold'):
        met.append(a.text)
        met.append(a.tail)
    for a in root.findall('.//sec[@sec-type="methods"]/p/italic/bold'):
        met.append(a.text)
        met.append(a.tail)
    for a in root.findall('.//sec[@sec-type="methods"]/p/bold/italic'):
        met.append(a.text)
        met.append(a.tail)
    for a in root.findall('.//sec[@sec-type="methods"]/p/underline'):
        met.append(a.text)
        met.append(a.tail)
    for a in root.findall('.//sec[@sec-type="methods"]/list/list-item/p'):
        met.append(a.text)
        met.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="methods"]/boxed-text/p'):
        met.append(a.text)
        met.append(a.tail)         
    for a in root.findall('.//sec[@sec-type="methods"]/p/xref'):
        met.append(a.text)
        met.append(a.tail)   
    for a in root.findall('.//sec[@sec-type="methods"]/p/xref/'):
        if a.text not in met:
            met.append(a.text)
        if a.text == 'et al':
            met.append(a.text)      
        if a.tail not in met:
            met.append(a.tail)    
    # Subsections:    
    for a in root.findall('.//sec[@sec-type="methods"]/sec/title'):
        met.append(a.text)
        met.append(a.tail)
    for a in root.findall('.//sec[@sec-type="methods"]/sec/p'):
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
    for a in root.findall('.//sec[@sec-type="methods"]/sec/p/italic/bold'):
        met.append(a.text)
        met.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="methods"]/sec/p/boxed-text/p'):
        met.append(a.text)
        met.append(a.tail)        
    for a in root.findall('.//sec[@sec-type="methods"]/sec/list/list-item/p'):
        met.append(a.text)
        met.append(a.tail)     
    for a in root.findall('.//sec[@sec-type="methods"]/sec/list/list-item/p/italic'):
        met.append(a.text)
        met.append(a.tail)
    for a in root.findall('.//sec[@sec-type="methods"]/sec/list/list-item/p/bold'):
        met.append(a.text)
        met.append(a.tail)
    for a in root.findall('.//sec[@sec-type="methods"]/sec/boxed-text/p'):
        met.append(a.text)
        met.append(a.tail)        
    for a in root.findall('.//sec[@sec-type="methods"]/sec/p/xref'):
        met.append(a.text)
        met.append(a.tail)
    for a in root.findall('.//sec[@sec-type="methods"]/sec/p/xref/italic'):
        met.append(a.text)
        met.append(a.tail)        
    for a in root.findall('.//sec[@sec-type="methods"]/sec/p/xref/'):
        if a.text not in met:
            met.append(a.text)
        if a.text == 'et al':
            met.append(a.text)    
        if a.tail not in met:
            met.append(a.tail)           
    for a in root.findall('.//sec[@sec-type="methods"]/sec/p/'):
        if a.text not in met:
            met.append(a.text)
        if a.tail not in met:
            met.append(a.tail)
    for a in root.findall('.//sec[@sec-type="methods"]/p/'):
        if a.text not in met:
            met.append(a.text)
        if a.tail not in met:
            met.append(a.tail)  
    if len(met) == 0:
        for a in root.findall('.//sec[@sec-type="materials | methods"]/title'):
            met.append(a.text)
            met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="materials | methods"]/p'):
            met.append(a.text)
            met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="materials | methods"]/p/underline'):
            met.append(a.text)
            met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="materials | methods"]/p/italic'):
            met.append(a.text)
            met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="materials | methods"]/p/bold'):
            met.append(a.text)
            met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="materials | methods"]/p/italic/bold'):
            met.append(a.text)
            met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="materials | methods"]/p/bold/italic'):
            met.append(a.text)
            met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="materials | methods"]/p/xref'):
            met.append(a.text)
            met.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="materials | methods"]/p/xref/italic'):
            met.append(a.text)
            met.append(a.tail)              
        for a in root.findall('.//sec[@sec-type="materials | methods"]/p/xref/'):
            if a.text not in met:
                met.append(a.text)
            if a.tail not in met:
                met.append(a.tail)    
        # Subsections:            
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/title'):
            met.append(a.text)
            met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/p'):
            met.append(a.text)
            met.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/p/underline'):
            met.append(a.text)
            met.append(a.tail)             
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/p/italic'):
            met.append(a.text)
            met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/p/bold'):
            met.append(a.text)
            met.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/p/bold/italic'):
            met.append(a.text)
            met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/p/italic/bold'):
            met.append(a.text)
            met.append(a.tail)    
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/list/list-item/p'):
            met.append(a.text)
            met.append(a.tail)     
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/list/list-item/p/italic'):
            met.append(a.text)
            met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/list/list-item/p/bold'):
            met.append(a.text)
            met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/boxed-text/p'):
            met.append(a.text)
            met.append(a.tail)     
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/p/xref'):
            met.append(a.text)
            met.append(a.tail)   
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/p/xref/'):
            if a.text not in met:
                met.append(a.text)
            if a.tail not in met:
                met.append(a.tail)    
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/p/'):
            if a.text not in met:
                met.append(a.text)
            if a.tail not in met:
                met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="materials | methods"]/p/'):
            if a.text not in met:
                met.append(a.text)
            if a.tail not in met:
                met.append(a.tail) 
        if len(met) == 0:
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/title'):
                met.append(a.text)
                met.append(a.tail)
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/p'):
                met.append(a.text)
                met.append(a.tail)
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/p/underline'):
                met.append(a.text)
                met.append(a.tail)
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/p/italic'):
                met.append(a.text)
                met.append(a.tail)
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/p/bold'):
                met.append(a.text)
                met.append(a.tail)
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/p/italic/bold'):
                met.append(a.text)
                met.append(a.tail)
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/p/bold/italic'):
                met.append(a.text)
                met.append(a.tail)
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/list/list-item/p'):
                met.append(a.text)
                met.append(a.tail) 
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/p/xref'):
                met.append(a.text)
                met.append(a.tail)   
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/p/xref/'):
                if a.text not in met:
                    met.append(a.text)
                if a.tail not in met:
                    met.append(a.tail)                 
            # Subsections:    
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/sec/title'):
                met.append(a.text)
                met.append(a.tail)
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/sec/p'):
                met.append(a.text)
                met.append(a.tail)                
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/sec/p/italic'):
                met.append(a.text)
                met.append(a.tail)
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/sec/p/bold'):
                met.append(a.text)
                met.append(a.tail) 
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/sec/p/bold/italic'):
                met.append(a.text)
                met.append(a.tail)
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/sec/p/italic/bold'):
                met.append(a.text)
                met.append(a.tail)    
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/sec/list/list-item/p'):
                met.append(a.text)
                met.append(a.tail)     
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/sec/list/list-item/p/italic'):
                met.append(a.text)
                met.append(a.tail)
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/sec/boxed-text/p'):
                met.append(a.text)
                met.append(a.tail)                    
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/sec/p/xref'):
                met.append(a.text)
                met.append(a.tail)
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/sec/p/xref/italic'):
                met.append(a.text)
                met.append(a.tail)                
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/sec/p/xref/'):
                if a.text not in met:
                    met.append(a.text)
                if a.tail not in met:
                    met.append(a.tail)                 
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/sec/p/'):
                if a.text not in met:
                    met.append(a.text)
                if a.tail not in met:
                    met.append(a.tail)
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/p/'):
                if a.text not in met:
                    met.append(a.text)
                if a.tail not in met:
                    met.append(a.tail)        

    for val in met: 
        if val != None : 
            methods.append(val) 
    met_str = ''.join(methods)
    met_str = met_str.replace("\n","");
    for ele in met_str:  
        if ele in brackets:  
            met_str = met_str.replace(ele, " ")
    methods = met_str.split()

    methods = [''.join(c for c in s if c not in string.punctuation) for s in methods]
    methods = [s for s in methods if s]

    # Additional cleaning:
    methods_clean = []
    for e in methods:
        if e != '.' and e != ',' and e != '–' and e != '=':
            methods_clean.append(e)
            
    methods_length = len(methods_clean)

    # Results
    res = []
    results = []
    res_str = ""
    global results_length
    results_length = 0
    global resultDiscussTogether
    resultDiscussTogether = False
    global discussResMerged
    discussResMerged = False
    
    for a in root.findall('.//sec[@sec-type="results"]/title'):
        res.append(a.text)
        res.append(a.tail)
    for a in root.findall('.//sec[@sec-type="results"]/p'):
        res.append(a.text)
        res.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="results"]/p/underline'):
        res.append(a.text)
        res.append(a.tail)
    for a in root.findall('.//sec[@sec-type="results"]/p/italic'):
        res.append(a.text)
        res.append(a.tail)
    for a in root.findall('.//sec[@sec-type="results"]/p/bold'):
        res.append(a.text)
        res.append(a.tail)
    for a in root.findall('.//sec[@sec-type="results"]/p/italic/bold'):
        res.append(a.text)
        res.append(a.tail)
    for a in root.findall('.//sec[@sec-type="results"]/p/bold/italic'):
        res.append(a.text)
        res.append(a.tail)
    for a in root.findall('.//sec[@sec-type="results"]/boxed-text/p'):
        res.append(a.text)
        res.append(a.tail)          
    for a in root.findall('.//sec[@sec-type="results"]/list/list-item/p'):
        res.append(a.text)
        res.append(a.tail)         
    for a in root.findall('.//sec[@sec-type="results"]/list/list-item/p/bold'):
        res.append(a.text)
        res.append(a.tail)     
    for a in root.findall('.//sec[@sec-type="results"]/list/list-item/p/italic'):
        res.append(a.text)
        res.append(a.tail)
    for a in root.findall('.//sec[@sec-type="results"]/p/xref'):
        res.append(a.text)
        res.append(a.tail)  
    for a in root.findall('.//sec[@sec-type="results"]/p/xref/italic'):
        res.append(a.text)
        res.append(a.tail)        
    for a in root.findall('.//sec[@sec-type="results"]/p/xref/'):
        if a.text not in res:      
            res.append(a.text)
        if a.tail not in res:    
            res.append(a.tail)        
    # Subsections:  
    for a in root.findall('.//sec[@sec-type="results"]/sec/title'):
        res.append(a.text)
        res.append(a.tail)
    for a in root.findall('.//sec[@sec-type="results"]/sec/p'):
        res.append(a.text)
        res.append(a.tail)
    for a in root.findall('.//sec[@sec-type="results"]/sec/p/underline'):
        res.append(a.text)
        res.append(a.tail)         
    for a in root.findall('.//sec[@sec-type="results"]/sec/p/italic'):
        res.append(a.text)
        res.append(a.tail)
    for a in root.findall('.//sec[@sec-type="results"]/sec/p/bold'):
        res.append(a.text)
        res.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="results"]/sec/p/italic/bold'):
        res.append(a.text)
        res.append(a.tail)     
    for a in root.findall('.//sec[@sec-type="results"]/sec/p/bold/italic'):
        res.append(a.text)
        res.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="results"]/sec/boxed-text/p'):
        res.append(a.text)
        res.append(a.tail)     
    for a in root.findall('.//sec[@sec-type="results"]/sec/list/list-item/p'):
        res.append(a.text)
        res.append(a.tail)     
    for a in root.findall('.//sec[@sec-type="results"]/sec/list/list-item/p/italic'):
        res.append(a.text)
        res.append(a.tail)  
    for a in root.findall('.//sec[@sec-type="results"]/sec/list/list-item/p/bold'):
        res.append(a.text)
        res.append(a.tail)        
    for a in root.findall('.//sec[@sec-type="results"]/sec/p/xref'):
        res.append(a.text)
        res.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="results"]/sec/p/xref/italic'):
        res.append(a.text)
        res.append(a.tail)        
    for a in root.findall('.//sec[@sec-type="results"]/sec/p/xref/'):
        if a.text not in res:      
            res.append(a.text)
        if a.text == 'et al':
            res.append(a.text)    
        if a.tail not in res:    
            res.append(a.tail)   
    for a in root.findall('.//sec[@sec-type="results"]/sec/p/'):
        if a.text not in res:      
            res.append(a.text)
        if a.tail not in res:    
            res.append(a.tail)    
    for a in root.findall('.//sec[@sec-type="results"]/p/'):
        if a.text not in res:      
            res.append(a.text)
        if a.tail not in res:    
            res.append(a.tail)        
    # Somethimes Results and Discussion are under same section:    
    if len(res) == 0:
        for a in root.findall('.//sec[@sec-type="results | discussion"]/title'):
            res.append(a.text)
            res.append(a.tail)
        for a in root.findall('.//sec[@sec-type="results | discussion"]/p'):
            res.append(a.text)
            res.append(a.tail)
        for a in root.findall('.//sec[@sec-type="results | discussion"]/p/italic'):
            res.append(a.text)
            res.append(a.tail)
        for a in root.findall('.//sec[@sec-type="results | discussion"]/p/bold'):
            res.append(a.text)
            res.append(a.tail)
        for a in root.findall('.//sec[@sec-type="results | discussion"]/p/italic/bold'):
            res.append(a.text)
            res.append(a.tail)
        for a in root.findall('.//sec[@sec-type="results | discussion"]/p/bold/italic'):
            res.append(a.text)
            res.append(a.tail)
        for a in root.findall('.//sec[@sec-type="results | discussion"]/p/underline'):
            res.append(a.text)
            res.append(a.tail)
        for a in root.findall('.//sec[@sec-type="results | discussion"]/p/xref'):
            res.append(a.text)
            res.append(a.tail)    
        # Subsections:            
        for a in root.findall('.//sec[@sec-type="results | discussion"]/sec/title'):
            res.append(a.text)
            res.append(a.tail)    
        for a in root.findall('.//sec[@sec-type="results | discussion"]/sec/p'):
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
        for a in root.findall('.//sec[@sec-type="results | discussion"]/sec/p/italic/bold'):
            res.append(a.text)
            res.append(a.tail)
        for a in root.findall('.//sec[@sec-type="results | discussion"]/sec/list/list-item/p'):
            res.append(a.text)
            res.append(a.tail)
        for a in root.findall('.//sec[@sec-type="results | discussion"]/sec/boxed-text/caption/p'):
            res.append(a.text)
            res.append(a.tail)
        for a in root.findall('.//sec[@sec-type="results | discussion"]/sec/boxed-text/p'):
            res.append(a.text)
            res.append(a.tail)             
        for a in root.findall('.//sec[@sec-type="results | discussion"]/sec/p/xref'):
            res.append(a.text)
            res.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="results | discussion"]/sec/p/xref/italic'):
            res.append(a.text)
            res.append(a.tail)
        for a in root.findall('.//sec[@sec-type="results | discussion"]/sec/p/xref/'):
            if a.text not in res:      
                res.append(a.text)
            if a.text == 'et al':
                res.append(a.text)    
            if a.tail not in res:    
                res.append(a.tail)             
        if len(res) != 0: 
            resultDiscussTogether = True

    for val in res: 
        if val != None : 
            results.append(val) 

    res_str = ''.join(results)
    res_str = res_str.replace("\n","");
    for ele in res_str:  
        if ele in brackets:  
            res_str = res_str.replace(ele, " ")
    results = res_str.split()

    results = [''.join(c for c in s if c not in string.punctuation) for s in results]
    results = [s for s in results if s]

    # Additional cleaning:
    results_clean = []
    for e in results:
        if e != '.' and e != ',' and e != '–' and e != '=':
            results_clean.append(e)
            
    results_length = len(results_clean)  
        
    # Discussion
    discuss = []
    discussion = [] 
    discuss_str = ""  
    global discussion_length
    discussion_length = 0
    
    for a in root.findall('.//sec[@sec-type="discussion"]/title'):
        discuss.append(a.text) 
        discuss.append(a.tail)
    for a in root.findall('.//sec[@sec-type="discussion"]/p'):
        discuss.append(a.text) 
        discuss.append(a.tail)
    for a in root.findall('.//sec[@sec-type="discussion"]/p/italic'):
        discuss.append(a.text) 
        discuss.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="discussion"]/p/bold'):
        discuss.append(a.text) 
        discuss.append(a.tail)
    for a in root.findall('.//sec[@sec-type="discussion"]/p/bold/italic'):
        discuss.append(a.text) 
        discuss.append(a.tail)
    for a in root.findall('.//sec[@sec-type="discussion"]/p/italic/bold'):
        discuss.append(a.text) 
        discuss.append(a.tail)
    for a in root.findall('.//sec[@sec-type="discussion"]/list/list_item/p'):
        discuss.append(a.text) 
        discuss.append(a.tail)
    for a in root.findall('.//sec[@sec-type="discussion"]/p/xref'):
        discuss.append(a.text)
        discuss.append(a.tail)
    for a in root.findall('.//sec[@sec-type="discussion"]/p/xref/italic'):
        discuss.append(a.text)
        discuss.append(a.tail)         
    for a in root.findall('.//sec[@sec-type="discussion"]/p/xref/'):
        if a.text not in discuss:
            discuss.append(a.text) 
        if a.tail not in discuss:      
            discuss.append(a.tail)         
    # Subsection:    
    for a in root.findall('.//sec[@sec-type="discussion"]/sec/title'):
        discuss.append(a.text) 
        discuss.append(a.tail)    
    for a in root.findall('.//sec[@sec-type="discussion"]/sec/p'):
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
    for a in root.findall('.//sec[@sec-type="discussion"]/sec/p/italic/bold'):
        discuss.append(a.text) 
        discuss.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="discussion"]/sec/list/list-item/p'):
        discuss.append(a.text) 
        discuss.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="discussion"]/sec/list/list-item/p/italic'):
        discuss.append(a.text) 
        discuss.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="discussion"]/sec/list/list-item/p/bold'):
        discuss.append(a.text) 
        discuss.append(a.tail)      
    for a in root.findall('.//sec[@sec-type="discussion"]/sec/boxed-text/p'):
        discuss.append(a.text) 
        discuss.append(a.tail)
    for a in root.findall('.//sec[@sec-type="discussion"]/sec/p/xref'):
        discuss.append(a.text) 
        discuss.append(a.tail)
    for a in root.findall('.//sec[@sec-type="discussion"]/sec/p/xref/'):    
        if a.text not in discuss:
            discuss.append(a.text) 
        if a.tail not in discuss:      
            discuss.append(a.tail)         
    for a in root.findall('.//sec[@sec-type="discussion"]/sec/p/'):
        if a.text not in discuss:
            discuss.append(a.text) 
        if a.tail not in discuss:      
            discuss.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="discussion"]/p/'):
        if a.text not in discuss:
            discuss.append(a.text) 
        if a.tail not in discuss:      
            discuss.append(a.tail)
    if len(discuss) == 0:
        # Sometimes Discussion and Conclusions are uder one chapter:
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/title'):
            discuss.append(a.text) 
            discuss.append(a.tail)
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/p'):
            discuss.append(a.text) 
            discuss.append(a.tail)
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/p/italic'):
            discuss.append(a.text) 
            discuss.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/p/bold'):
            discuss.append(a.text) 
            discuss.append(a.tail)
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/p/xref'):
            discuss.append(a.text)
            discuss.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/p/xref/italic'):
            discuss.append(a.text)
            discuss.append(a.tail)     
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/p/xref/'):
            if a.text not in discuss:
                discuss.append(a.text) 
            if a.tail not in discuss:      
                discuss.append(a.tail)
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/list/list-item/p'):
            discuss.append(a.text) 
            discuss.append(a.tail)             
        # Subsections:    
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/sec/title'):
            discuss.append(a.text) 
            discuss.append(a.tail)    
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/sec/p'):
            discuss.append(a.text) 
            discuss.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/sec/p/underline'):
            discuss.append(a.text) 
            discuss.append(a.tail)            
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/sec/p/italic'):
            discuss.append(a.text) 
            discuss.append(a.tail)
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/sec/p/bold'):
            discuss.append(a.text) 
            discuss.append(a.tail)
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/sec/p/bold/italic'):
            discuss.append(a.text) 
            discuss.append(a.tail)
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/sec/p/italic/bold'):
            discuss.append(a.text) 
            discuss.append(a.tail)  
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/sec/list/list-item/p'):
            discuss.append(a.text) 
            discuss.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/sec//list/list-item/p/italic'):
            discuss.append(a.text) 
            discuss.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/sec/boxed-text/caption/p'):
            discuss.append(a.text) 
            discuss.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/sec/boxed-text/p'):
            discuss.append(a.text) 
            discuss.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/sec/p/xref'):
            discuss.append(a.text) 
            discuss.append(a.tail)   
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/sec/p/xref/italic'):
            discuss.append(a.text) 
            discuss.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/sec/p/xref/'):
            if a.text not in discuss:
                discuss.append(a.text) 
            if a.tail not in discuss:      
                discuss.append(a.tail)            
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/sec/p/'):
            if a.text not in discuss:
                discuss.append(a.text) 
            if a.tail not in discuss:      
                discuss.append(a.tail)                
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/p/'):
            if a.text not in discuss:
                discuss.append(a.text) 
            if a.tail not in discuss:      
                discuss.append(a.tail)
        if len(discuss) != 0:
            discussResMerged = True
            
    
    for val in discuss: 
        if val != None: 
            discussion.append(val)    
    discuss_str = ''.join(discussion)
    
    discuss_str = discuss_str.replace("\n","");
    for ele in discuss_str:  
        if ele in brackets:  
            discuss_str = discuss_str.replace(ele, " ")
                
    discussion = discuss_str.split()
    
    discussion = [''.join(c for c in s if c not in string.punctuation) for s in discussion]
    discussion = [s for s in discussion if s]
    
    discussion_clean = []
    for e in discussion:
        if e != '.' and e != ',' and e != '–' and e != '=':
            discussion_clean.append(e)
            
    discussion_length = len(discussion_clean)
          
    # Conclusion
    concl = []
    conclusion = []
    concl_str = ""   
    global conclusion_length
    conclusion_length = 0
    
    for a in root.findall('.//sec[@sec-type="conclusions"]/title'):
        concl.append(a.text)
        concl.append(a.tail)   
    for a in root.findall('.//sec[@sec-type="conclusions"]/p'):
        concl.append(a.text)
        concl.append(a.tail)
    for a in root.findall('.//sec[@sec-type="conclusions"]/p/underline'):
        concl.append(a.text)
        concl.append(a.tail)     
    for a in root.findall('.//sec[@sec-type="conclusions"]/p/italic'):
        concl.append(a.text)
        concl.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="conclusions"]/p/bold'):
        concl.append(a.text)
        concl.append(a.tail)
    for a in root.findall('.//sec[@sec-type="conclusions"]/p/bold/italic'):
        concl.append(a.text)
        concl.append(a.tail)
    for a in root.findall('.//sec[@sec-type="conclusions"]/p/italic/bold'):
        concl.append(a.text)
        concl.append(a.tail)
    for a in root.findall('.//sec[@sec-type="conclusions"]/list/list-item/p'):
        concl.append(a.text)
        concl.append(a.tail)
    for a in root.findall('.//sec[@sec-type="conclusions"]/boxed-text/p'):
        concl.append(a.text)
        concl.append(a.tail)
    for a in root.findall('.//sec[@sec-type="conclusions"]/p/xref'):
        concl.append(a.text)
        concl.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="conclusions"]/p/xref/italic'):
        concl.append(a.text)
        concl.append(a.tail)         
    for a in root.findall('.//sec[@sec-type="conclusions"]/p/xref/'):
        if a.text not in concl:
            concl.append(a.text)
        if a.tail not in concl:    
            concl.append(a.tail)         
    # Subsections:         
    for a in root.findall('.//sec[@sec-type="conclusions"]/sec/title'):
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
    for a in root.findall('.//sec[@sec-type="conclusions"]/sec/p/italic/bold'):
        concl.append(a.text)
        concl.append(a.tail)
    for a in root.findall('.//sec[@sec-type="conclusions"]/sec/list/list-item/p'):
        concl.append(a.text)
        concl.append(a.tail)
    for a in root.findall('.//sec[@sec-type="conclusions"]/sec/boxed-text/caption/p'):
        concl.append(a.text)
        concl.append(a.tail)
    for a in root.findall('.//sec[@sec-type="conclusions"]/sec/p/boxed-text/p'):
        concl.append(a.text)
        concl.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="conclusions"]/sec/p/xref'):
        concl.append(a.text)
        concl.append(a.tail)
    for a in root.findall('.//sec[@sec-type="conclusions"]/sec/p/xref/'): 
        if a.text not in concl:
            concl.append(a.text)
        if a.tail not in concl:    
            concl.append(a.tail)      
    for a in root.findall('.//sec[@sec-type="conclusions"]/sec/p/'):
        if a.text not in concl:
            concl.append(a.text)
        if a.tail not in concl:    
            concl.append(a.tail)    
    for a in root.findall('.//sec[@sec-type="conclusions"]/p/'):
        if a.text not in concl:
            concl.append(a.text)
        if a.tail not in concl:    
            concl.append(a.tail)
    if len(concl) == 0:
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/title'):
            concl.append(a.text)
            concl.append(a.tail)   
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/p'):
            concl.append(a.text)
            concl.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/p/italic'):
            concl.append(a.text)
            concl.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/p/bold'):
            concl.append(a.text)
            concl.append(a.tail)
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/p/italic/bold'):
            concl.append(a.text)
            concl.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/p/bold/italic'):
            concl.append(a.text)
            concl.append(a.tail)             
        # Subsections:            
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/sec/title'):
            concl.append(a.text)
            concl.append(a.tail)   
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/sec/p'):
            concl.append(a.text)
            concl.append(a.tail)
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/sec/p/italic'):
            concl.append(a.text)
            concl.append(a.tail)    
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/sec/p/bold'):
            concl.append(a.text)
            concl.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/sec/p/bold/italic'):
            concl.append(a.text)
            concl.append(a.tail)  
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/sec/p/italic/bold'):
            concl.append(a.text)
            concl.append(a.tail)
        
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/sec/list/list-item/p'):
            concl.append(a.text)
            concl.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/sec/boxed-text/caption/title'):
            concl.append(a.text)
            concl.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/boxed-text/p'):
            concl.append(a.text)
            concl.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/sec/p/xref'):
            concl.append(a.text)
            concl.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/sec/p/xref/italic'):
            concl.append(a.text)
            concl.append(a.tail)
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/sec/p/xref/'):
            if a.text not in concl:
                concl.append(a.text)
            if a.tail not in concl:    
                concl.append(a.tail)            
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/sec/p/'):
            if a.text not in concl:
                concl.append(a.text)
            if a.tail not in concl:    
                concl.append(a.tail)   
        for a in root.findall('.//sec[@sec-type="summary | conclusions"]/p/'):
            if a.text not in concl:
                concl.append(a.text)
            if a.tail not in concl:    
                concl.append(a.tail) 
        
    for val in concl: 
        if val != None : 
            conclusion.append(val)
            
    concl_str = ''.join(conclusion)
    concl_str = concl_str.replace("\n","");
    for ele in concl_str:  
        if ele in brackets:  
            concl_str = concl_str.replace(ele, " ")
    conclusion = concl_str.split()
    
    conclusion = [''.join(c for c in s if c not in string.punctuation) for s in conclusion]
    conclusion = [s for s in conclusion if s]
    
    conclusion_clean = []
    for e in conclusion:
        if e != '.' and e != ',' and e != '–' and e != '=':
            conclusion_clean.append(e)
            
    conclusion_length = len(conclusion_clean)
    
    # Word number
    return (abstract_length +  introduction_length + methods_length + 
            results_length + discussion_length + conclusion_length)
            
            
def createImrdDf (current_doi):
# Create a pandas DataFrame containing IMRaD chapters information           
            
    global imrd_info
    imrd_info = pd.DataFrame({'doi':[current_doi],                            
                              'abstractSize':[abstract_length],
                              'introductionSize':[introduction_length],
                              'methodSize':[methods_length],
                              'resultSize':[results_length],
                              'discussionSize':[discussion_length],
                              'ResultDiscussMerged': [resultDiscussTogether],
                              'DiscussConclMerged': [discussResMerged],
                              'conclusionSize':[conclusion_length]})
                              
    print("\nIMRaD information: \n")
    print(imrd_info)
    return(imrd_info)
    
def countAllWords (root):
# Count the total raw number of words per article

    # All chapters
    nonImrd = []
    nonImrdChapter = []
    nonImrd_str = ""
    brackets = '''()[]{}<>'''

    for a in root.findall('.//body/sec/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//body/sec/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//body/sec/p/underline'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//body/sec/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//body/sec/p/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//body/sec/p/bold/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//body/sec/p/italic/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)        
    for a in root.findall('.//body/sec/p/boxed-text/caption/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//body/sec/p/boxed-text/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)  
    for a in root.findall('.//body/sec/p/xref'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//body/sec/p/xref/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)         
    for a in root.findall('.//body/sec/p/xref/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail) 
    for a in root.findall('.//body/sec/list/list-item/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//body/sec/list/list-item/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//body/sec/list/list-item/p/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)  
    for a in root.findall('.//body/sec/list/list-item/p/italic/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)  
    for a in root.findall('.//body/sec/list/list-item/p/bold/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    # Subsections:    
    for a in root.findall('.//body/sec/sec/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//body/sec/sec/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//body/sec/sec/p/underline'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//body/sec/sec/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//body/sec/sec/p/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//body/sec/sec/p/bold/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//body/sec/sec/p/italic/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)        
    for a in root.findall('.//body/sec/sec/p/boxed-text/caption/title'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//body/sec/sec/p/boxed-text/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//body/sec/sec/p/boxed-text/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//body/sec/sec/p/boxed-text/p/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//body/sec/sec/p/boxed-text/p/italic/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)         
    for a in root.findall('.//body/sec/sec/p/boxed-text/p/bold/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)         
    for a in root.findall('.//body/sec/sec/p/xref'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//body/sec/sec/p/xref/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//body/sec/sec/p/sup'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)     
    for a in root.findall('.//body/sec/sec/sup'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)            
    for a in root.findall('.//body/sec/sec/p/xref/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.text == 'et al':
            nonImrd.append(a.text)      
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail) 
    for a in root.findall('.//body/sec/sec/p/sup/ext-link'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//body/sec/sec/p/ext-link'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)         
    for a in root.findall('.//body/sec/sec/list/list-item/p'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//body/sec/sec/list/list-item/p/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail) 
    for a in root.findall('.//body/sec/sec/list/list-item/p/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)  
    for a in root.findall('.//body/sec/sec/list/list-item/p/italic/bold'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//body/sec/sec/list/list-item/p/bold/italic'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//body/sec/sec/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)           
    for a in root.findall('.//body/sec/p/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)
    
    # Sometimes abstract is not part of the body but part of front/article-meta:    
    for elem in abstr:
        if elem not in nonImrd:
            nonImrd.append(elem)        
            
    for val in nonImrd: 
        if val != None : 
            nonImrdChapter.append(val)

    nonImrd_str = ''.join(nonImrdChapter)
    nonImrd_str = nonImrd_str.replace("\n","");
    nonImrdChapter = nonImrd_str.split()

    nonImrdChapter = [''.join(c for c in s if c not in string.punctuation) for s in nonImrdChapter]
    nonImrdChapter = [s for s in nonImrdChapter if s]     

    # Additional cleaning:
    nonImrdChapter_clean = []
    for e in nonImrdChapter:
        if e != '.' and e != ',' and e != '–' and e != '=':
            nonImrdChapter_clean.append(e)     
 
    return(len(nonImrdChapter_clean))            
    
def getChapterTitles (root, current_doi):

    chaptTitl = []
    chapterTitles = []
    isImrd = False
    
    # Striclty IMRaD list:
    strictImrdlist = ['Introduction', 'Background', 'Method', 'Methods', 'Material and methods', 'Materials and methods', 'Subjects and methods', 
                      'Result', 'Results', 'Results: Applying the ecological framework to the findings', 'Result and discussion', 'Results and discussion',
                      'Discussion', 'Discussions', 'Discussion and conclusion', 'Discussion and conclusions', 'Discussion/Conclusions',
                      'Conclusion', 'Conclusions', 'Conclusions and discussion', 'Conclusions and recommendations', 'Conclusions and future directions', 'Conclusions and additional comment']
    
    # Chapters that are not strictly IMRaD but they still belong to scientific paper format:
    imrdList = ['Abstract', 'Introduction', 'Abbreviations', 'Addendum', 'Data availability', 'Background', 'List of Symbols and Abbreviations', 'List of abbreviations:', 'Theory and Hypotheses',
                'Method', 'Methods', 'Material and methods', 'Materials and methods', 'Subjects and methods', 
                'Result', 'Results', 'Results: Applying the ecological framework to the findings', 'Result and discussion', 'Results and discussion',
                'Discussion', 'Discussions', 'Discussion and conclusion', 'Discussion and conclusions', 'Discussion/Conclusions',
                'Conclusion', 'Conclusions', 'Conclusions and discussion', 'Conclusions and recommendations', 'Conclusions and future directions', 'Conclusions and additional comment',
                'Consent and ethical approval', 'Ethical approval', 'Consent', 'Ethical considerations', 'Ethical statement', 'Ethics and consent', 'Ethics compliance', 'Ethics approval and consent', 'Ethics approval and consent to participate', 'Ethical issues',
                'Summary', 'Lay summary', 'Summary and conclusion', 'Author information', 'Other published results', 'Respondents', 'Data', 'Objective', 'Supplementary material', 'Appendix', 'Software availability',
                'Limitations', 'Strengths and limitations', 'Limitations and Future Directions', 'Lessons learned and recommendations', 'Implications for research/policy', 'Policy implications']
    
    # Additional chapters often found in scientific papers:    
    imrdAdditions = ['Abbreviations', 'Addendum', 'Data availability', 'Background', 'List of Symbols and Abbreviations', 'List of abbreviations:', 'Theory and Hypotheses',
                     'Consent and ethical approval', 'Ethical approval', 'Consent', 'Ethical considerations', 'Ethical statement', 'Ethics and consent', 'Ethics compliance', 'Ethics approval and consent', 'Ethics approval and consent to participate', 'Ethical issues',
                     'Summary', 'Lay summary', 'Summary and conclusion', 'Author information', 'Other published results', 'Respondents', 'Data', 'Objective', 'Supplementary material', 'Appendix', 'Software availability',
                     'Limitations', 'Strengths and limitations', 'Limitations and Future Directions', 'Lessons learned and recommendations', 'Implications for research/policy', 'Policy implications']  
    
    # Get all chapters titles per article:
    for a in root.findall('.//body/sec/title'):  
        chaptTitl.append(a.text) 
    
    for val in chaptTitl:
        if val != None :
            chapterTitles.append(val.replace("\n",""))  
    
    print("\nChapter titles: ", chapterTitles)
    
    # Get titles specific for an article:
    nonImrdNum = 0
    specificChapters = []
    
    for val in chapterTitles:
        if val not in imrdList:
            if val != None :
                nonImrdNum += 1
                specificChapters.append(val)
    
    # Check whether an article strictly follows the IMRaD format:      
    strictImrdNum = 0
    for val in chapterTitles:
        if val in strictImrdlist:
            strictImrdNum += 1
    if strictImrdNum >= 4:
        isImrd =  True

    # Get the number of additional chapters: 
    imrdAddNum = 0
    for val in chapterTitles:
        if val in imrdAdditions:
            imrdAddNum += 1
    
    # Create a pandas DataFrame containing IMRad structure information: 
    chapters_df = pd.DataFrame({'doi': [current_doi],
                                'IMRD': [isImrd],
                                'NumAddChapters': [imrdAddNum],
                                'NumSpecChapters': [nonImrdNum]})
    print("\nChapters table:\n", chapters_df)                       

    return(chapters_df)    