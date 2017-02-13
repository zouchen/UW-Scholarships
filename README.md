# UW Scholarships
A Python script using UWaterloo Open Data API to find all the available scholarships I'm qualified to apply for today.

###Sample API JSON output:
https://github.com/uWaterloo/api-documentation/blob/master/v2/awards/undergraduate.md


1. To fetch the JSON file to local machine:
  brew install wget
  wget https://api.uwaterloo.ca/v2/awards/undergraduate.json?key=4abfd4892a60a729f6c2225466121a44
  
2. To connect to the University of Waterloo Open Data API through the official Python wrapper **(currently under maintainance due to an Import Error)**:
  from uwaterlooapi import UWaterlooAPI
  uw = UWaterlooAPI(api_key="4abfd4892a60a729f6c2225466121a44")
  uw.current_weather()
