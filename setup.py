import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="open_server_scraper",
    version="1.0.0",
    description="Utility to scrape open web servers with only file listing ('index of' type)",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ByteBaker/open_server_scraper",
    author="Shraddha Kishan",
    author_email="shraddha.kishan@gmail.com",
    license="GPL v3.0",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["open_server_scraper"],
    include_package_data=True,
    install_requires=[

    ],
    entry_points={
        "console_scripts": [
            "open_server_scraper=open_server_scraper.__main__:main",
        ]
    },
)