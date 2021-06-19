# Github Projects Fetcher  (gp-fetcher)

- This a tool to fetch your github project details so that your time for writing an API is saved.
- Simple to use tool made in Python with bs4(Beautiful Soup)

## Link to the package: [pypi.org/project/gpfetcher](https://pypi.org/project/gpfetcher/)

## Documentation


*Assuming python and pip installed on your system*

- *Checkout resources to install [python](https://www.python.org/downloads/) and [pip](https://packaging.python.org/tutorials/installing-packages/) if not installed*

___
#### Installing the package gpfetcher

For linux and mac
```bash

pip3 install gpfetcher
```


For windows
```bash
pip install gpfetcher 
```


- Then use the package in your python file as shown below 

## Usage

```python
from gpfetcher import scraper

if __name__ == "__main__":
    username = "< github userrname here >"
    scraper.scrape(username)
```

- After you get the message below, check your root where your .py file is , a json file is generated that can be used in your projects

```bash
  Done! checkout your {github-username-here}-projects.json file at the root of this project directory
```
##### You are done!

*go ahead and use this json to parse in your project*


## Sample Output

```json
{
    "gp-fetcher": {
        "src": "https://github.com//DevGautam2000/gp-fetcher",
        "about": "You don't want to spend a lot of time just writing a block of code for fetching your projects from github. So, go ahead and use this python package to make your life easier",
        "tech-stack": [
            "Python"
        ],
        "license": "MIT License"
    },
    "infoScraper": {
        "src": "https://github.com//DevGautam2000/infoScraper",
        "about": "Scraper written in Python using bs4 to scrape results from SMIT results",
        "tech-stack": [
            "Python"
        ],
        "license": "MIT License"
    },
    "results-web": {
        "src": "https://github.com//DevGautam2000/results-web",
        "about": "The web app for Results",
        "tech-stack": [
            "JavaScript"
        ],
        "license": ""
    },
    "results.github.io": {
        "src": "https://github.com//DevGautam2000/results.github.io",
        "about": "",
        "tech-stack": [
            "Python"
        ],
        "license": ""
    },
```

- Also fetches the forked repos separately

```json

    "license": ""
    },
    "FORKED": {
        "Making-Musical-Apps": {
            "src": "https://github.com//DevGautam2000/Making-Musical-Apps",
            "about": "Resources for the O'Reilly book \"Making Musical Apps\"",
            "tech-stack": [
                "Pure Data"
            ],
            "license": "",
            "from": "Forked from nettoyeurny/Making-Musical-Apps"
        },
        "Simple-Guitar-Tuner": {
            "src": "https://github.com//DevGautam2000/Simple-Guitar-Tuner",
            "about": "Android app",
            "tech-stack": [
                "Java"
            ],
            "license": "",
            "from": "Forked from siemanko/Simple-Guitar-Tuner"
        }
    }
}

```

___
# Author
## Gautam Chandra Saha

2021 &copy; Gautam Chandra Saha
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
