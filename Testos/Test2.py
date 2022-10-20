from lxml import html
from bs4 import BeautifulSoup
import requests
import numpy as np
import json
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
    daysTable=["lundi","mardi","mercredi","jeudi","vendredi","samedi"]
    h=0
    arrNames=[]
    arrColors=[]
    dicts={}
    tr = table.find_all("tr")[2:]
    for row in tr:
        rr=[]
        rrr=[]
        for td in row.find_all('td')[1:]:
            val = td.find('a')
            valC=td['bgcolor']
            if val:
                rr.append([val.text,valC])
            else:
                rr.append(['',valC])
       

    #     for i in rr:
    #         for j in daysTable:
    #             dicts[f'dev{h}']={
    #             f'{j}':{
    #                 f"":i
    #             }}
    #             h+=1
    #     # print(dicts)
    # print(json.dumps(dicts))

            


            

        # arrNames.append(rr)
    # print(arrNames)

    # arrColors=[]
    # trC= table.find_all("tr")[2:]
    # for rowC in trC:
    #     rrr=[]
    #     for td in rowC.find_all('td')[1:]:
    #         valC = td['bgcolor']
    #         if valC:
    #             rrr.append(valC)
    #     arrColors.append(rrr)
    # print(arrColors)   
    finalArr=[]
    # for i in range(0,len(arrNames)):
    #     for j in range(0,len(arrColors)):
    #         if(i==j):
    #             finalArr.append([arrNames[i],arrColors[j]])
    # # print('********************************')
    # print(finaleArr)
    # print(len(arrNames),len(arrColors))

        # for j in  range(0,len(arrColors)):
                # finalArr.append([arrNames[i][i],arrColors[i][i]])




    # print(len(arrColors),len(arrNames))
    # for i in range(0,len(arrNames)):
    #     for j in range(0,len(arrNames[i])):
    #         for k in range(0,len(arrColors)):
    #             for q in range(0,len(arrColors[k])):
    #                 if(q==j and i==k):
    #                     finalArr.append([arrNames[i][j],arrColors[k][q]])
    # print(len(finalArr))

# def checkChanges(arr):
#     bool=True
#     wf=open("data.txt","r+")
#     lines=wf.readlines()
#     oldOne=[]
#     for i in range(0,len(lines)):
#         # print(lines[i].rstrip().split(','),'*')
#         oldOne.append(lines[i].rstrip().split(','))
#     # print(oldOne)

#     npoldOne=np.array(oldOne)
#     npnewOne=np.array(arr)

#     if(np.array_equal(npoldOne,npnewOne)==False or len(npnewOne)!=len(npoldOne)):
#         bool=False
#     print(bool)
#     wf.close()

#     if(bool==False):
#         rf=open("data.txt",'w+')
#         for i in npnewOne:
#             # print(i)
#             joinArr=",".join(i)
#             rf.writelines(f'{joinArr}\n')
#         rf.close()
        
#     return bool


getData()
# print(checkChanges(arr))
