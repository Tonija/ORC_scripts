# ORC data base
#os.chdir("..")

orc_med_doi = []
for i in range(1,97):
    med_results = requests.get("https://openresearchcentral.org/browse/articles?websiteId=&term0=Medicine_and_health_sciences&articleTypes=RESEARCH_ARTICLE&show=20&page="+format(i))
    src = med_results.content
    soup = bs4.BeautifulSoup(med_results.content, "html.parser")
    divs = soup.findAll("article", {"class": "c-browse__item c-article u-mb--3"})
    for div in divs:
        orc_med_doi.append(div.attrs['data-doi'])

orc_soc_doi = []
for i in range(1,25):
    soc_results = requests.get("https://openresearchcentral.org/browse/articles?websiteId=&term0=Social_sciences&articleTypes=RESEARCH_ARTICLE&show=20&page="+format(i))
    src = soc_results.content
    soup = bs4.BeautifulSoup(soc_results.content, "html.parser")
    divs = soup.findAll("article", {"class": "c-browse__item c-article u-mb--3"})
    for div in divs:
        orc_soc_doi.append(div.attrs['data-doi'])

print(len(orc_med_doi))
print(len(orc_soc_doi))

with open('orc_med_doi.csv', 'w') as f:
    for i in range (0,len(orc_med_doi)):
        f.write(orc_med_doi[i])
        f.write('\n')
        
with open('orc_soc_doi.csv', 'w') as f:
    for i in range (0,len(orc_soc_doi)):
        f.write(orc_soc_doi[i])
        f.write('\n') 
        
orc_bio_doi = []
for i in range(1,89):
    bio_results = requests.get("https://openresearchcentral.org/browse/articles?websiteId=&term0=Biology_and_life_sciences&articleTypes=RESEARCH_ARTICLE&show=20&page="+format(i))
    src = bio_results.content
    soup = bs4.BeautifulSoup(bio_results.content, "html.parser")
    divs = soup.findAll("article", {"class": "c-browse__item c-article u-mb--3"})
    for div in divs:
        orc_bio_doi.append(div.attrs['data-doi'])

orc_comp_doi = []
for i in range(1,12):
    comp_results = requests.get("https://openresearchcentral.org/browse/articles?websiteId=&term0=Computer_and_information_sciences&articleTypes=RESEARCH_ARTICLE&show=20&page="+format(i))
    src = comp_results.content
    soup = bs4.BeautifulSoup(comp_results.content, "html.parser")
    divs = soup.findAll("article", {"class": "c-browse__item c-article u-mb--3"})
    for div in divs:
        orc_comp_doi.append(div.attrs['data-doi'])
        
orc_earth_doi = []
for i in range(1,9):
    earth_results = requests.get("https://openresearchcentral.org/browse/articles?websiteId=&term0=Earth_sciences&articleTypes=RESEARCH_ARTICLE&show=20&page="+format(i))
    src = earth_results.content
    soup = bs4.BeautifulSoup(earth_results.content, "html.parser")
    divs = soup.findAll("article", {"class": "c-browse__item c-article u-mb--3"})
    for div in divs:
        orc_earth_doi.append(div.attrs['data-doi'])        

print(len(orc_bio_doi))
print(len(orc_comp_doi))
print(len(orc_earth_doi))

with open('orc_bio_doi.csv', 'w') as f:
    for i in range (0,len(orc_bio_doi)):
        f.write(orc_bio_doi[i])
        f.write('\n')
        
with open('orc_comp_doi.csv', 'w') as f:
    for i in range (0,len(orc_comp_doi)):
        f.write(orc_comp_doi[i])
        f.write('\n')
        
with open('orc_earth_doi.csv', 'w') as f:
    for i in range (0,len(orc_earth_doi)):
        f.write(orc_earth_doi[i])
        f.write('\n') 

orc_eco_doi = []
for i in range(1,6):
    eco_results = requests.get("https://openresearchcentral.org/browse/articles?websiteId=&term0=Ecology_and_environmental_sciences&articleTypes=RESEARCH_ARTICLE&show=20&page="+format(i))
    src = eco_results.content
    soup = bs4.BeautifulSoup(eco_results.content, "html.parser")
    divs = soup.findAll("article", {"class": "c-browse__item c-article u-mb--3"})
    for div in divs:
        orc_eco_doi.append(div.attrs['data-doi'])

