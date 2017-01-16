# CreateGMapMarkers
Python wrapper for Google Maps API, automatically generates HTML with mapped markers

# Create an object and pass coordinates
1. Create an instance of the object 
```
map = CreateGoogleMapMarkers(map_center_latitude, map_center_longitude, zoom_level, map_center_icon, map_center_icon_title)

# map_center_latitude/longitude = single coordinate, can either be a string or a float
# zoom_level = controls how zoomed in the map will render, ranges from 0-18
# map_center_icon = 'none' for no markers, 'default' for pin seen in example below, 'picture_name.extension' found in icons folder 
# map_center_icon_title = Marker title if it exists, can pass HTML content
```


## Example Map: 
[test.html](http://creategmapmarkers-test.bitballoon.com/)
![alt text](http://i.imgur.com/eD7Qc28.png)
**Raw List of Coordinates:**
```
black_lat = ['49.284040', '49.283190']
black_lon = ['-123.115950', '-123.115680']
black_titles = ['black 1', 'black 2']
red_lat = ['49.283460', '49.284490', '49.284740']
red_lon = ['-123.116560', '-123.115000', '-123.115170']
red_titles = ['red 1', 'red 2', 'red 3']
yellow_lat = ['49.284740', '49.284790', '49.284580', '49.284580']
yellow_lon = ['-123.115170', '-123.115240', '-123.114610', '-123.117080']
yellow_titles = ['yellow 1', 'yellow 2', 'yellow 3', 'yellow 4']
red_lat2 = ['49.284790', '49.285050']
red_lon2 = ['-123.116780', '-123.116350']
red_titles2 = ['red 4', 'red 5']
```
**Creating object & creating HTML file:**
```
test = CreateGoogleMapMarkers("49.283140", -123.115950, 16, 'none', '<b>Current Location!</b>')
test.set_api_key('AIzaSyBXrysmCDm_vqwz6gSINY2f0X6eHJTGGQw')
test.create_markers(red_lat, red_lon, red_titles, 'red')
test.create_markers(black_lat, black_lon, 'None', 'black')
test.create_markers(yellow_lat, yellow_lon, yellow_titles, 'yellow')
test.create_markers(red_lat2, red_lon2, red_titles2, 'red')
test.map_markers('test')
```
