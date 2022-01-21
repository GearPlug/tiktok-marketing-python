# tiktok-marketing-python

Python developed library for [tiktok marketing api](https://ads.tiktok.com/marketing_api/docs)


## Installing
```
pip install git+https://github.com/GearPlug/tiktok-marketing-python.git
```

## Usage

### Using this library with OAuth 2.0

#### Client instantiation
```python
from tiktok_marketing.api import TikTokClient

client = TikTokClient(app_id='your_app_id', secret='your_secret')
```

#### Get authorization url
```python
# state is optional
url = client.auth.get_authorization_url("your_redirect_url", state="your_state")
```

#### Exchange the auth_code for an access_token
```python
response = client.auth.authenticate(auth_code)
access_token = response["access_token"]
```

#### Set access token
```python
client.auth.set_access_token(access_token)
```

## Requirements
- requests

## Contributing
We are always grateful for any kind of contribution including but not limited to bug reports, code enhancements, bug fixes, and even functionality suggestions.

#### You can report any bug you find or suggest new functionality with a new [issue](https://github.com/GearPlug/tiktok-marketing-python/issues).

#### If you want to add yourself some functionality to the wrapper:
1. Fork it ( https://github.com/GearPlug/tiktok-marketing-python )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Adds my new feature')
4. Push to the branch (git push origin my-new-feature)
5. Create a new Pull Request