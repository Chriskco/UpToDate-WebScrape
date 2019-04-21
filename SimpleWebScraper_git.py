# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 15:45:03 2019

@author: Christopher Co
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# setting a delay and preference for chrome page loading
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"

browser = webdriver.Chrome(desired_capabilities=caps)

# browser.implicitly_wait(10)
# url = "http://www.google.com/xhtml"
url = "https://www.uptodate.com/login" #/contents/table-of-contents/general-surgery"
browser.get(url)

# browser.maximize_window()

#%%

username = browser.find_element_by_id("userName") #username form field
password = browser.find_element_by_id("password") #password form field

# input username and password - default Username and Password are used
username.send_keys("Username")
password.send_keys("Password")

# click submit
submitButton = browser.find_element_by_id("btnLoginSubmit")
submitButton.click()

#%% Get array of all specialties

browser.get("https://www.uptodate.com/contents/table-of-contents")
wait = WebDriverWait(browser, 10)
men_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='utd-main']")))

#innerHTML = browser.execute_script("return document.body.innerHTML")

TOChtml = browser.execute_script("return document.body.innerHTML")
# Test inner HTML
#print(TOChtml)

# scrape html from the page
TOC_content = BeautifulSoup(TOChtml, "html.parser")

# searching for specialties
TOC_titles = TOC_content.find_all(attrs={"data-ng-bind-html":"item.name"})
# print(TOC_titles)

# Array for titles
TOC_array = []
for c in range(len(TOC_titles)):
    if c < 5 or TOC_titles[c].text=='Drug Information' or TOC_titles[c].text=='Lab Interpretation™':
        continue 
    else:
        TOC_array.append(TOC_titles[c].text)

print(TOC_array)

#%%
# navigate to page behind login
browser.get("https://www.uptodate.com/contents/table-of-contents/general-surgery")

# wait for element to appear
# wait = WebDriverWait(browser, 10)
men_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-ng-bind-html='item.name']")))

#%%
# returns the inner HTMl as a string
innerHTML = browser.execute_script("return document.body.innerHTML")

# testing innerHTML
# print(innerHTML)
#%%

# scrape html from the page
page_content = BeautifulSoup(innerHTML, "html.parser")

# The entire page content
# print(page_content)

# searching for the topic titles with a focused search - use a dict to find attrs
titles = page_content.find_all(attrs={"data-ng-bind-html":"item.name"})

title_array = []
# find the text for titles
for t in range(len(titles)-1):
    title_array.append(titles[t].text)
        
print(title_array)    
#%%
# Delete all of the colons from the array (:)
    

# Replace all spaces with dashes (-)
    