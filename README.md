# Project 4
ENGO 551

The purpose of this web application is to display all of the schools in Calgary along with all of the Healthcare service locations.
When the user hovers their mouse over a school or healthcare service, the name is displayed in a popup. When the user clicks on
a school marker, a red circle appears around the closest healthcare service to that school.

application.py - The flask application for this web app. In this project, there is only one route, so it is very simple. The python
code passes the url for the two geojson files containing the school and healthcare service data.

index.html - The main html file for this project. First, the data from the two geojson files is loaded into two variables using fetch.
The provided mapbox tutorial was followed, and the mapbox light style was used. The two layers were added to the map separately. The
schools are represented by the "school" symbol (pencil and ruler), and the healthcare services are represented by the "hospital"
symbol (cross). Hovering over a school or healthcare service symbol will display a popup with the name and address. The popup closes
itself when the mouse is moved off the symbol. Clicking on a school symbol will call the turf.nearest() function to find the
nearest healthcare service to that school. The nearest healthcare service will be displayed with a red circle around the symbol.

layout.html - The layout format for any html pages (in this project there is only one). Contains all header links as well as styling.

requirements.txt - contains requirements of what has to be installed to run the application.
