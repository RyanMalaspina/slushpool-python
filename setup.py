import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="slushpool",
    version="1.0.0",
    author="Ryan Malaspina",
    author_email="ryan@malaspina.tech",
    description="An API wrapper for Slushpool.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/RyanMalaspina/slushpool-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
