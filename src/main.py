from api.apiClient import ApiClient
from api.credential import CredentialGenerator
import json

credentialManager = CredentialGenerator()
credentialManager.generateCredentials()
spotifyClient = ApiClient()

#print(json.dumps(spotifyClient.queryArtists(), sort_keys=True, indent=4))
print(json.dumps(spotifyClient.getPlaylist(), sort_keys=True, indent=4))