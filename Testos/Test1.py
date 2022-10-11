import urllib.request, json 
with urllib.request.urlopen("https://www.nticrabat.com/emploi/emp.php?groupe=244") as url:
    data = json.load(url)
    print(data)