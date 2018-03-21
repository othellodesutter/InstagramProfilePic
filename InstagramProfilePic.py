from selenium import webdriver
from bs4 import BeautifulSoup
import time

profile = input("Username?")
url = "https://www.instagram.com/" + profile

phantomjs_path = r" " 	#PUT HERE THE PATH WHERE PHANTOMJS IS INSTALLED
wd = webdriver.PhantomJS(phantomjs_path)
time.sleep(1)
wd.get(url)

html_page = wd.page_source
soup = BeautifulSoup(html_page, "html.parser")

pp = soup.find('img')['src']

pp = pp.replace("s150x150", "s1080x1080")
pp = pp.replace("/vp/", "/")

print(pp)

input("Press enter to exit ;)")