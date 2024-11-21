from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import requests
import time

def easy_question():
    
    driver = webdriver.Chrome()

    driver.get("https://www.codewars.com/kata/search/python?q=&tags=Debugging&beta=false&order_by=sort_date%20desc")
    time.sleep(5)

    question = driver.find_elements(By.CLASS_NAME, 'ml-2')
    all_links = []
    for element in question:
        all_links.append(element.get_attribute("href"))

    link = all_links[random.randint(0,len(all_links))]
    driver.get(link)  
    time.sleep(5)

    description = driver.find_element(By.ID, "description").text
    driver.quit()
    return description
