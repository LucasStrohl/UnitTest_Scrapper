import json
from datetime import datetime
from datetime import date
from Request import Request

class Game:

    def __init__(self, playstationId, title, price, platform, releaseDate, publisher, genre):
        self.playstationId = playstationId
        self.title = title
        self.price = price
        self.platform = platform
        self.releaseDate = str(datetime.strptime(releaseDate, '%d/%m/%Y').date())
        self.publisher = publisher
        self.genre = genre
        self.createdAt = str(date.today())
    
    def toJson(self):
        return json.dumps(self.__dict__)
    
    def sendToBDD(self, url):

        response = Request.sendRequest(Request.GET, url + '/' + self.playstationId)
        print("Exist code : " + str(response.status_code))
        if response.status_code == 200:
            response = Request.sendRequest(Request.PUT, url + '/' + self.playstationId, self.toJson())
            print("PUT code : " + str(response.status_code))
        else:
            response = Request.sendRequest(Request.POST, url, self.toJson())
            print("POST code : " + str(response.status_code))
        return response