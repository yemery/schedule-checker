from distutils.command import check
from lxml import html
from bs4 import BeautifulSoup
import requests
import numpy as np
import time
import schedule
from discord_webhook import DiscordWebhook

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
        # payload['groupe']="{}".format(att['value'])
        # print(payload)
    return grList
# print(getGr())
# print(gr)

    # print(i)
def checkChanges(arr,grNum):
        bool=True
        wf=open(f"dbTxt/{gr[grNum]}.txt","r+")
        lines=wf.readlines()
        oldOne=[]
        for i in range(0,len(lines)):
        # print(lines[i].rstrip().split(','),'*')
            oldOne.append(lines[i].rstrip().split(','))
    # print(oldOne)

        npoldOne=np.array(oldOne)
        npnewOne=np.array(arr)
        # print(len(npnewOne))
        # print('***')
        # print(len(npnewOne))
        # print('**')

        if(np.array_equal(npoldOne,npnewOne)==False or len(npnewOne)!=len(npoldOne)):
            bool=False
        # print(bool)
        wf.close()

        if(bool==False):
            rf=open(f"dbTxt/{gr[grNum]}.txt",'w+')
            for i in npnewOne:
            # print(i)
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
# webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1028634412218331186/_gvhAXlOjgHCg7eTDzQI1fBNurWIOrn7bgnJiLxZCFqPn4Oy8UXnXuYpM_7i_K-A4r_m', content=f'schedule  has been changed')
def main():
    grNum=0
    # webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1028634412218331186/_gvhAXlOjgHCg7eTDzQI1fBNurWIOrn7bgnJiLxZCFqPn4Oy8UXnXuYpM_7i_K-A4r_m', content=f'schedule {gr[grNum]}  has been changed')
    grList=getGr()

    for i in grList:
        payload={
            'groupe':f'{i}',
        }
        URL = "https://www.nticrabat.com/emploi/emp.php"
        r = requests.get(URL,params=payload)

        arr=getData(r)
        if(checkChanges(arr,grNum)==False):
            webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1028634412218331186/_gvhAXlOjgHCg7eTDzQI1fBNurWIOrn7bgnJiLxZCFqPn4Oy8UXnXuYpM_7i_K-A4r_m', content=f'schedule {gr[grNum]}  has been changed')
            response = webhook.execute()
        grNum+=1 
   
schedule.every(5).seconds.do(main)

while 2:
    n = schedule.idle_seconds()
    if n is None:
        # no more jobs
        break
    elif n > 0:
        # sleep exactly the right amount of time
        print('****')
        time.sleep(n)
    schedule.run_pending()
    