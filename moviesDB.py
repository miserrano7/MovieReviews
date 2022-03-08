import os
import random
import requests
import json
from dotenv import load_dotenv, find_dotenv
from wiki_info import get_wiki_link


# This is to load your API keys from .env
load_dotenv(find_dotenv())

BASE_URL = "https://api.themoviedb.org/3/movie/"
CONFIG_URL = "https://api.themoviedb.org/3/configuration"
# base url for wiki api
WIKI_URL = "https://en.wikipedia.org/w/api.php"


def get_movie_data():
    # randomizing movie ids to then join with base url for movies to get a random movie each time
    movieIDS = ["19913", "22538", "8966"]
    randomPICK = random.choice(movieIDS)
    url_and_id = (BASE_URL, randomPICK)
    favMovies_URL = "".join(url_and_id)

    params = {"api_key": os.getenv("MOVIES_KEY")}
    response = requests.get(favMovies_URL, params=params)
    # getting json data for movie details
    data = response.json()
    responseImage = requests.get(CONFIG_URL, params=params)
    # getting json data for cofiguration to get the poster image
    dataImage = responseImage.json()

    def get_title():
        titles = data["title"]
        return titles

    titleReturned = get_title()

    def get_tagline():
        tagline = data["tagline"]
        return tagline

    def get_genre():
        genre = data["genres"]
        # https://www.kite.com/python/answers/how-to-find-the-values-of-a-key-in-a-list-of-dictionaries-in-python
        # creating list of all elements corresponding to the key
        # "name" within the list if dictionaries
        genre = [item["name"] for item in genre]
        genre = ", ".join(genre)
        return genre

    def get_pic():
        baseIMAGE_URL = dataImage["images"]["base_url"]
        posterSize = dataImage["images"]["poster_sizes"][6]
        posterPath = data["poster_path"]
        mytup = (baseIMAGE_URL, posterSize, posterPath)
        image = "".join(mytup)
        return image

    return (
        get_title(),
        get_tagline(),
        get_genre(),
        get_pic(),
        get_wiki_link(titleReturned),
        randomPICK,
    )