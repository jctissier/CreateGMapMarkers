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


Example Map: [test.html](http://creategmapmarkers-test.bitballoon.com/)
![alt text](http://i.imgur.com/eD7Qc28.png)
