# UW Scholarships
A Python script using UWaterloo Open Data API to find all the available scholarships I'm qualified to apply for today.

###Sample API JSON output:
https://github.com/uWaterloo/api-documentation/blob/master/v2/awards/undergraduate.md


1. To fetch the JSON file to local machine:
```Shell
brew install wget
wget https://api.uwaterloo.ca/v2/awards/undergraduate.json?key=YOUR_API_KEY
```
  
2. To connect to the University of Waterloo Open Data API through the official Python wrapper **(currently under maintainance due to an Import Error)**:
```Python
from uwaterlooapi import UWaterlooAPI
uw = UWaterlooAPI(api_key="YOUR API KEY")
dir(uw)
```
