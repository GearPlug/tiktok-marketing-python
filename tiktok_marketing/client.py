import requests
from urllib.parse import urljoin
from urllib.parse import urlencode
from tiktok_marketing.exceptions import ExceptionFactory


class Client:
    """
    Requests library wrapper to perform calls to tiktok marketing api.
    """

    API_URL = "https://business-api.tiktok.com/open_api/v1.3/"
    SANDBOX_URL = "https://sandbox-ads.tiktok.com/open_api/v1.3/"
    AUTHORIZATION_URL = "https://ads.tiktok.com/marketing_api/auth"

    def __init__(
        self,
        app_id: str = None,
        secret: str = None,
        access_token: str = None,
        sandbox: bool = False,
    ):
        """Initialize required parameters for API access."""
        self.app_id = app_id
        self.secret = secret
        self.access_token = access_token
        self.sandbox = sandbox
        self.exceptions = ExceptionFactory()

    def set_access_token(self, access_token):
        self.access_token = access_token

    def get_access_token(self):
        return self.access_token

    def get(self, url: str, **kwargs):
        return self.request("get", url, **kwargs)

    def post(self, url: str, json: dict, **kwargs):
        return self.request("post", url, json=json, **kwargs)

    def put(self, url: str, json: dict, **kwargs):
        return self.request("put", url, json=json, **kwargs)

    def delete(self, url: str, **kwargs):
        return self.request("delete", url, **kwargs)

    def build_app_data(self, include_access_token=False, **kwargs) -> dict:
        """This method returns the app_id and the secret as a dict."""
        data = dict(app_id=self.app_id, secret=self.secret, **kwargs)
        if include_access_token:
            data.update(access_token=self.access_token)

        return data

    def build_url(self, endpoint: str) -> str:
        """
        This method returns the full url for the given endpoint.
        All endpoints must be relative to API_URL.
        """
        base_url = self.API_URL if not self.sandbox else self.SANDBOX_URL
        return urljoin(base_url, endpoint.lstrip("/"))

    def build_authorization_url(self, redirect_uri, state=None) -> str:
        """
        This method returns the oauth authorization url.
        https://ads.tiktok.com/marketing_api/docs?id=1701890912382977

        ## Parameters
        - redirect_uri: str
            - The redirect uri to which the user will be redirected after authorization.
            must match the redirect_uri registered in the app.
        - state: str
            - optional random string of your choice
        """
        params = dict(
            app_id=self.app_id,
            redirect_uri=redirect_uri,
        )

        if state is not None:
            params.update(state=state)

        return self.AUTHORIZATION_URL + "?" + urlencode(params)

    def build_authentication_data(self, auth_code: str) -> dict:
        """This method returns the needed data to obtain the access token."""
        app_data = self.build_app_data(auth_code=auth_code)
        return app_data

    def request(self, method, url, **kwargs):
        """
        This method performs the requests to the API.
        If access_token is set it will be added to the headers.
        If method is post or put Content-Type: application/json will be added to the headers.

        ## Parameters
        - method: str
            - The HTTP method to use.
        - url: str
            - can be any url but TikTok API endpoints are expected
            - use build_url beforehand to get the endpoint full path.
        - kwargs: dict
            - any other parameters that can be passed to the requests library.
            - keep allow_redirects=True
        """
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        if self.access_token is not None and "access_token" not in params:
            headers["Access-Token"] = self.access_token

        if method in ["post", "put"]:
            headers["Content-Type"] = "application/json"

        response = requests.request(
            method,
            url,
            headers=headers,
            params=params,
            allow_redirects=True,
            **kwargs,
        )
        return self.parse_response(response)

    def parse_response(self, response: requests.Response):
        """
        This method decodes the response if there's any problem it will raise a custom exception.

        ## Parameters
        - response: requests.Response
        """
        try:
            status_code = response.status_code
            rsp = response.json()
            tiktok_code = int(rsp.get("code", 0))
        except:
            rsp = response.text
        finally:
            if not response.ok:
                message = None
                if "error" in rsp:
                    message = rsp["error"]

                raise self.exceptions.get_exception(status_code, message, rsp)

            if "code" in rsp and tiktok_code != 0:
                message = rsp.get("message", None)
                print(rsp)
                raise self.exceptions.get_exception(tiktok_code, message, rsp)

            if "data" in rsp and isinstance(rsp, dict):
                return rsp.get("data", {})
            else:
                return rsp
