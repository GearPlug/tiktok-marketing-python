import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="tiktok-marketing-python",
    version="1.0.1",
    description="Python developed library for TikTok Marketing API",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/GearPlug/tiktok-marketing-python",
    author="Santiago G. Alegria",
    author_email="sgiraldo@gearplug.io",
    license="MIT",
    packages=["tiktok_marketing"],
    install_requires=["requests"],
    zip_safe=False,
)
