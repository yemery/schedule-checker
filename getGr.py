from bs4 import BeautifulSoup
import requests
# payload={

# }
URL = "https://www.nticrabat.com/"
r = requests.get(URL)
soup=BeautifulSoup(r.content,'html5lib')
# print(soup.prettify())
select= BeautifulSoup(str(soup.find('select', { "id" : "coursera-front-search-banner-input" })), 'html5lib')
# print(select)
payload={
    "groupe":""

}
grList=[]
for i in select.find_all('option')[1:]:
    att=i.attrs
    grList.append(att['value'])
    payload['groupe']="{}".format(att['value'])
    print(payload)

# print(grList)
# print( payload)
    

