import os
import sys
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests 


browser = webdriver.Chrome('/home/arch/myDev/chromedriver')
browser.get('https://www.mediapart.fr/login')

def authenticate():
    python_button = browser.find_element_by_xpath("//*[@id='edit-name-page']")
    python_button.send_keys('darboisantoine@gmail.com')
    python_button = browser.find_element_by_xpath("//*[@id='edit-pass-page']")
    python_button.send_keys('Jerry1994')
    # python_button = browser.find_element_by_xpath("//*[@id='logFormEl'][1]")
    python_button.submit()
    url = browser.current_url



if __name__ == '__main__':
    authenticate()


