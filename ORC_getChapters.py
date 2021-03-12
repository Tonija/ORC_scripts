import string
import pandas as pd

def countImrdWords (root):
# Count the word number of each IMRAD section
  
    brackets = '''()[]{}<>''' # remove?
    
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
    # Remove 
    abstr_str = abstr_str.replace("\n","");
    for ele in abstr_str:  
        if ele in brackets:  
            abstr_str = abstr_str.replace(ele, " ") 
    # Split string into words:    
    abstract = abstr_str.split()
    
    # Remove comma if it appears as separated list element
    # so to avoid counting it as a word:
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
    for a in root.findall('.//sec[@sec-type="intro"]/sec/title'):
        intro.append(a.text)
        intro.append(a.tail)    
    for a in root.findall('.//sec[@sec-type="intro"]/sec/p'):
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
    for a in root.findall('.//sec[@sec-type="intro"]/p/xref'):
        intro.append(a.text)
        intro.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="intro"]/p/xref/'):
        if a.text not in intro:
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
    for a in root.findall('.//sec[@sec-type="methods"]/sec/list[@list-type="bullet"]/list-item/p'):
        met.append(a.text)
        met.append(a.tail)     
    for a in root.findall('.//sec[@sec-type="methods"]/sec/list[@list-type="bullet"]/list-item/p/italic'):
        met.append(a.text)
        met.append(a.tail)
    for a in root.findall('.//sec[@sec-type="methods"]/sec/p/xref'):
        met.append(a.text)
        met.append(a.tail)   
    for a in root.findall('.//sec[@sec-type="methods"]/sec/p/xref/'):
        if a.text not in met:
            met.append(a.text)
        if a.tail not in met:
            met.append(a.tail)    
    for a in root.findall('.//sec[@sec-type="methods"]/p/xref'):
        met.append(a.text)
        met.append(a.tail)   
    for a in root.findall('.//sec[@sec-type="methods"]/p/xref/'):
        if a.text not in met:
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
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/title'):
            met.append(a.text)
            met.append(a.tail)
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/p'):
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
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/list[@list-type="bullet"]/list-item/p'):
            met.append(a.text)
            met.append(a.tail)     
        for a in root.findall('.//sec[@sec-type="materials | methods"]/sec/list[@list-type="bullet"]/list-item/p/italic'):
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
        for a in root.findall('.//sec[@sec-type="materials | methods"]/p/xref'):
            met.append(a.text)
            met.append(a.tail)   
        for a in root.findall('.//sec[@sec-type="materials | methods"]/p/xref/'):
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
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/sec/list[@list-type="bullet"]/list-item/p'):
                met.append(a.text)
                met.append(a.tail)     
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/sec/list[@list-type="bullet"]/list-item/p/italic'):
                met.append(a.text)
                met.append(a.tail)
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/sec/p/xref'):
                met.append(a.text)
                met.append(a.tail)   
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/sec/p/xref/'):
                if a.text not in met:
                    met.append(a.text)
                if a.tail not in met:
                    met.append(a.tail)   
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/p/xref'):
                met.append(a.text)
                met.append(a.tail)   
            for a in root.findall('.//sec[@sec-type="subjects | methods"]/p/xref/'):
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
    for a in root.findall('.//sec[@sec-type="results"]/list[@list-type="bullet"]/list-item/p'):
        res.append(a.text)
        res.append(a.tail)     
    for a in root.findall('.//sec[@sec-type="results"]/list[@list-type="bullet"]/list-item/p/italic'):
        res.append(a.text)
        res.append(a.tail)     
    for a in root.findall('.//sec[@sec-type="results"]/p/italic'):
        res.append(a.text)
        res.append(a.tail)
    for a in root.findall('.//sec[@sec-type="results"]/p/bold'):
        res.append(a.text)
        res.append(a.tail)    
    for a in root.findall('.//sec[@sec-type="results"]/sec/p/xref'):
        res.append(a.text)
        res.append(a.tail)   
    for a in root.findall('.//sec[@sec-type="results"]/sec/p/xref/'):
        if a.text not in res:      
            res.append(a.text)
        if a.tail not in res:    
            res.append(a.tail)     
    for a in root.findall('.//sec[@sec-type="results"]/p/xref'):
        res.append(a.text)
        res.append(a.tail)   
    for a in root.findall('.//sec[@sec-type="results"]/p/xref/'):
        if a.text not in res:      
            res.append(a.text)
        if a.tail not in res:    
            res.append(a.tail)   
    for a in root.findall('.//sec[@sec-type="results"]/sec/title'):
        res.append(a.text)
        res.append(a.tail)
    for a in root.findall('.//sec[@sec-type="results"]/sec/p'):
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
    for a in root.findall('.//sec[@sec-type="results"]/sec/list[@list-type="bullet"]/list-item/p'):
        res.append(a.text)
        res.append(a.tail)     
    for a in root.findall('.//sec[@sec-type="results"]/sec/list[@list-type="bullet"]/list-item/p/italic'):
        res.append(a.text)
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
    for a in root.findall('.//sec[@sec-type="discussion"]/p/xref'):
        discuss.append(a.text)
        discuss.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="discussion"]/p/xref/'):
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
    #for a in root.findall('.//sec[@sec-type="discussion"]/sec/p/sup'):
     #   discuss.append(a.tail)
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
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/sec/title'):
            discuss.append(a.text) 
            discuss.append(a.tail)    
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/sec/p'):
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
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/p/xref'):
            discuss.append(a.text)
            discuss.append(a.tail) 
        for a in root.findall('.//sec[@sec-type="discussion | conclusions"]/p/xref/'):
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
    for a in root.findall('.//sec[@sec-type="conclusions"]/p/italic'):
        concl.append(a.text)
        concl.append(a.tail) 
    for a in root.findall('.//sec[@sec-type="conclusions"]/p/bold'):
        concl.append(a.text)
        concl.append(a.tail)        
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
    for a in root.findall('.//sec[@sec-type="conclusions"]/p/xref'):
        concl.append(a.text)
        concl.append(a.tail)  
    for a in root.findall('.//sec[@sec-type="conclusions"]/p/xref/'):
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
                              
    print("\nIMRD information: \n")
    print(imrd_info)
    return(imrd_info)
    
