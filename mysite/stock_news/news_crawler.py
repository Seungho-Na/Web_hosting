from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class CrawlObj():

    def crawl_news(self):
        urlsAndtext = []
        display = Display(visible=0, size=(1024, 768))
        display.start()

        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        path = '/home/immasaru/Web_hosting/mysite/stock_news/geckodriver'
        binary = FirefoxBinary('/usr/local/bin/firefox')
        driver = webdriver.Firefox(firefox_binary=binary, capabilities=cap, executable_path=path)
        print(driver.title)

        driver.get('http://www.google.com/')
        element = driver.find_element_by_name('q')
        element.send_keys("주식")
        element.submit()

        selectPage = 2
        index = 0

        driver.find_element_by_link_text("News").click()
        driver.find_element_by_xpath("//div[@id='hdtb-tls']").click()
        time.sleep(1)
        driver.find_element_by_tag_name("g-popup").click()
        time.sleep(1)
        driver.find_element_by_link_text("Past 24 hours").click()

        links = driver.find_elements_by_tag_name('a')
        for link in links:
            style = link.get_attribute("style")
            href = str(link.get_attribute('href'))
            link_text = link.text
            if style == "text-decoration: none; display: block;" and href[:4] == "http":
                print((href, link_text))

        driver.close()
        display.stop()

        '''
        #print(driver.find_elements_by_class_name("fl")[index].get_attribute("aria-label"))
        #print("Page %s" % selectPage)
        #print(driver.find_elements_by_class_name("fl")[index].get_attribute("aria-label") == "Page %s" % selectPage)

        #무조건 끝에 가면 에러남
        try:
            while(driver.find_elements_by_class_name("fl")[index].get_attribute("aria-label") == "Page %s" % selectPage):

                links = driver.find_elements_by_tag_name('a')
                for link in links:
                    style = link.get_attribute("style")
                    href = str(link.get_attribute('href'))
                    link_text = link.text
                    if style == "text-decoration: none; display: block;" and href[:4] == "http":
                        urlsAndtext.append((href, link_text))

                driver.find_elements_by_class_name("fl")[index].click()
                selectPage += 1
                if selectPage <= 12:
                    index = selectPage - 2
                else:
                    index = 10
        except:
            driver.close()
            display.stop()
        return urlsAndtext
        '''

uat = CrawlObj().crawl_news()
print(len(uat))
print(uat)

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









