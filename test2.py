from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://search.jd.com/Search?keyword=%E4%B9%A6%E5%8C%85&enc=utf-8&wq=%E4%B9%A6%E5%8C%85&pvid=30bc0d46228548339836694fe115b208")
# html = driver.page_source
items = driver.find_elements_by_xpath("//div[@id='J_goodsList']//li[@class='gl-item']")
print(items)
print("商品名称                              好评率")
for item in items:
    name = item.find_element_by_xpath(".//div[@class='p-name p-name-type-2']//em").text #.replace('\n', '').replace('\r', '')
    comment_url = item.find_element_by_xpath(".//div[@class='p-commit']//a").get_attribute("href")
    driver1 = webdriver.Chrome(chrome_options=chrome_options)
    driver1.get(comment_url)
    comment = driver1.find_element_by_xpath("//div[@class='percent-con']").text
    driver1.quit()
    print("{:<15}{:^30}".format(name, comment))
# time.sleep(4)

driver.quit()