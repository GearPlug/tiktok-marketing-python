import requests
from urllib.parse import urljoin
from urllib.parse import urlencode
from tiktok_marketing import exceptions


class Client:
    API_URL = "https://business-api.tiktok.com/open_api/v1.2/"
    AUTHORIZATION_URL = "https://ads.tiktok.com/marketing_api/auth"

    def __init__(self, app_id: str = None, secret: str = None, access_token: str = None):
        """Initialize required parameters for API access."""
        self.app_id = app_id
        self.secret = secret
        self.access_token = access_token

    def get_authorization_url(self, redirect_uri, state=None) -> str:
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

    def authenticate(self, auth_code) -> dict:
        """
        After authorization is complete an auth_code is given, use it to generate a long-lived access token.
        https://ads.tiktok.com/marketing_api/docs?id=1701890914536450

        ## Returns
        - dict of shape:

        {
            "message": "OK",
            "code": 0,
            "data": {"access_token": "xxxxxxxxxxxxx", "scope": [4], "advertiser_ids": [1234, 1234]},
            "request_id": "2020042715295501023125104093250",
        }
        """
        authentication_url = self.build_url("oauth2/access_token/")
        return self.post(
            authentication_url,
            json=dict(
                app_id=self.app_id,
                secret=self.secret,
                auth_code=auth_code,
            ),
        )

    def set_access_token(self, access_token):
        self.access_token = access_token

    def get(self, url: str, **kwargs):
        return self.request("get", url, **kwargs)

    def post(self, url: str, json: dict, **kwargs):
        return self.request("post", url, json=json, **kwargs)

    def put(self, url: str, json: dict, **kwargs):
        return self.request("put", url, json=json, **kwargs)

    def delete(self, url: str, **kwargs):
        return self.request("delete", url, **kwargs)

    def build_url(self, endpoint: str) -> str:
        """
        This method returns the full url for the given endpoint.
        """
        return urljoin(self.API_URL, endpoint.lstrip("/"))

    def request(self, method, url, **kwargs):
        headers = kwargs.pop("headers", {})
        params = kwargs.pop("params", {})
        if self.access_token is not None:
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
        except:
            rsp = response.text
        finally:
            if not response.ok:
                error = None
                if "error" in rsp:
                    error = rsp["error"]
                if status_code == 400:
                    raise exceptions.BadRequestError(error, rsp)
                elif status_code == 401:
                    raise exceptions.UnauthorizedError(error, rsp)
                elif status_code == 403:
                    raise exceptions.ForbiddenError(error, rsp)
                elif status_code == 404:
                    raise exceptions.NotFoundError(error, rsp)
                elif status_code == 410:
                    raise exceptions.GoneError(error, rsp)
                elif status_code == 415:
                    raise exceptions.UnsupportedMediaTypeError(error, rsp)
                elif status_code == 422:
                    raise exceptions.UnprocessableEntityError(error, rsp)
                elif status_code == 429:
                    raise exceptions.TooManyRequestsError(error, rsp)
                elif status_code == 500:
                    raise exceptions.InternalServerError(error, rsp)
                elif status_code == 501:
                    raise exceptions.NotImplementedError(error, rsp)
                elif status_code == 503:
                    raise exceptions.ServiceUnavailableError(error, rsp)
                else:
                    raise exceptions.UnknownError(error, rsp)

            return rsp
