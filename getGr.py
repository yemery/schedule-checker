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
gr=[]
def getGr():
    URL = "https://www.nticrabat.com/"
    r = requests.get(URL)
    soup=BeautifulSoup(r.content,'html5lib')
    select= BeautifulSoup(str(soup.find('select', { "id" : "coursera-front-search-banner-input" })), 'html5lib')

    grList=[]
    for i in select.find_all('option')[1:]:
        
        
        att=i.attrs
        gr.append(i.text)
        grList.append(att['value'])
        # payload['groupe']="{}".format(att['value'])
        # print(payload)
    return grList
# print(getGr())
grList=getGr()
# print(grList)
print(gr)
    

