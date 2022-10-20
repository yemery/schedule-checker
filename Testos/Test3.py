from array import array
import json
f=open('jsonData.json','r')
data=json.load(f)
# print(data['dev1'][1])
# for i in data['dev1']:
#     print(i)
print(data['dev1'][1]['8-11'])
d={}
arr=['dev1']
arr1=[
    ['A',"B","C",'D'],
    ['A',"B","C",'D'],
    ['A',"B","C",'D'],
    ['A',"B","C",'D']
]
timeline=['8-11',"11-13","13-16",'16-18']
j=0
for i in arr:
    d[i]=[
    ]
    for k in timeline:
        d[i][j]={
            f"{k}":arr1[j]
        }
    
print(d)
