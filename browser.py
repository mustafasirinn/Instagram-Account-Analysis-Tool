from selenium import webdriver
import time
import user_infos as usi

class Browser:
	def __init__(self,link):
		self.link = link
		self.browser = webdriver.Chrome()
		Browser.instagramWeb(self)

	def instagramWeb(self):
		self.browser.get(self.link)
		time.sleep(3)
		Browser.login(self)
		Browser.getFollowers(self)

	def login(self):
		username = self.browser.find_element_by_name("username")
		password = self.browser.find_element_by_name("password")
		username.send_keys(usi.username)
		password.send_keys(usi.password)

		loginBtn = self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3)")
		loginBtn.click()
		time.sleep(5)

		self.browser.get(self.link+"/"+usi.username)
		time.sleep(4)

	def getFollowers(self):
		self.browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a").click()
		time.sleep(4)

		Browser.scrollDown(self)

		takipciler = self.browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
		sayac = 0
		for takipci in takipciler:
			sayac += 1
			print(str(sayac) + " --> " +takipci.text)

	def scrollDown(self):
		jsKomut = """
		sayfa = document.querySelector(".isgrP");
		sayfa.scrollTo(0,sayfa.scrollHeight);
		var sayfaSonu = sayfa.scrollHeight;
		return sayfaSonu;
		"""
		sayfaSonu = self.browser.execute_script(jsKomut)
		while True:
			son = sayfaSonu 
			time.sleep(1)
			sayfaSonu = self.browser.execute_script(jsKomut)
			if son == sayfaSonu:
				break