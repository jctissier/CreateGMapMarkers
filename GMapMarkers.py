import json
import requests
from pprint import pprint
from bs4 import BeautifulSoup
import gmplot
import webbrowser
import time


class CreateGoogleMapMarkers(object):
    API_KEY = ''

    # Set API Key
    def __init__(self, center_lat, center_long, zoom, icon, title):
        self.center_location = (float(center_lat), float(center_long))
        self.zoom = int(zoom)
        self.icon = str(icon)
        self.title = str(title)
        self.key = API_KEY
        self.white_lats = []
        self.white_longs = []
        self.white_titles = []
        self.black_lats = []
        self.black_longs = []
        self.black_titles = []
        self.blue_lats = []
        self.blue_longs = []
        self.blue_titles = []
        self.orange_lats = []
        self.orange_longs = []
        self.orange_titles = []
        self.purple_lats = []
        self.purple_longs = []
        self.purple_titles = []
        self.red_lats = []
        self.red_longs = []
        self.red_titles = []
        self.green_lats = []
        self.green_longs = []
        self.green_titles = []
        self.yellow_lats = []
        self.yellow_longs = []
        self.yellow_titles = []
        self.custom_lats = []
        self.custom_longs = []
        self.custom_titles =[]

    @staticmethod
    def set_api_key(key):
        global API_KEY
        API_KEY = key
