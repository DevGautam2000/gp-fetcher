# Github Projects Fetcher  (gp-fetcher)

- This a tool to fetch your github project details so that your time for writing an API is saved.
- Simple to use tool made in Python with bs4(Beautiful Soup)

## Link to the package: [pypi.org/project/gpfetcher/0.2/](https://pypi.org/project/gpfetcher/0.2/)

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

___
# Author
## Gautam Chandra Saha

2021 &copy; Gautam Chandra Saha
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
