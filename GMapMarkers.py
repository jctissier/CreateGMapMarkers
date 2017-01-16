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
        
    def map_markers(self, file_name):
        # Top of HTML file -> CONSTANT
        f = open(file_name + '.html', 'w')
        f.write('<!DOCTYPE html>\n')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('\t<meta http-equiv="content-type" content="text/html; charset=UTF-8" />\n')
        f.write('\t<title>Google Maps Markers</title>\n')
        f.write('\t<script src="http://maps.google.com/maps/api/js?key=' + API_KEY +
                '&sensor=true_or_false&libraries=visualization" type="text/javascript"></script>\n')
        f.write('</head>\n')
        f.write('<body style="margin:0px; padding:0px;" onload="initialize()">\n')
        f.write('\t<div id="map" style="width: 1500px; height: 1000px;"></div>\n')
        f.write('\t<script type="text/javascript">\n')
        f.write('\t\tfunction initialize() {\n')
        # Write current location lat & lons
        self.add_center_location(f)
        # create locations with different colored markers
        self.set_white_markers(f)
        self.set_black_markers(f)
        self.set_red_markers(f)
        self.set_purple_markers(f)
        self.set_green_markers(f)
        self.set_orange_markers(f)
        self.set_blue_markers(f)
        self.set_yellow_markers(f)
        # Bottom of HTML file -> CONSTANT
        f.write('\t\t\tsetMap(locationMarker);\n')
        f.write('\t\t}\n')
        f.write('\t</script>\n')
        f.write('</body>\n')
        f.write('</html>\n')
        f.close()

    # Adds a lat, lng for center of map
    def add_center_location(self, f):
        f.write('\t\t\tvar mapCenter = new google.maps.LatLng(%f, %f, \'%s\');\n' %
                (self.center_location[0], self.center_location[1], self.title))
        f.write('\t\t\tvar myOptions = {\n')
        f.write('\t\t\t\tzoom: %d,\n' % self.zoom)
        f.write('\t\t\t\tcenter: mapCenter,\n')
        f.write('\t\t\t\tmapTypeId: google.maps.MapTypeId.ROADMAP\n')
        f.write('\t\t\t};\n')
        f.write('\t\t\tvar map = new google.maps.Map(document.getElementById(\'map\'), myOptions);\n')
        f.write('\n')
        f.write('\t\t\tvar locationMarker = new google.maps.Marker({\n')
        f.write('\t\t\t\tposition: mapCenter,\n')
        f.write('\t\t\t\tanimation: google.maps.Animation.BOUNCE,\n')
        f.write('\t\t\t\tmap:map,\n')
        if self.icon == 'default':
            self.icon = 'pins/pin.png'
        f.write('\t\t\t\ticon: \'%s\' \n' % self.icon)
        f.write('\t\t\t});\n')
        f.write('\t\t\tvar locationWindow = new google.maps.InfoWindow();\n')
        f.write('\t\t\tgoogle.maps.event.addListener(locationMarker, \'click\', (function (locationMarker) {\n')
        f.write('\t\t\t\treturn function() {\n')
        f.write('\t\t\t\t\tlocationWindow.setContent(\'%s\');\n' % self.title)
        f.write('\t\t\t\t\tlocationWindow.open(map, locationMarker);\n')
        f.write('\t\t\t\t}\n')
        f.write('\t\t\t})(locationMarker));\n\n')

    # Add marker locations based on marker color
    def create_markers(self, latitudes, longitudes, titles, color):
        if color == 'white':
            self.white_lats.extend(latitudes)
            self.white_longs.extend(longitudes)
            if titles != "None":
                self.white_titles.extend(titles)
        elif color == 'red':
            self.red_lats.extend(latitudes)
            self.red_longs.extend(longitudes)
            if titles != "None":
                self.red_titles.extend(titles)
        elif color == 'orange':
            self.orange_lats.extend(latitudes)
            self.orange_longs.extend(longitudes)
            if titles != "None":
                self.orange_titles.extend(titles)
        elif color == 'purple':
            self.purple_lats.extend(latitudes)
            self.purple_longs.extend(longitudes)
            if titles != "None":
                self.purple_titles.extend(titles)
        elif color == 'yellow':
            self.yellow_lats.extend(latitudes)
            self.yellow_longs.extend(longitudes)
            if titles != "None":
                self.yellow_titles.extend(titles)
        elif color == 'blue':
            self.blue_lats.extend(latitudes)
            self.blue_longs.extend(longitudes)
            if titles != "None":
                self.blue_titles.extend(titles)
        elif color == 'black':
            self.black_lats.extend(latitudes)
            self.black_longs.extend(longitudes)
            if titles != "None":
                self.black_titles.extend(titles)
        elif color == 'green':
            self.green_lats.extend(latitudes)
            self.green_longs.extend(longitudes)
            if titles != "None":
                self.green_titles.extend(titles)
        elif color == 'custom':
            self.custom_lats.extend(latitudes)
            self.custom_longs.extend(longitudes)
            if titles != "None":
                self.custom_titles.extend(titles)

    def set_white_markers(self, f):
        if len(self.white_lats) == len(self.white_longs) and (len(self.white_lats) and len(self.white_longs)) != 0:
            if len(self.white_titles) != 0:
                self.add_locations_info(f, self.white_lats, self.white_longs,
                                        self.white_titles, 'pins/white.png', 'white')
            elif len(self.white_titles) == 0:
                self.add_locations_markers(f, self.white_lats, self.white_longs, 'pins/white.png', 'white')

    def set_red_markers(self, f):
        if len(self.red_lats) == len(self.red_longs) and (len(self.red_lats) and len(self.red_longs)) != 0:
            if len(self.red_titles) != 0:
                self.add_locations_info(f, self.red_lats, self.red_longs,
                                        self.red_titles, '', 'red')
            elif len(self.red_titles) == 0:
                self.add_locations_markers(f, self.red_lats, self.red_longs, '', 'red')

    def set_orange_markers(self, f):
        if len(self.orange_lats) == len(self.orange_longs) and (len(self.orange_lats) and len(self.orange_longs)) != 0:
            if len(self.orange_titles) != 0:
                self.add_locations_info(f, self.orange_lats, self.orange_longs,
                                        self.orange_titles, 'pins/orange.png', 'orange')
            elif len(self.orange_titles) == 0:
                self.add_locations_markers(f, self.orange_lats, self.orange_longs, 'pins/orange.png', 'orange')

    def set_purple_markers(self, f):
        if len(self.purple_lats) == len(self.purple_longs) and (len(self.purple_lats) and len(self.purple_longs)) != 0:
            if len(self.purple_titles) != 0:
                self.add_locations_info(f, self.purple_lats, self.purple_longs,
                                        self.purple_titles, 'pins/purple.png', 'purple')
            elif len(self.purple_titles) == 0:
                self.add_locations_markers(f, self.purple_lats, self.purple_longs, 'pins/purple.png', 'purple')

    def set_yellow_markers(self, f):
        if len(self.yellow_lats) == len(self.yellow_longs) and (len(self.yellow_lats) and len(self.yellow_longs)) != 0:
            if len(self.yellow_titles) != 0:
                self.add_locations_info(f, self.yellow_lats, self.yellow_longs,
                                        self.yellow_titles, 'pins/yellow.png', 'yellow')
            elif len(self.yellow_titles) == 0:
                self.add_locations_markers(f, self.yellow_lats, self.yellow_longs, 'pins/yellow.png', 'yellow')

    def set_blue_markers(self, f):
        if (len(self.blue_lats) == len(self.blue_longs)) and (len(self.blue_lats) and len(self.blue_longs)) != 0:
            if len(self.blue_titles) != 0:
                self.add_locations_info(f, self.blue_lats, self.blue_longs,
                                        self.blue_titles, 'pins/blue.png', 'blue')
            elif len(self.blue_titles) == 0:
                self.add_locations_markers(f, self.blue_lats, self.blue_longs, 'pins/blue.png', 'blue')

    def set_black_markers(self, f):
        if len(self.black_lats) == len(self.black_longs) and (len(self.black_lats) and len(self.black_longs)) != 0:
            if len(self.black_titles) != 0:
                self.add_locations_info(f, self.black_lats, self.black_longs,
                                        self.black_titles, 'pins/black.png', 'black')
            elif len(self.black_titles) == 0:
                self.add_locations_markers(f, self.black_lats, self.black_longs, 'pins/black.png', 'black')

    def set_green_markers(self, f):
        if len(self.green_lats) == len(self.green_longs) and (len(self.green_lats) and len(self.green_longs)) != 0:
            if len(self.green_titles) != 0:
                self.add_locations_info(f, self.green_lats, self.green_longs,
                                        self.green_titles, 'pins/green.png', 'green')
            elif len(self.green_titles) == 0:
                self.add_locations_markers(f, self.green_lats, self.green_longs, 'pins/green.png', 'green')
