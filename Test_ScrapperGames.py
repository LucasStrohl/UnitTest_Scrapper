import unittest
from Scrapper import Scrapper
from selenium import webdriver 
from selenium.webdriver.common.by import By

class Test_ScrapperGames(unittest.TestCase):

    def setUp(self):
        print('begin')
        self.url = 'https://www.playstation.com/fr-fr/'
        self.scrapper = Scrapper(self.url)
        self.scrapper.acceptCookies()
        self.scrapper.maximizeWindow()
        self.scrapper.goToShop()
    
    def test_getListOfGames(self):
        self.assertNotEqual(self.scrapper.getGames(), None)
    
    def test_hasMorePage(self):
        self.assertTrue(self.scrapper.hasNextPage())
    
    def test_changePage(self):
        urlFristPage = self.scrapper.browser.current_url
        self.scrapper.hasNextPage()
        urlSecondPage = self.scrapper.browser.current_url
        self.assertNotEquals(urlFristPage, urlSecondPage)

    def test_goInGamePage(self):
        game = self.scrapper.getGames()[0]
        self.scrapper.goToGame(game)
        self.assertTrue('https://store.playstation.com/fr-fr/product/' in self.scrapper.browser.current_url)

    def test_getGameData(self):
        game = self.scrapper.getGames()[0]
        self.scrapper.goToGame(game)
        gameData = self.scrapper.getGame()
        self.assertNotEqual(gameData, None)

    def test_goBack(self):
        urlFristPage = self.scrapper.browser.current_url
        self.scrapper.hasNextPage()
        self.scrapper.goBack()
        urlSecondPage = self.scrapper.browser.current_url
        self.assertEqual(urlFristPage, urlSecondPage)




if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False,verbosity=20)