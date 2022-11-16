from lxml import html
from bs4 import BeautifulSoup
import requests
import numpy as np
import time
import schedule
from discord_webhook import DiscordWebhook
import datetime




gr=[]
def getGr():
    URL = "https://www.nticrabat.com/"
    r = requests.get(URL)
    soup=BeautifulSoup(r.content,'html5lib')
    select= BeautifulSoup(str(soup.find('select', { "id" : "coursera-front-search-banner-input" })), 'html5lib')

    grList=[]
    for i in select.find_all('option')[1:]:
        gr.append(i.text)
        att=i.attrs
        grList.append(att['value'])
    print(grList)
    return grList



def checkChanges(arr,grNum):
        bool=True
        wf=open(f"dbTxt/{gr[grNum]}.txt","r+")
        lines=wf.readlines()
        oldOne=[]
        for i in range(0,len(lines)):
            oldOne.append(lines[i].rstrip().split(','))

        npoldOne=np.array(oldOne)
        npnewOne=np.array(arr)
     

        if(np.array_equal(npoldOne,npnewOne)==False or len(npnewOne)!=len(npoldOne)):
            bool=False
        wf.close()

        if(bool==False):
            rf=open(f"dbTxt/{gr[grNum]}.txt",'w+')
            for i in npnewOne:
                joinArr=",".join(i)
                rf.writelines(f'{joinArr}\n')
            rf.close()
        
        return bool
def getData(r):
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
                    arrNames.append(tdSplit)

                else:
                    arrNames.append('')

        arrColors=[]
        trC= table.find_all("tr")[2:]
        for rowC in trC:
            for td in rowC.find_all('td')[1:]:
                valC = td['bgcolor']
                if valC:
                    arrColors.append(valC)
        finalArr=[]
        for i in range(0,len(arrNames)):
            for j in range(0,len(arrColors)):
                if(i==j):
                    finalArr.append([arrNames[i],arrColors[j]])
   
        return finalArr
def main():
    now = datetime.datetime.now()
    grNum=0
    grList=getGr()
    print(gr)

    for i in grList:
        payload={
            'groupe':f'{i}',
        }
        URL = "https://www.nticrabat.com/emploi/emp.php"
        r = requests.get(URL,params=payload)

        arr=getData(r)
        if(checkChanges(arr,grNum)==False):
            webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1028634412218331186/_gvhAXlOjgHCg7eTDzQI1fBNurWIOrn7bgnJiLxZCFqPn4Oy8UXnXuYpM_7i_K-A4r_m', content=f'schedule of <@&{1039095859452837928}>  has been changed . {now}  https://www.nticrabat.com/index.php?groupe={int(grList[grNum])}#emploi' )
            response = webhook.execute()
        grNum+=1 
   
schedule.every(5).seconds.do(main)

while 2:
    n = schedule.idle_seconds()
    if n is None:
        break
    elif n > 0:
        time.sleep(n)
    schedule.run_pending()
    