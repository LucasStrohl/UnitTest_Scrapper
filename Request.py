import requests
import urllib3

urllib3.disable_warnings()

class Request:
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4
    HEADER = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Content-Type': 'application/json'
    }

    @staticmethod
    def sendRequest(method, url, data = {}):
        match method:
            case Request.GET:
                return requests.get(url, headers = Request.HEADER, verify=False)
            case Request.POST:
                return requests.post(url, headers = Request.HEADER, data = data, verify=False)
            case Request.PUT:
                return requests.put(url, headers = Request.HEADER, data = data, verify=False)
            case Request.DELETE:
                return requests.delete(url, headers = Request.HEADER, verify=False)
        return None