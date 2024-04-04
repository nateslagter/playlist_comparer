from api.credential import CredentialGenerator
import requests
import sys
sys.path.append("..")
import appsettings
from domain.request import Request



class ApiClient:

    def __init__(self) -> None:
        pass

    def sendGetRequest(self, request):
        response = requests.get(request.url, headers=request.headers)
        return response.json()

    def buildRequest(self):
        pass

    def queryArtists(self):
        request = Request("/artists", queryParams = "/2QoU3awHVdcHS8LrZEKvSM")
        response = self.sendGetRequest(request)
        return response
    
    def getAllPlaylists(self):
        request = Request("/me/playlists")
        response = self.sendGetRequest(request)
        return response
    
    def getPlaylist(self):
        request = Request("/playlists", queryParams = "/1pFsgCOBgwdlJU9QD6DBEd")
        response = self.sendGetRequest(request)
        return response