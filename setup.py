from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="shopstat",
    version="1.0",
    author="Pawel Dlugosz",
    author_email="pawel.dlugosz97@gmail.com",
    description="An app helping with planning daily shopping",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/pawlooss1/shopstat/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
)
