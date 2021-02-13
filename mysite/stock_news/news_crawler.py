from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class CrawlObj():


    def crawl_news_url(self):
        urls = []
        display = Display(visible=0, size=(1024, 768))
        display.start()

        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        path = '/home/immasaru/Web_hosting/mysite/stock_news/geckodriver'
        binary = FirefoxBinary('/usr/local/bin/firefox')
        driver = webdriver.Firefox(firefox_binary=binary, capabilities=cap, executable_path=path)

        driver.get('http://www.google.com/')
        print(driver.title)

        element = driver.find_element_by_name('q')
        element.send_keys("주식")
        element.submit()

        driver.find_element_by_link_text("News").click()

        links= driver.find_elements_by_tag_name('a')
        for link in links:
            style = link.get_attribute("style")
            href = str(link.get_attribute('href'))
            if style == "text-decoration: none; display: block;" and href[:4] == "http":
                urls.append(href)

        driver.close()
        display.stop()
        return urls

'''

for link in links:
    try:
        news_div= link.find_element_by_class_name('yr3B8d.KWQBje')
        print("plz say something")
        print(news_div.text)
        if news_div != None:
            href = str(link.get_attribute('href'))
            if href[:4] == "http":
                print(href)
    except:
        continue

'''









