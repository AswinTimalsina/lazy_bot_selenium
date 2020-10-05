
from selenium import webdriver
# import PyPDF2
from selenium.webdriver.common.keys import Keys #allows us to type in the text bar
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from general import *

# chrome driver path
PATH = "E:\Projects\selenium_web_bot\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# change this keyword for different searches
search_keyword = "apple"
driver.get("https://ulm.louislibraries.org/uhtbin/ezproxylogin_louis_ulm.x?url=http://search.ebscohost.com/login.aspx?direct=true&site=eds-live&scope=site&type=0&mode=and&cli0=FT1&clv0=Y&authtype=ip&bquery="+search_keyword)

# first page automated authentication
search = driver.find_element_by_name("id")
search.send_keys("30098693")

search = driver.find_element_by_name("pin")
search.send_keys("0797")
search.send_keys(Keys.RETURN)

# wait till the results are completed
try: 
    pdf = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "resultListInnerDiv"))
    )
    articles = pdf.find_elements_by_link_text("PDF Full Text")  #creates an array

    create_project_file(search_keyword)
    count = 1
    for article in articles:
        data = str(count)+'. ' + article.get_attribute("href")
        append_to_file(search_keyword+'.txt', data)
        count+=1

    
# if there is exception in scraping
except:
    print("Exception!!!! QUITTING!")
    driver.quit()

# closes the window screen after all the tasks complete
finally:
    print('QUITTING!')
    driver.quit()