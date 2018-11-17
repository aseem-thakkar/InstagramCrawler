from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
user="aseem.thakkar"
# print("enter the Instagram user id of profile to crawl: ")
# user=input()
driver.get("https://www.instagram.com/"+user)
assert user in driver.title
first_post = driver.find_element_by_css_selector('div.eLAPa')
first_post.click()
# driver.implicitly_wait(2) # seconds
global dialog
try:
	dialog = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.vCf6V article")))
except:
	print("locha in article finding\nAb kuch nai ho sakta. so quitting")
	driver.close()

post={
	"index":"",
	"imageURL":"",
	"caption":"",
	"likes":"",
	"comments":"",
	"dateTimeStamp":""
}

count=0



while(count!=3):
	try:
		print(driver.current_url)
		# dialog = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.vCf6V article")))
		# dialog = WebDriverWait(driver, 4).until(EC.staleness_of((By.CSS_SELECTOR, "div.vCf6V article")))
		# scraping data from within the article
		dialog=driver.find_element_by_css_selector('div.vCf6V article')
		print("dialog : "+str(dialog))
		image=driver.find_element_by_css_selector('img.FFVAD')
		post["imageURL"]=image.get_attribute("src")
		try:
			post["caption"]=image.get_attribute("alt")
		except Exception as e:
			print("exception : "+e)
			post["caption"]=""
		print("src = "+post["imageURL"]+"\n"+"caption = "+post["caption"])


		#done crawling 
		next_button=driver.find_element_by_css_selector('a.coreSpriteRightPaginationArrow')
		# next_button = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.coreSpriteRightPaginationArrow")))
		next_button.click()
		count=count+1
		driver.implicitly_wait(2) # seconds
	except Exception as e:
		print("exception : "+str(e))
		count=count - 1
		print("done crawling till the end. count = "+str(count))
		break


print("will export the scraped data")
# driver.close()