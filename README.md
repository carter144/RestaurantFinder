# RestaurantFinder

This script uses the Google Places API to generate the top restaurants near you based on ratings or a random restaurant.

To retrieve a Places API from Google visit: https://developers.google.com/console

## Requirements
You will need Python 3.7.2 or above with pip

To install:

`git clone git@github.com:carter144/RestaurantFinder.git`

`cd RestaurantFinder`

`pip install -r requirements.txt`

## Running the program

1. Set your API Key by replacing `<YOUR API KEY HERE>` with your Places API key that starts with "AI..."
2. Change the lat/long values in `restaurants = Restaurants('37.62569530416217', '-77.55075216293335', radius, keyword, key, rand)`


The script will take in 3 parameters:
1. -r (radius) in meters
2. -k (keyword) a keyword to search for ex: (pizza in NY)
3. -random (y) If there is a value for random then the program will only generate one random restaurant

To generate a list of the top restaurants within your area:

`python restaurants.py -r 5000`

To generate a list of the top pizza restaurants within you area:

`python restaurants.py -r 5000 -k pizza`

To generate a random restaurant within your area:

`python restaurants.py -r 5000 -random y`

To generate a random pizza restaurant within you area:

`python restaurants.py -r 5000 -k pizza -random y`

