



# payload={
#     'groupe':'244'
# }
# req=requests.get('https://www.nticrabat.com/emploi/emp.php',params=payload)
# # print(req.url)
# soup=BeautifulSoup(req.content,'html.parser')
# arrNames=[]
# tr = table.find_all("tr")[2:]
# for row in tr:
#     r=[]
#     for td in row.find_all('td')[1:]:
#         val = td.find('a')
#         if val:
#             r.append(val.text)
#         else:
#             r.append('')
#     arrNames.append(r)
# # print(arrNames)

# arrColors=[]
# trC= table.find_all("tr")[2:]
# for rowC in trC:
#     rC=[]
#     for td in rowC.find_all('td')[1:]:
#         valC = td['bgcolor']
#         if valC:
#             rC.append(valC)
#     arrColors.append(rC)
# # print(arrColors)