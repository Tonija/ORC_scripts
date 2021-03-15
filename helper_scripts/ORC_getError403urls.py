import os
import csv
import urllib
from urllib.request import urlopen

os.chdir("C:\\Users\\Korisnik\\Desktop\\Welcome_script")
xml_urls = []
HTTP_403 = []

with open('filtered_xml_urls.csv', 'r') as xml_f:
    reader = csv.reader(xml_f)
    for row in reader:
        xml_urls.append((" ".join(row)))
            
    # xml_urls contains only last versions of artcles, add older versions as well:
    for x in xml_urls:
        if x.endswith('2'):
            xml_urls.append(x[:-1] + str(1))
        if x.endswith('3'):
            xml_urls.append(x[:-1] + str(2))  
        if x.endswith('4'):
            xml_urls.append(x[:-1] + str(3))

for i in range(len(xml_urls)):
    try:
        with urlopen(xml_urls[i]) as f:
            print("\nPassed")
    except:
        print("\nCould not open file: ", xml_urls[i])
        HTTP_403.append(xml_urls[i])
            
with open('HTTP_403_test.txt', 'w') as http_f: #rename later (remove _test)
    for item in HTTP_403:
        http_f.write("%s\n" % item)

# Go to HTTP_403.txt file and download files manually
# Save the files into new folder HTTP_403 
# Folder HTTP_403 needs to be in the same directory as ORC_main.py script	