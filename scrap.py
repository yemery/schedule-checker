from lxml import html
from bs4 import BeautifulSoup
import requests
import numpy as np

import schedule
from discord_webhook import DiscordWebhook
payload={
    'groupe':'244'
}
URL = "https://www.nticrabat.com/emploi/emp.php"
r = requests.get(URL,params=payload)


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
                tdSplit=' '.join(tdA)
                # tdA.append(tdSplit)
                arrNames.append(tdSplit)

            else:
                arrNames.append('')
    # print(arrNames)

    arrColors=[]
    trC= table.find_all("tr")[2:]
    for rowC in trC:
        for td in rowC.find_all('td')[1:]:
            valC = td['bgcolor']
            if valC:
                arrColors.append(valC)
    # print(arrColors)   
    finalArr=[]
    for i in range(0,len(arrNames)):
        for j in range(0,len(arrColors)):
            if(i==j):
                finalArr.append([arrNames[i],arrColors[j]])
    # print('********************************')
    # print(finaleArr)
    return finalArr




def checkChanges(arr):
    bool=True
    wf=open("data.txt","r+")
    lines=wf.readlines()
    oldOne=[]
    for i in range(0,len(lines)):
        # print(lines[i].rstrip().split(','),'*')
        oldOne.append(lines[i].rstrip().split(','))
    # print(oldOne)

    npoldOne=np.array(oldOne)
    npnewOne=np.array(arr)

    if(np.array_equal(npoldOne,npnewOne)==False or len(npnewOne)!=len(npoldOne)):
        bool=False
    print(bool)
    wf.close()

    if(bool==False):
        rf=open("data.txt",'w+')
        for i in npnewOne:
            # print(i)
            joinArr=",".join(i)
            rf.writelines(f'{joinArr}\n')
        rf.close()
        
    return bool


# arr=getData()
# print(checkChanges(arr))

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1028634412218331186/_gvhAXlOjgHCg7eTDzQI1fBNurWIOrn7bgnJiLxZCFqPn4Oy8UXnXuYpM_7i_K-A4r_m', content='schedule has been changed')
def main():
    arr=getData()
    
    if(checkChanges(arr)==False):
        response = webhook.execute()
schedule.every(5).seconds.do(main)
while True:
    schedule.run_pending()
