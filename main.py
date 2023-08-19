import web_site
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
web = web_site.Web_site(driver)
web.open_website()