def countAllWords (root):

    # NonIMRD chapters
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
    for a in root.findall('.//body/sec/p/sup/xref'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)   
    for a in root.findall('.//body/sec/p/sup/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
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
    for a in root.findall('.//body/sec/sec/p/sup'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)     
    for a in root.findall('.//body/sec/sec/sup'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)    
    for a in root.findall('.//body/sec/sec/sup/xref'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)
    for a in root.findall('.//body/sec/sec/p/sup/xref'):
        nonImrd.append(a.text)
        nonImrd.append(a.tail)         
    for a in root.findall('.//body/sec/sec/p/sup/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail)              
    for a in root.findall('.//body/sec/sec/p/xref/'):
        if a.text not in nonImrd:
            nonImrd.append(a.text)
        if a.tail not in nonImrd:    
            nonImrd.append(a.tail) 
    for a in root.findall('.//body/sec/sec/p/sup/ext-link'):
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
    
def getChapterTitles (root, imrdList):

    chaptTitl = []
    chapterTitles = []
    isImrd = True
    
    for a in root.findall('.//body/sec/title'):  
        chaptTitl.append(a.text) 
    
    for val in chaptTitl:
        chapterTitles.append(val.replace("\n",""))  
    
    print("\nChapter titles: ", chapterTitles)
    
    for val in chapterTitles:
        if val not in imrdList:
            isImrd = False
    print("\nIMRD format: ", isImrd) 

    return(isImrd)    