import os
import requests
import json

BASE_URL = "https://en.wikipedia.org/w/api.php"

# https://www.mediawiki.org/wiki/API:Opensearch
# https://stackoverflow.com/questions/7185288/how-can-i-get-wikipedia-content-using-wikipedias-api
# passing title as parameter to get same title for info for moviedb and also wiki
def get_wiki_link(title):
    params = {"action": "opensearch", "format": "json", "search": title, "limit": 1}

    response = requests.get(url=BASE_URL, params=params)
    DATA = response.json()
    # https://www.learnbyexample.org/python-nested-list/
    urlLink = DATA[3][0]
    return urlLink
