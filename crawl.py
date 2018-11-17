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

profile_links=[]

global count


def scrape_posts():
	# print(profile_links)
	c=0
	for i in profile_links:
		c=c+1
		# print(c)
		driver.get(i)
		image=driver.find_element_by_css_selector('img.FFVAD')
		post["imageURL"]=image.get_attribute("src")
		try:
			temp=driver.find_element_by_css_selector("div.C4VMK span")
			user_found=driver.find_element_by_css_selector("h2._6lAjh")
			# print("comment by : " + user_found)
			# if(user_found.text==user):
			post["caption"]=temp.text
			# post["caption"]=""
		except Exception as e:
			# print("exception : "+e)
			post["caption"]=""
		post["comments"]=len(driver.find_elements_by_css_selector("h3._6lAjh"))
		date=driver.find_element_by_css_selector("time.Nzb55").get_attribute("datetime")
		date=date[::-1]
		date=date[5:]
		date=date[::-1]
		date=date.replace("T","")
		time=date[10:]
		date=date[0:10]
		print(date+"\t"+time)
		print("\n\n"+str(c)+"\nimg url : "+post["imageURL"]+"\ncomments : "+str(post["comments"])+"\n"+"caption : "+post["caption"])


def get_url():
	while(True):
		try:
			profile_links.append(driver.current_url)
			dialog = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.vCf6V article")))
			next_button = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.coreSpriteRightPaginationArrow")))
			next_button.click()
		except Exception as e:
			# print("exception : "+str(e))
			print("done crawling till the end. count = "+str(len(profile_links)))
			break
	# print("will export the scraped data")
	# input()
	scrape_posts()
	# driver.close()

get_url()