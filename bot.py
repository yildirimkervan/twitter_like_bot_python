from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import chromedriver_binary
from selenium.common.exceptions import WebDriverException

class Twitterrobo:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.robo = webdriver.Chrome(executable_path=r'C:\PATH TO CHROME DRIVER\chromedriver_win32\chromedriver.exe')

	def login(self):
		robo = self.robo
		robo.get('https://twitter.com')
		time.sleep(3)
		email = robo.find_element_by_class_name('email-input')
		password = robo.find_element_by_name('session[password]')
		email.clear()
		password.clear()
		email.send_keys(self.username)
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		time.sleep(2)

	def Tweet_like(self,hashtag):
		robo = self.robo
		robo.get("https://twitter.com/search?q="+hashtag+"&src=typd")
		time.sleep(3)
		for y in range(0,10000):
			div = robo.find_elements_by_xpath('//div[@data-testid="like"]/div[@dir="ltr"]/div[@class="css-1dbjc4n r-xoduu5"]/*[name()="svg"]')
			if not div:
				robo.execute_script('window.scrollTo(0,document.body.scrollHeight)')
				print("scrolled down")
				time.sleep(10)
			else:
				div = robo.find_elements_by_xpath('//div[@data-testid="like"]/div[@dir="ltr"]/div[@class="css-1dbjc4n r-xoduu5"]/*[name()="svg"]')
				print("liking data step 1")
				ls = len(div)
				for i in range(0,ls):
					time.sleep(10)
					if i < ls:
						print(i)
						print(ls)
						print("liking data step 2")
						try:
						    div[i].click()
						except WebDriverException:
						    print("Element is not clickable")
						    continue
						time.sleep(10)
					else:
						print(i)
						print(ls)
						print("liking data step 3")
						time.sleep(10)
						robo.execute_script('window.scrollTo(0,document.body.scrollHeight)')

yk = Twitterrobo('yourusername','yourpassword')
yk.login()
yk.Tweet_like("jquery")
