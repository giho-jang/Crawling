import bs4

html_str = """
<html>
    <body>
        <ul class="ko">
            <li>
                <a href="http://www.naver.com/">네이버</a>
            </li>
        </ul>
        <ul class="sns">
            <li>
                <a href="http://www.facebook.com/">페이스북</a>
            </li>
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
atag = bs_obj.find("a")
print(atag) # a 태그줄 출력
print(atag['href']) # 주소만 출력
