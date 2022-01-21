from tiktok_marketing.module import Module


class Auth(Module):
    def set_access_token(self, token: str):
        """This method sets the access token needed for API calls."""
        self.client.set_access_token(token)

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
        return self.client.build_authorization_url(redirect_uri, state)

    def authenticate(self, auth_code) -> dict:
        """
        After authorization is complete a valid 10-minute auth_code is given.
        Use this method to generate a long-lived access token with the auth_code.
        https://ads.tiktok.com/marketing_api/docs?id=1701890914536450

        ## Parameters
        - auth_code: str
            - 10-minute valid code to generate an access token.

        ## Returns
        - dict of shape:

        {
            "message": "OK",
            "code": 0,
            "data": {"access_token": "xxxxxxxxxxxxx", "scope": [4], "advertiser_ids": [1234, 1234]},
            "request_id": "2020042715295501023125104093250",
        }
        """
        authentication_url = self.client.build_url("oauth2/access_token/")
        authentication_data = self.client.build_authentication_data(auth_code)
        return self.client.post(authentication_url, authentication_data)
