# Save urls of filtered articles (for xmls and pdfs) 
import io
import string
import urllib.request

xml_url_wellcome = 'https://wellcomeopenresearch.org/extapi/article/xml?doi='
xml_url_f1000 = 'https://f1000research.com/extapi/article/xml?doi='
xml_url_gates = 'https://gatesopenresearch.org/extapi/article/xml?doi='
xml_url_mni = 'https://mniopenresearch.org/extapi/article/xml?doi='
xml_url_hrb = 'https://hrbopenresearch.org/extapi/article/xml?doi='
xml_url_aas = 'https://aasopenresearch.org/extapi/article/xml?doi='
xml_url_amrc = 'https://amrcopenresearch.org/extapi/article/xml?doi='
xml_url_em = 'https://emeraldopenresearch.com/extapi/article/xml?doi='

filtered_xml_urls = []
filtered_pdf_urls = []

# Social:
for i in range(len(orc_soc_doi_filtered)):
    try:
        with urllib.request.urlopen(xml_url_wellcome + orc_soc_doi_filtered[i]) as webFile:
            filtered_xml_urls.append(str(xml_url_wellcome) + str(orc_soc_doi_filtered[i]))
    except:
        pass
        
    try:
        with urllib.request.urlopen(xml_url_f1000 + orc_soc_doi_filtered[i]) as webFile:
            filtered_xml_urls.append(str(xml_url_f1000) + str(orc_soc_doi_filtered[i]))
    except:
        pass
        
    try:
        with urllib.request.urlopen(xml_url_gates + orc_soc_doi_filtered[i]) as webFile:
            filtered_xml_urls.append(str(xml_url_gates) + str(orc_soc_doi_filtered[i]))
    except:
        pass
        
    try:
        with urllib.request.urlopen(xml_url_mni + orc_soc_doi_filtered[i]) as webFile:
            filtered_xml_urls.append(str(xml_url_mni) + str(orc_soc_doi_filtered[i]))
    except:
        pass        

    try:
        with urllib.request.urlopen(xml_url_hrb + orc_soc_doi_filtered[i]) as webFile:
            filtered_xml_urls.append(str(xml_url_hrb) + str(orc_soc_doi_filtered[i]))
    except:
        pass        
        
    try:
        with urllib.request.urlopen(xml_url_aas + orc_soc_doi_filtered[i]) as webFile:
            filtered_xml_urls.append(str(xml_url_aas) + str(orc_soc_doi_filtered[i]))
    except:
        pass        

    try:
        with urllib.request.urlopen(xml_url_amrc + orc_soc_doi_filtered[i]) as webFile:
            filtered_xml_urls.append(str(xml_url_amrc) + str(orc_soc_doi_filtered[i]))
    except:
        pass                
        
    try:
        with urllib.request.urlopen(xml_url_em + orc_soc_doi_filtered[i]) as webFile:
            filtered_xml_urls.append(str(xml_url_em) + str(orc_soc_doi_filtered[i]))
    except:
        pass          
        
# Medical:
for i in range(len(orc_med_doi_filtered)):
    try:
        with urllib.request.urlopen(xml_url_wellcome + orc_med_doi_filtered[i]) as webFile:
            filtered_xml_urls.append(str(xml_url_wellcome) + str(orc_med_doi_filtered[i]))
    except:
        pass
        
    try:
        with urllib.request.urlopen(xml_url_f1000 + orc_med_doi_filtered[i]) as webFile:
            filtered_xml_urls.append(str(xml_url_f1000) + str(orc_med_doi_filtered[i]))
    except:
        pass
        
    try:
        with urllib.request.urlopen(xml_url_gates + orc_med_doi_filtered[i]) as webFile:
            filtered_xml_urls.append(str(xml_url_gates) + str(orc_med_doi_filtered[i]))
    except:
        pass
        
    try:
        with urllib.request.urlopen(xml_url_mni + orc_med_doi_filtered[i]) as webFile:
            filtered_xml_urls.append(str(xml_url_mni) + str(orc_med_doi_filtered[i]))
    except:
        pass        

    try:
        with urllib.request.urlopen(xml_url_hrb + orc_med_doi_filtered[i]) as webFile:
            filtered_xml_urls.append(str(xml_url_hrb) + str(orc_med_doi_filtered[i]))
    except:
        pass        
        
    try:
        with urllib.request.urlopen(xml_url_aas + orc_med_doi_filtered[i]) as webFile:
            filtered_xml_urls.append(str(xml_url_aas) + str(orc_med_doi_filtered[i]))
    except:
        pass        

    try:
        with urllib.request.urlopen(xml_url_amrc + orc_med_doi_filtered[i]) as webFile:
            filtered_xml_urls.append(str(xml_url_amrc) + str(orc_med_doi_filtered[i]))
    except:
        pass                
        
    try:
        with urllib.request.urlopen(xml_url_em + orc_med_doi_filtered[i]) as webFile:
            filtered_xml_urls.append(str(xml_url_em) + str(orc_med_doi_filtered[i]))
    except:
        pass
        
print(filtered_xml_urls)   

# Save to file:
os.chdir("C:\\Users\\Korisnik\\Desktop\\Welcome_script")
with open('filtered_xml_urls.csv', 'w') as f:
    for i in range (0,len(filtered_xml_urls)):
        f.write(filtered_xml_urls[i])
        f.write('\n')

# Get pdf urls:
for el in filtered_xml_urls:
    pdf_str = el.replace('xml?doi', 'pdf?doi' )
    filtered_pdf_urls.append(pdf_str)
    
# Save to file:
with open('filtered_pdf_urls.csv', 'w') as f:
    for i in range (0,len(filtered_pdf_urls)):
        f.write(filtered_pdf_urls[i])
        f.write('\n')
    
f.close()        