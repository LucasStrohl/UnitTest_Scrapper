import time
import requests
import re
import json
from selenium import webdriver 
from selenium.webdriver.common.by import By
from Scrapper import Scrapper
from Request import Request

hasNext = True
urlScrapper = 'https://www.playstation.com/fr-fr/'
baseUrlRequest = "https://localhost:7194/api/Games"

scrapper = Scrapper(urlScrapper)
scrapper.acceptCookies()
scrapper.maximizeWindow()
scrapper.goToShop()

while hasNext:
    games = scrapper.getGames()

    for i in range(len(games)):
        scrapper.goToGame(games[i])

        game = scrapper.getGame()
        
        response = game.sendToBDD(baseUrlRequest)
        
        scrapper.goBack()
        
        games = scrapper.getGames()

    hasNext = scrapper.hasNextPage()

