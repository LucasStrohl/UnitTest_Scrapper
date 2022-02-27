import time
import re
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Game import Game

class Scrapper:
    SLEEP = 2
    
    def __init__(self, url):
        self.browser = webdriver.Chrome('C:/Program Files (x86)/chromedriver_win32/chromedriver.exe')
        self.browser.get(url)
        time.sleep(self.SLEEP)

    def goBack(self):
        self.browser.back()
        time.sleep(self.SLEEP)

    def acceptCookies(self):
        cookies = self.browser.find_element(By.ID, '_evidon-accept-button')
        cookies.click()

    def maximizeWindow(self):
        self.browser.maximize_window()

    def goToShop(self):
        shop = self.browser.find_element(By.ID, 'menu-button-primary--msg-shop')
        shop.click()
        time.sleep(self.SLEEP)

        shopLink = self.browser.find_element(By.ID, 'link-link-list--msg-shop-1')
        shopLink.click()
        time.sleep(self.SLEEP)

    def getGames(self):
        return self.browser.find_elements(By.XPATH, 'html/body/div[3]/main/section/div/div/div/div[2]/div[2]/ul/li')

    def getGame(self):
        url = self.browser.current_url.split('/')
        playstationId = url[len(url)-1]

        gameHeader = self.browser.find_element(By.XPATH, 'html/body/div[3]/main/div/div[1]/div[3]/div[2]/div/div/div')
        title = gameHeader.find_element(By.CSS_SELECTOR, 'h1.psw-t-title-l').text
        price = float(re.findall(r'[\d\.\d]+', gameHeader.find_element(By.CSS_SELECTOR, 'span.psw-t-title-m').text.replace(",", "."))[0]) if len(re.findall(r'[\d\.\d]+', gameHeader.find_element(By.CSS_SELECTOR, 'span.psw-t-title-m').text.replace(",", "."))) > 0 else float(0)
        
        gameBody = self.browser.find_element(By.CSS_SELECTOR, 'dl.psw-l-grid')
        platform = gameBody.find_element(By.XPATH, 'dd[1]').text
        release = gameBody.find_element(By.XPATH, 'dd[2]').text
        publisher = gameBody.find_element(By.XPATH, 'dd[3]').text
        genre = gameBody.find_element(By.XPATH, 'dd[4]').text

        return Game(playstationId, title, price, platform, release, publisher, genre)

    def goToGame(self, game):
        game.find_element(By.XPATH, 'div/a').click()
        time.sleep(self.SLEEP)

    def hasNextPage(self):
        nextButton = self.browser.find_element(By.XPATH, 'html/body/div[3]/main/section/div/div/div/div[2]/div[2]/div/nav/button[2]')
        if not 'disable' in nextButton.get_attribute('class'):
            nextButton.click()
            time.sleep(self.SLEEP)
            return True
        return False
