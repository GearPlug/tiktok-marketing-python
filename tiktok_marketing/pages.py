from datetime import datetime
from tiktok_marketing.module import Module


class Pages(Module):
    def get_pages(self, advertiser_id: int = None, library_id: int = None, **kwargs):
        """
        This method returns page ids that can be used in lead ads or collection ads.

        ## Parameters
        - `advertiser_id`: number, conditional
            - If the instant form and the generated leads are under an ad account,
            you must specify the advertiser ID.
        - `library_id`: number, conditional
            - If the instant form and the generated leads are under a Business Center,
            you must specify the ID of the form library that contains the instant form and leads.

        ## Keyword Arguments
        - `page`: number, optional, default: 1
            - The page number to retrieve.
        - `page_size`: number, optional, default: 100
            - The number of results to return per page.
        - `start`: timestamp, optional, default: 1546318800.0
            - Start time, Unix timestamp
        - `end`: timestamp, optional, default: datetime.now().timestamp()
            - End time, Unix timestamp
        - `status`: string, optional, default: None
            - Status of the instant form.
            - Options: EDITED, PUBLISHED
        - `title`: string, optional, default: None
            - Instant Form title, will filter the form that **contains** the words in the title.
        - `business_type`: string, optional, default: LEAD_GEN
            - Instant page type，optional values: LEAD_GEN(InstantForm), STORE_FRONT(Storefront Page)

        ## Returns
        - dict with the following keys:
            - page_info
                - total_number: 1,
                - page: 1,
                - page_size: 10,
                - total_page: 1
            - list:
                - status: "PUBLISHED",
                - duplicate_id: 6854791294359699461,
                - user_id: 6844401689412666374,
                - title: "page_title",
                - preview_url: "http://preview.page.url",
                - thumbnail: "http://preview.page.thumbnail",
                - create_time: 1596012542,
                - update_time: 1597055449,
                - publish_time: 1597055450,
                - page_id: 6854821673904898054,
                - template_id: 6852135057059610630
        """
        endpoint = self.client.build_url("pages/get/")
        default_start = datetime(2019, 1, 1).timestamp()
        default_end = datetime.now().timestamp()
        params = dict(
            page=kwargs.get("page", 1),
            page_size=kwargs.get("page_size", 100),
            update_time_range=dict(
                start=kwargs.get("start", default_start),
                end=kwargs.get("end", default_end),
            ),
        )
        status = kwargs.get("status", None)
        title = kwargs.get("title", None)
        business_type = kwargs.get("business_type", None)

        if advertiser_id is not None:
            params.update(advertiser_id=advertiser_id)
        elif library_id is not None:
            params.update(library_id=library_id)
        else:
            raise ValueError("Either advertiser_id or library_id must be specified.")

        if status is not None and isinstance(status, str) and status.upper() in ["EDITED", "PUBLISHED"]:
            params.update(status=status.upper())

        if title is not None and isinstance(title, str):
            params.update(title=title)

        if business_type is not None and business_type in ["LEAD_GEN", "STORE_FRONT"]:
            params.update(business_type=business_type)

        return self.client.get(endpoint, params=params)
