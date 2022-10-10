# from xml.etree.ElementTree import fromstring 
from lxml import html
from bs4 import BeautifulSoup
import requests
import pandas as pd
# payload={
#     'groupe':'244'
# }
# req=requests.get('https://www.nticrabat.com/emploi/emp.php',params=payload)
# # print(req.url)
# soup=BeautifulSoup(req.content,'html.parser')

  
URL = "https://www.nticrabat.com/emploi/emp.php?groupe=244"
r = requests.get(URL)







  

def getData():
    soup = BeautifulSoup(r.content, 'html5lib') 
    table = BeautifulSoup(str(soup.find_all('table')[-1]), 'html5lib')



    arrNames=[]
    tr = table.find_all("tr")[2:]
    for row in tr:
        
    
        for td in row.find_all('td')[1:]:
            val = td.find_all('a')
            # print(val.text)
            if val:
                tdA=[]
                for i in val:
                    
                    tdA.append(i.text)
                tdSplit=','.join(tdA)
                # tdA.append(tdSplit)
                arrNames.append(tdSplit)

            else:
                arrNames.append('')
            
    print(arrNames)

    arrColors=[]
    trC= table.find_all("tr")[2:]
    for rowC in trC:
        for td in rowC.find_all('td')[1:]:
            valC = td['bgcolor']
            if valC:
                arrColors.append(valC)
    print(arrColors)   

    finaleArr=[]
    for i in range(0,len(arrNames)):
        for j in range(0,len(arrColors)):
            if(i==j):
                finaleArr.append([arrNames[i],arrColors[j]])
    print('********************************')
    print(finaleArr)



getData()