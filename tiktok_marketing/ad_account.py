from xml.etree.ElementInclude import include
from tiktok_marketing.module import Module


class AdAccount(Module):
    def get_advertisers(self) -> dict:
        """
        This method returns a list of advertiser accounts that authorized an app

        ## Reference

        https://ads.tiktok.com/marketing_api/docs?id=1708503202263042

        ## Returns
        - dict of shape:
        {
            "list": [
                {
                    "advertiser_id": "string",
                    "advertiser_name": "string",
                },
                ...
            ]
        }

        """
        endpoint = self.client.build_url("oauth2/advertiser/get/")
        params = self.client.build_app_data(include_access_token=True)
        return self.client.get(endpoint, params=params)

    def get_advertiser_info(self, advertiser_ids: list, fields: list = None) -> list:
        """
        This method returns the details of an advertiser's account.
        To minimize the number of API calls, a list of advertiser ids can be provided.

        ## Reference

        https://ads.tiktok.com/marketing_api/docs?id=1708503235186689

        ## Parameters
        - advertiser_ids: list, required
            - list of advertiser ids
        - fields: list, optional
            - list of advertiser info fields to return, available options:
                - promotion_area
                - telephone
                - contacter
                - currency
                - phonenumber
                - timezone
                - id
                - role
                - company
                - status
                - description
                - reason
                - address
                - name
                - language
                - industry
                - license_no
                - email
                - license_url
                - country
                - balance
                - create_time

        """
        endpoint = self.client.build_url("advertiser/info/")
        params = dict(advertiser_ids=advertiser_ids)
        if fields is not None:
            params.update(fields=fields)
        return self.client.get(endpoint, params=params)
