from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()
setup(
    name="image_processing",  
    version="0.0.1",
    author="Andrey Santos",
    author_email="correaandrey25@gmail.com",
    description="My short description",  
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andreysantos01?tab=repositories",  
    packages=find_packages(),
    install_requires= requirements,  
    python_requires=">=3.8",
)