orc_eng_doi = []
for i in range(1,10):
    eng_results = requests.get("https://openresearchcentral.org/browse/articles?websiteId=&term0=Engineering_and_technology&articleTypes=RESEARCH_ARTICLE&show=20&page="+format(i))
    src = eng_results.content
    soup = bs4.BeautifulSoup(eng_results.content, "html.parser")
    divs = soup.findAll("article", {"class": "c-browse__item c-article u-mb--3"})
    for div in divs:
        orc_eng_doi.append(div.attrs['data-doi'])
        
orc_peo_doi = []
for i in range(1,43):
    peo_results = requests.get("https://openresearchcentral.org/browse/articles?websiteId=&term0=People_and_places&articleTypes=RESEARCH_ARTICLE&show=20&page="+format(i))
    src = peo_results.content
    soup = bs4.BeautifulSoup(peo_results.content, "html.parser")
    divs = soup.findAll("article", {"class": "c-browse__item c-article u-mb--3"})
    for div in divs:
        orc_peo_doi.append(div.attrs['data-doi'])        

print(len(orc_eco_doi))
print(len(orc_eng_doi))
print(len(orc_peo_doi))

with open('orc_eco_doi.csv', 'w') as f:
    for i in range (0,len(orc_eco_doi)):
        f.write(orc_eco_doi[i])
        f.write('\n')
        
with open('orc_eng_doi.csv', 'w') as f:
    for i in range (0,len(orc_eng_doi)):
        f.write(orc_eng_doi[i])
        f.write('\n')
        
with open('orc_peo_doi.csv', 'w') as f:
    for i in range (0,len(orc_peo_doi)):
        f.write(orc_peo_doi[i])
        f.write('\n') 

orc_phy_doi = []
for i in range(1,30):
    phy_results = requests.get("https://openresearchcentral.org/browse/articles?websiteId=&term0=Physical_sciences&articleTypes=RESEARCH_ARTICLE&show=20&page="+format(i))
    src = phy_results.content
    soup = bs4.BeautifulSoup(phy_results.content, "html.parser")
    divs = soup.findAll("article", {"class": "c-browse__item c-article u-mb--3"})
    for div in divs:
        orc_phy_doi.append(div.attrs['data-doi'])

orc_res_doi = []
for i in range(50):
    res_results = requests.get("https://openresearchcentral.org/browse/articles?websiteId=&term0=Research_and_analysis_methods&articleTypes=RESEARCH_ARTICLE&show=20&page="+format(i))
    src = res_results.content
    soup = bs4.BeautifulSoup(res_results.content, "html.parser")
    divs = soup.findAll("article", {"class": "c-browse__item c-article u-mb--3"})
    for div in divs:
        orc_res_doi.append(div.attrs['data-doi'])
        
orc_sci_doi = []
for i in range(1,4):
    sci_results = requests.get("https://openresearchcentral.org/browse/articles?websiteId=&term0=Science_policy&articleTypes=RESEARCH_ARTICLE&show=20&page="+format(i))
    src = sci_results.content
    soup = bs4.BeautifulSoup(sci_results.content, "html.parser")
    divs = soup.findAll("article", {"class": "c-browse__item c-article u-mb--3"})
    for div in divs:
        orc_sci_doi.append(div.attrs['data-doi'])        

print(len(orc_phy_doi))
print(len(orc_res_doi))
print(len(orc_sci_doi))

with open('orc_phy_doi.csv', 'w') as f:
    for i in range (0,len(orc_phy_doi)):
        f.write(orc_phy_doi[i])
        f.write('\n')
        
with open('orc_res_doi.csv', 'w') as f:
    for i in range (0,len(orc_res_doi)):
        f.write(orc_res_doi[i])
        f.write('\n')
        
with open('orc_sci_doi.csv', 'w') as f:
    for i in range (0,len(orc_sci_doi)):
        f.write(orc_sci_doi[i])
        f.write('\n') 

f.close()        