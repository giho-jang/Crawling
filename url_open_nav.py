import urllib.request
import bs4

url = "https://www.naver.com"
html = urllib.request.urlopen(url) # 데이터를 받아옴

bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("ul", {"class":"an_l"})
lis = ul.findAll("li")

for li in lis:
    a_tag = li.find("a")
    span = a_tag.find("span", {"class":"an_txt"})
    print(span.text)
