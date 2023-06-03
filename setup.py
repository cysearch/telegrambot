from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="telegrambot",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["requests"],
    author="Cysearch",
    author_email="cmatboo@skiff.com",
    description="A Python package for interacting with the Telegram Web API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cysearch/telegrambot",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)