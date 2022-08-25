import httpx

from httpx import Response

class HTTPRequest:
    def __init__(self, url: str,  method: str ="GET", headers: dict | None = None, data: dict | None =None, params: dict | None = None):
        """Initialize the request object

        Args:
            url (str): URL
            method (str, optional): HTTP request method. Defaults to "GET".
            headers (dict, optional): HTTP request headers. Defaults to None.
            data (dict, optional): HTTP request data. Defaults to None.
            params (dict, optional): HTTP request params. Defaults to None.
        """        
        self.url = url
        self.method = method
        self.headers = headers
        self.data = data
        self.params = params

    def send(self) -> Response | Exception:
        """Send the request
            
        Returns:
            httpx.Response: HTTP response
        """        
        try:
            with httpx.Client() as client:
                response = client.request(
                    method=self.method,
                    url=self.url,
                    headers=self.headers,
                    data=self.data,
                    params=self.params,
                )
                return response
        except Exception as e:
            return e