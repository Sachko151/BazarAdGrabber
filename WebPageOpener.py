from time import sleep

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import AdReader


def browsePageBazar(url):
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
                print(browser.current_url)
                AdReader.printAdBazar(browser.current_url)
            except Exception as e:
                print(e)
            browser.back()
        try:
            browser.find_element_by_xpath('/html/body/div[1]/div/div[7]/div[1]/div[3]/a[11]').click()
            url = browser.current_url
        except:
            hasNextPage = False

def browsePageOlx(url):
    hasNextPage = True
    while hasNextPage == True:
        browser = webdriver.Firefox(executable_path='D:\D\Python\FirefoxGecko\geckodriver.exe')
        browser.get(url)
        sleep(4)
        browser.find_element_by_id('onetrust-accept-btn-handler').click()
        i = 1;
        for i in range(43):
            # ActionChains(browser).move_to_element(browser.find_element_by_xpath('/html/body/div[1]/div/div[8]/div[1]/div[1]/div['+str(i)+']/a/img'))
            try:
                browser.find_element_by_xpath(
                    '/html/body/div[1]/div[5]/section/div[3]/div/div[1]/table[2]/tbody/tr['+str(i)+']/td/div/table/tbody/tr[1]/td[1]/a/img').click()
                print(browser.current_url)
                AdReader.printAdOlx(browser.current_url)
            except Exception as e:
                print(e)
            browser.back()
        try:
            browser.find_element_by_xpath('/html/body/div[1]/div[5]/section/div[3]/div/div[4]/span[17]/a').click()
            url = browser.current_url
        except:
            hasNextPage = False
