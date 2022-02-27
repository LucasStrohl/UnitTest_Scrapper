import unittest
from Game import Game
from Request import Request

class Test_ScrapperGames(unittest.TestCase):

    def setUp(self):
        self.url = 'https://localhost:7194/api/Games'
        self.game = Game("EP4389-CUSA24277_00-SPELLFORCE3PS4EU", "SpellForce III Reforced", 39.99, "PS4", "7/6/2022", "THQ NORDIC GMBH", "RPG")

    def test_apiCall(self):
        response = Request.sendRequest(Request.POST, self.url, self.game.toJson())
        self.assertEqual(response.status_code, 201)
        
        response = Request.sendRequest(Request.GET, self.url + '/' + self.game.playstationId)
        self.assertEqual(response.status_code, 200)
        
        response = Request.sendRequest(Request.PUT, self.url + '/' + self.game.playstationId, self.game.toJson())
        self.assertEqual(response.status_code, 204)
        
        response = Request.sendRequest(Request.GET, self.url)
        self.assertEqual(response.status_code, 200)
        
        response = Request.sendRequest(Request.DELETE, self.url + '/' + self.game.playstationId)
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False,verbosity=20)