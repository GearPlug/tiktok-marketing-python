from ast import Mod
from tiktok_marketing.module import Module


class User(Module):
    def info(self):
        """
        Returns the authenticated user information
        
        Reference: https://ads.tiktok.com/marketing_api/docs?id=1701890922708994
        """
        endpoint = self.client.build_url("user/info/")
        return self.client.get(endpoint)
