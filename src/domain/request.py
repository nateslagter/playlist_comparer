import sys
sys.path.insert(1, '../appsettings')
import appsettings

class Request:

    url = ""

    def __init__(self, path, headers, grantType=None, queryParams=None):
        self.path = path
        self.headers = {"Authorization" :  "Bearer " + appsettings.accessToken}
        self.grant_type = grantType
        self.queryParams = queryParams
        self.url = self.request_builder()

    def __str__(self):
        return f"Request(path={self.path}, headers={self.headers}, grantType={self.grantType}, queryParams={self.queryParams})"
    
    def request_builder(self):
        url = f"{appsettings.baseUrl}/{self.path}"
        if self.queryParams:
            url += '?' + '&'.join([f"{key}={value}" for key, value in self.queryParams.items()])
        return url