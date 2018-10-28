import json
from selenium import webdriver

driver=webdriver.Chrome()
user="aseem.thakkar"
driver.get("https://www.instagram.com/"+user)
driver.close()	