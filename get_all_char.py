import requests
from bs4 import BeautifulSoup

def pureCNtext(url,txtname):
	r=requests.get(url) 
	r.encoding='utf-8' 
	soup=BeautifulSoup(r.text,'lxml') 
	text=soup.get_text() 
	text_nospace=text.replace('\n','').replace(' ','') 
	return text_nospace

sitemap_url = "https://www.cestlavie.moe/sitemap.xml"
xml = requests.get(sitemap_url).content
parser = BeautifulSoup(xml, "xml")
loc_tags = parser.find_all('loc')
urls = []
text = ''
for loc in loc_tags:
    url = loc.get_text()
    urls.append(url)
print(urls)
for url in urls:
    print(url)
    text = text + str(pureCNtext(url,'blog'))

with open('blog.txt','a',encoding='utf-8') as f:
    f.write(text)