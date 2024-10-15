from setuptools import setup, find_packages

setup(
    name="airflow_4evr",
    version="0.1",
    packages=find_packages(),
    install_requires=["numpy"],  # Add any dependencies here
    description="A simple Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rnhttr/airflow_4evr",
    author="Ryan",
    author_email="your.email@example.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
