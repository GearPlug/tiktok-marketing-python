# tiktok-marketing-python
![](https://img.shields.io/badge/version-1.0.1-success) ![](https://img.shields.io/badge/Python-3.8%20|%203.9%20|%203.10%20|%203.11-4B8BBE?logo=python&logoColor=white)

Python developed library for [tiktok marketing api](https://ads.tiktok.com/marketing_api/docs)


## Installing
```
pip install tiktok-marketing-python
```

## Usage

### Using this library with OAuth 2.0

#### Client instantiation
```python
from tiktok_marketing import TikTokClient

client = TikTokClient('your_app_id', 'your_secret')
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
   - To add new modules create a file `<module_name>.py`
   - create a class that extends `module.py::Module`
   - Import and add the new module to `api.py::TikTokClient` and remove the todo comment
4. Push to the branch (git push origin my-new-feature)
5. Create a new Pull Request