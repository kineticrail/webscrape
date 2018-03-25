from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

nameList = bsObj.findAll("span", {"class":"green"})

for name in nameList:

	#현재 문서에서 모든 태그를 제거하고 텍스트만 들어있는 문자열을 반환
	print(name.get_text())

	#해당 문서의 태그를 제거하지 않고 해당 태드를 반환
	#print(name)

