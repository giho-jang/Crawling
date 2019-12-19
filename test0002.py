import bs4
html_str = """
<html>
    <body>
        <ul class="great">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

ul = bs_obj.find("ul")
# ul = bs_obj.find("ul", {"class":"reply"}) # bs_obj 안에있는 ul에서 class(reply)를 불러옴
print(ul)
print(ul.text)
print()

li = ul.find("li")
print(li)
print(li.text)
print()

lis = ul.findAll("li")  # li 데이터가 여러개가 아닌 하나인경우 [] 제외하고 출력
print(lis)
print(lis[2])   # 0 ~ ? 까지 원하는 라인의 값을 출력
print(lis[2].text)
print()

