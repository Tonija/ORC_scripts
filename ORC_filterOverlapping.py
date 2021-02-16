# Chech for overlapping (whether some articles belong 
# to both Social and Medical subject area or to some other areas)
import os
import csv

#################
### VARIABLES ###
#################

orc_med_doi = []
orc_soc_doi = []
orc_bio_doi = []
orc_comp_doi = []
orc_earth_doi = []
orc_eco_doi = []
orc_eng_doi = []
orc_peo_doi = []
orc_phy_doi = []
orc_res_doi = []
orc_sci_doi = []

orc_med_doi_filtered = []
orc_soc_doi_filtered = []

os.chdir("C:\\Users\\Korisnik\\Desktop\\Welcome_script")

with open('orc_med_doi.csv', 'r') as med_f:
    reader = csv.reader(med_f)
    for row in reader:
        orc_med_doi.append((" ".join(row)))
        
with open('orc_soc_doi.csv', 'r') as soc_f:
    reader = csv.reader(soc_f)
    for row in reader:
        orc_soc_doi.append((" ".join(row)))
        
with open('orc_bio_doi.csv', 'r') as bio_f:
    reader = csv.reader(bio_f)
    for row in reader:
        orc_bio_doi.append((" ".join(row)))
        
with open('orc_comp_doi.csv', 'r') as comp_f:
    reader = csv.reader(comp_f)
    for row in reader:
        orc_comp_doi.append((" ".join(row)))
        
with open('orc_earth_doi.csv', 'r') as earth_f:
    reader = csv.reader(earth_f)
    for row in reader:
        orc_earth_doi.append((" ".join(row)))
        
with open('orc_eco_doi.csv', 'r') as eco_f:
    reader = csv.reader(eco_f)
    for row in reader:
        orc_eco_doi.append((" ".join(row)))
        
with open('orc_eng_doi.csv', 'r') as eng_f:
    reader = csv.reader(eng_f)
    for row in reader:
        orc_eng_doi.append((" ".join(row)))
        
with open('orc_peo_doi.csv', 'r') as peo_f:
    reader = csv.reader(peo_f)
    for row in reader:
        orc_peo_doi.append((" ".join(row)))
        
with open('orc_phy_doi.csv', 'r') as phy_f:
    reader = csv.reader(phy_f)
    for row in reader:
        orc_phy_doi.append((" ".join(row)))
        
with open('orc_res_doi.csv', 'r') as res_f:
    reader = csv.reader(res_f)
    for row in reader:
        orc_res_doi.append((" ".join(row)))
        
with open('orc_sci_doi.csv', 'r') as sci_f:
    reader = csv.reader(sci_f)
    for row in reader:
        orc_sci_doi.append((" ".join(row)))
 
# Check for overlapping and filter:  
for doi in orc_med_doi:
    if (doi not in orc_soc_doi and doi not in orc_comp_doi and
        doi not in orc_eng_doi and doi not in orc_earth_doi and 
        doi not in orc_phy_doi and doi not in orc_sci_doi and
        doi not in orc_eco_doi and doi not in orc_res_doi and
        doi not in orc_peo_doi):
        orc_med_doi_filtered.append(doi)
print(len(orc_med_doi_filtered))
        
for doi in orc_soc_doi:
    if (doi not in orc_med_doi and doi not in orc_bio_doi):
        orc_soc_doi_filtered.append(doi)
print(len(orc_soc_doi_filtered))

# Save filtered dois:
with open('orc_filtered_doi.csv', 'w') as f:
    for i in range (0,len(orc_med_doi_filtered)):
        f.write(orc_med_doi_filtered[i])
        f.write('\n') 
    for i in range (0,len(orc_soc_doi_filtered)):
        f.write(orc_soc_doi_filtered[i])
        f.write('\n') 
f.close() 

med_f.close()
soc_f.close() 
bio_f.close()
comp_f.close()  
earth_f.close()
eng_f.close()
peo_f.close()
phy_f.close()
res_f.close()
sci_f.close()