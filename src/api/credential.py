import requests
import sys
sys.path.insert(1, '../appsettings')
import appsettings

class CredentialGenerator:

    headers = {"Content-Type" : "application/x-www-form-urlencoded"}
    data = {
        "grant_type" : "client_credentials", 
        "client_id" : appsettings.clientId, 
        "client_secret" : appsettings.clientSecret}

    def __init__(self) -> None:
        pass

    def generateCredentials(self):
        #sends request to spotify token API and retrieves the access token to use their API
        response = requests.post(appsettings.tokenUrl, data=self.data, headers=self.headers)        
        appsettings.accessToken = response.json()["access_token"]