from tiktok_marketing.client import Client
from tiktok_marketing.auth import Auth
from tiktok_marketing.ad_account import AdAccount
from tiktok_marketing.leads import Leads
from tiktok_marketing.user import User


class TikTokClient:
    """
    Facade to provide access to different API modules

    Modules reference: https://ads.tiktok.com/marketing_api/docs?id=1705600933769218
    """

    def __init__(self, app_id: str, secret: str) -> None:
        client = Client(app_id=app_id, secret=secret)
        self.auth = Auth(client)
        self.ad_account = AdAccount(client)
        self.leads = Leads(client)
        self.user = User(client)
        # TODO: Ads
        # TODO: Ad Comments
        # TODO: Ad Groups
        # TODO: Audiences
        # TODO: Automated Rules
        # TODO: Business Center
        # TODO: BC Partners
        # TODO: BC Members
        # TODO: Campaigns
        # TODO: Catalogs
        # TODO: Catalog Event Source
        # TODO: Catalog Feeds
        # TODO: Catalog Products
        # TODO: Catalog Product Sets
        # TODO: Catalog Videos
        # TODO: Change Log
        # TODO: Creative Portfolios
        # TODO: Events API
        # TODO: Files
        # TODO: Identity
        # TODO: Images
        # TODO: Mobile Apps
        # TODO: Music
        # TODO: Pangle
        # TODO: Pixels
        # TODO: Reach and Frequency
        # TODO: Reporting
        # TODO: Spark Ads
        # TODO: Split Test
        # TODO: Terms
        # TODO: TikTok Store
        # TODO: Tools
        # TODO: Videos
