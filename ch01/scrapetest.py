from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

try:
	#html = urlopen("http://pythonscraping.com/pages/page1.html")
	html = urlopen("http://www.pythonscraping.com/pages/error.html")
except HTTPError as e :
	print(e)
	# null을 반환하거나, break 문을 실행하거, 기타 다른 방법을 사용
else:
	bsObj = BeautifulSoup(html.read(), "html.parser")
	print(bsObj.h1)