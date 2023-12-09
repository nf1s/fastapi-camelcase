# -*- coding: utf-8 -*-
import io
import re

from setuptools import setup

with io.open("README.md") as f:
    long_description = f.read()

with io.open("fastapi_camelcase/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)


setup(
    name="fastapi_camelcase",
    version=version,
    description="Package provides an easy way to have camelcase request/response bodies for Pydantic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://nf1s.github.io/fastapi-camelcase/",
    author="Ahmed Nafies",
    author_email="ahmed.nafies@gmail.com",
    license="MIT",
    packages=["fastapi_camelcase"],
    package_data={"fastapi_camelcase": ["py.typed"]},
    install_requires=["pydantic", "pyhumps"],
    project_urls={
        "Documentation": "https://nf1s.github.io/fastapi-camelcase/",
        "Source": "https://github.com/nf1s/fastapi-camelcase",
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    zip_safe=False,
    python_requires=">=3.9",
)
