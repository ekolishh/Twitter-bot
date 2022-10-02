from lib2to3.pgen2 import driver
from re import search
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
import time
import random
with open("tweet atma botu.txt", "r" ,encoding="utf8") as tweets:
    tweetlist = list()
    text = tweets.read()
    tweetlist = text.split("\n")
   
    browser = webdriver.Edge()
    browser.get("https://twitter.com")
    browser.implicitly_wait(20)
    login = browser.find_element("xpath","//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a")
    login.click()
    time.sleep(5)
    username = browser.find_element("name","text")
    username.send_keys("Your Username")
    username.send_keys(Keys.ENTER)
    time.sleep(3)
    password = browser.find_element("name","password")
    password.send_keys("Your Password")
    password.send_keys(Keys.ENTER)

    time.sleep(7)
    

def tweet():
    while True:
        tivit = browser.find_element("xpath","//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
        tivit.click()
        time.sleep(5)
        sending_tivit =tweetlist[random.randint(0,len(tweetlist)-1)]
        tivit.send_keys(sending_tivit)
        time.sleep(2)
        tivit.send_keys(Keys.CONTROL, Keys.ENTER)

        
        time.sleep(15)

tweet()

    