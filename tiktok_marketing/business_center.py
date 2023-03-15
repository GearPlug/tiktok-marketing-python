from tiktok_marketing.module import Module


class BusinessCenter(Module):
    """
    ## Business Center module

    Reference: https://ads.tiktok.com/marketing_api/docs?id=1739562438061058
    """

    def get_business_centers(self, bc_id: int = None, **kwargs):
        endpoint = self.client.build_url("bc/get/")
        params = dict(page=kwargs.get("page", 1), page_size=kwargs.get("page_size", 100))
        if bc_id is not None:
            params.update(bc_id=bc_id)
        return self.client.get(endpoint, params=params)

    def create_advertiser_account(
        self,
        bc_id: int,
        advertiser_info: dict,
        customer_info: dict,
        billing_group_info: dict,
        contact_info: dict = None,
        billing_info: dict = None,
        qualification_info: dict = None,
    ):
        """
        Reference: https://ads.tiktok.com/marketing_api/docs?id=1739939020318721
        """
        endpoint = self.client.build_url("bc/advertiser/create/")
        data = {
            "bc_id": bc_id,
            "advertiser_info": advertiser_info,
            "customer_info": customer_info,
            "billing_group_info": billing_group_info,
        }
        if contact_info is not None:
            data.update(contact_info=contact_info)
        if billing_info is not None:
            data.update(billing_info=billing_info)
        if qualification_info is not None:
            data.update(qualification_info=qualification_info)
        return self.client.post(endpoint, data)
