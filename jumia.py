import requests
import re
from bs4 import BeautifulSoup




class Scraper:
	def __init__(self):
		obj=self.start()
		self.url_http=[]
		self.url_relative=[]
		abs_url,data=self.parse_obj(obj)
		for ht in abs_url:
			self.url_http.append(ht.attrs['href']) if ht.attrs['href'].startswith("http")\
			 else self.url_relative.append(ht.attrs['href'])
		print(self.url_relative)


	def start(self,url="http://jumia.com.ng"):
		if url:
			try:
				html=requests.get(url).text
				bsobj=BeautifulSoup(html,'html.parser')
			except requests.exceptions.RequestException as e:
				print(e)
		else:
			try:
				html=requests.get(url).text
				bsobj=BeautifulSoup(html,'html.parser')
			except requests.exceptions.RequestException as e:
				print(e)
		return bsobj

	def parse_obj(self,obj):
	    abs_url=obj.findAll('a',href=re.compile('^(http|https|/).'))
	    data=obj.find_all('div',{'class':re.compile("prc")})
	    return abs_url,data


jumia=Scraper()