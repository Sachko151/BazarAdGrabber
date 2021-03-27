from time import sleep

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import AdReader


def browsePage(url):
    hasNextPage = True
    while hasNextPage == True:
        browser = webdriver.Firefox(executable_path='D:\D\Python\FirefoxGecko\geckodriver.exe')
        browser.get(url)
        browser.find_element_by_class_name('fc-button-label').click()
        i = 1;
        for i in range(29):
            # ActionChains(browser).move_to_element(browser.find_element_by_xpath('/html/body/div[1]/div/div[8]/div[1]/div[1]/div['+str(i)+']/a/img'))
            try:
                browser.find_element_by_xpath(
                    '/html/body/div[1]/div/div[7]/div[1]/div[1]/div[' + str(i) + ']/a/img').click()
                AdReader.printAd(browser.current_url)
            except Exception as e:
                print(e)
            browser.back()
        try:
            browser.find_element_by_xpath('/html/body/div[1]/div/div[7]/div[1]/div[3]/a[11]').click()
            url = browser.current_url
        except:
            hasNextPage = False
