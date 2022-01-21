from os import access
from tiktok_marketing.module import Module


class Leads(Module):
    """
    ## Leads module

    Reference: https://ads.tiktok.com/marketing_api/docs?id=1709486073255937

    ### Testing leads

    - Create test lead
    - Get test leads
    - Delete test lead

    ### Downloading leads

    - Create lead download task
    - Download leads

    ### Subscribing to leads

    - Subscribe to leads
    - Get subscriptions
    - Cancel subscription

    ### Leads migration

    - Get form libraries
    - Migrate leads to Business Center
    """

    def create_test_lead(
        self,
        page_id: int,
        advertiser_id: int = None,
        library_id: int = None,
    ) -> dict:
        """
        ## Reference

        https://ads.tiktok.com/marketing_api/docs?id=1701890943400962

        ## Parameters
        - page_id: number, required
            - The ID of the instant form.
        - advertiser_id: number, conditional
            - If the instant form and the generated leads are under an ad account,
            you must specify the advertiser ID.
        - library_id: number, conditional
            - If the instant form and the generated leads are under a Business Center,
            you must specify the ID of the form library that contains the instant form and leads.

        ## Returns
        - dict with the following keys:
            - request_id: string
            - lead_data: object
            - meta_data: object
                - lead_id: number
                - page_id: number
                - campaign_id: number
                - campaign_name: string
                - adgroup_id: number
                - adgroup_name: string
                - ad_id: number
                - ad_name: string
                - create_time: string
        """
        endpoint = self.client.build_url("pages/leads/mock/create/")
        data = dict(page_id=page_id)
        if advertiser_id is not None:
            data.update(advertiser_id=advertiser_id)
        elif library_id is not None:
            data.update(library_id=library_id)
        else:
            raise ValueError("Either advertiser_id or library_id must be specified.")

        return self.client.post(endpoint, data)

    def get_test_leads(
        self,
        page_id: int,
        advertiser_id: int = None,
        library_id: int = None,
    ) -> dict:
        """
        ## Reference

        https://ads.tiktok.com/marketing_api/docs?id=1709486980307969
        """
        # endpoint = self.client.build_url("pages/leads/mock/get/")
        raise NotImplementedError("Not implemented yet.")

    def delete_test_lead(
        self,
        lead_id: int,
        advertiser_id: int = None,
        library_id: int = None,
    ) -> dict:
        """
        ## Reference

        https://ads.tiktok.com/marketing_api/docs?id=1709487026425858

        ## Parameters
        - lead_id: number, required
            - The ID of the instant form.
        - advertiser_id: number, conditional
            - If the instant form and the generated leads are under an ad account,
            you must specify the advertiser ID.
        - library_id: number, conditional
            - If the instant form and the generated leads are under a Business Center,
            you must specify the ID of the form library that contains the instant form and leads.

        ## Returns
        - empty dict
        """
        endpoint = self.client.build_url("pages/leads/mock/delete/")
        data = dict(lead_id=lead_id)

        if advertiser_id is not None:
            data.update(advertiser_id=advertiser_id)
        elif library_id is not None:
            data.update(library_id=library_id)
        else:
            raise ValueError("Either advertiser_id or library_id must be specified.")

        return self.client.post(endpoint, data)

    def create_lead_download_task(
        self,
        advertiser_id=None,
        library_id=None,
        ad_id=None,
        page_id=None,
        task_id=None,
    ) -> dict:
        """
        ## Reference

        https://ads.tiktok.com/marketing_api/docs?id=1701890942344193
        """
        # endpoint = self.client.build_url("pages/leads/task/")
        raise NotImplementedError("Not implemented yet.")

    def download_leads(
        self,
        task_id: int,
        advertiser_id: int = None,
        library_id: int = None,
    ) -> dict:
        """
        ## Reference

        https://ads.tiktok.com/marketing_api/docs?id=1709486183758850
        """
        # endpoint = self.client.build_url("pages/leads/task/download/")
        raise NotImplementedError("Not implemented yet.")

    def subscribe_to_leads(
        self,
        callback_url: str,
        page_id: int = None,
        advertiser_id: int = None,
        library_id: int = None,
    ) -> dict:
        """
        ## Reference

        https://ads.tiktok.com/marketing_api/docs?id=1701890942854146

        ## Parameters
        - callback_url: string, required
            - The callback URL to which the leads will be sent.
        - page_id: number, required
            - The ID of the instant form that you want to subscribe to.
            - If not specified, all instant forms of the advertiser will be subscribed to.
        - advertiser_id: number, conditional
            - If leads are under ad account, you must specify the advertiser ID.
        - library_id: number, conditional
            - If leads are under a Business Center, you must specify the ID of the form
            library that contains the leads.

        ## Returns
        - dict with the following keys:
            - subscription_id: number
                - The subscription ID.
        """
        endpoint = self.client.build_url("subscription/subscribe/")
        data = self.client.build_app_data()
        access_token = self.client.get_access_token()
        subscription_detail = dict(
            access_token=access_token,
        )
        if page_id is not None:
            subscription_detail.update(page_id=page_id)

        if advertiser_id is not None:
            subscription_detail.update(advertiser_id=advertiser_id)
        elif library_id is not None:
            subscription_detail.update(library_id=library_id)
        else:
            raise ValueError("Either advertiser_id or library_id must be specified.")

        data.update(
            object="LEAD",
            url=callback_url,
            subscription_detail=subscription_detail,
        )

        return self.client.post(endpoint, data)

    def get_subscriptions(self, page: int, page_size: int = 10) -> dict:
        """
        ## Reference

        https://ads.tiktok.com/marketing_api/docs?id=1709486516846593
        """
        endpoint = self.client.build_url("subscription/get/")
        data = self.client.build_app_data()
        data.update(object="LEAD", page=page, page_size=page_size)
        return self.client.post(endpoint, data)

    def cancel_subscription(self, subscription_id: int) -> dict:
        """
        ## Reference

        https://ads.tiktok.com/marketing_api/docs?id=1709486460752897

        ## Parameters

        """
        endpoint = self.client.build_url("subscription/unsubscribe/")
        data = self.client.build_app_data()
        data.update(subscription_id=subscription_id)
        return self.client.post(endpoint, data)

    def get_from_libraries(self):
        """
        ## Reference

        https://ads.tiktok.com/marketing_api/docs?id=1721823886974977
        """
        endpoint = self.client.build_url("pages/library/get/")
        return self.client.get(endpoint)

    def transfer_leads(self, advertiser_id: int, bc_id: int) -> dict:
        """
        ## Reference

        https://ads.tiktok.com/marketing_api/docs?id=1721825310161922
        """
        data = dict(advertiser_id=advertiser_id, bc_id=bc_id)
        endpoint = self.client.build_url("pages/library/transfer/")
        return self.client.post(endpoint, data)
