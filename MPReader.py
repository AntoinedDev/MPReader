import os
import sys
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests 
import re
import time

browser = webdriver.Chrome('/home/arch/myDev/chromedriver')
browser.get('https://www.mediapart.fr/login')

def authenticate():
    articles_list = []
    newlist = []
    python_button = browser.find_element_by_xpath("//*[@id='edit-name-page']")
    python_button.send_keys('darboisantoine@gmail.com')
    python_button = browser.find_element_by_xpath("//*[@id='edit-pass-page']")
    python_button.send_keys('Jerry1994')
    python_button.submit()
    URL = browser.current_url
    r = requests.get(URL) 
    soup = bs(r.content, 'html5lib')
    browser.get("https://www.mediapart.fr/journal/france")     
    a = soup.find_all('h3', attrs={'class': "title"})
    articles_list.append(a)
    list_all_articles = str(articles_list).split('href=')    
    with open('/home/arch/Bureau/articles_link.txt', 'w+') as f:
        for x in range(len(list_all_articles)):
            try:
                f.write(list_all_articles[x])
            except IndexError:
                pass
    articles_list.clear()
    with open('/home/arch/Bureau/only_link.txt', 'w+') as h:
        with open('/home/arch/Bureau/articles_link.txt', 'r+') as g:
            line = g.readlines()
            for lines in line:
                articles = re.findall("""\<a "/journal/.{0,800}>""",lines)
                newlist.append(articles)
            for x in range(len(newlist)+1):
                try:
                    if newlist[x] == '':
                        pass
                    else:
                        link = (str(newlist[x]))
                        articles_list.append(link)
                except IndexError:
                    pass
            for x in range(len(articles_list)+1):
                try:
                    if articles_list[x] == '[]':
                        pass
                    else:
                        browser.get('https://mediapart.fr/{}?onglet=full'.format(articles_list[x][7:-4]))
                        # python_button = browser.find_element_by_xpath('//*[@id="menuOutilsTopEl"]/ul[1]/li[4]/a')
                        # python_button.submit
                        time.sleep(60)



                except IndexError:
                    pass

if __name__ == '__main__':
    authenticate()


