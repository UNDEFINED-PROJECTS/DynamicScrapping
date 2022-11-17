from autoselenium import Driver
from selenium.webdriver.common.by import *
from bs4 import BeautifulSoup
import time

navegador = "firefox"
link = 'https://aniyan.net/'
webDriver = Driver(navegador, root='drivers').driver


webDriver.get(link)
# time.sleep(2)
page:str = webDriver.page_source
webDriver.close()

# tratamento da pagina
page = page.replace('src="/', 'src="'+link).replace('href="/', 'href="'+link)
with open("page.html", "wb",) as f:
    f.write(page.encode("utf-8"))
    f.close()
