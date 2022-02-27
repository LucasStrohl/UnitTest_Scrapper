import unittest
from Scrapper import Scrapper
from selenium import webdriver 
from selenium.webdriver.common.by import By

class Test_ScrapperInit(unittest.TestCase):

    def setUp(self):
        print('begin')
        self.url = 'https://www.playstation.com/fr-fr/'
        self.scrapper = Scrapper(self.url)
    
    def test_initScrapper(self):
        self.assertEquals(self.scrapper.browser.current_url, self.url)
    
    def test_cookies(self):
        self.scrapper.acceptCookies()
        self.assertTrue(len(self.scrapper.browser.find_elements(By.ID, '_evidon-accept-button')) == 0)
    
    def test_storePage(self):
        self.scrapper.goToShop()
        self.assertEquals(self.scrapper.browser.current_url, 'https://store.playstation.com/fr-fr/category/44d8bb20-653e-431e-8ad0-c0a365f68d2f')

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False,verbosity=20)