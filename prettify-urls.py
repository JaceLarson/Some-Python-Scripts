import requests, bs4
import copy
from selenium import webdriver
import time
url = str(input("Paste url you want to prettify: "))

res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(soup.prettify)
time.sleep(5)									#time to copy html to clipboard
driver = webdriver.Chrome()
driver.get("http://htmlformatter.com/")
time.sleep(25)
driver.quit()