#!/usr/bin/env python


'''
Sample API JSON output:
https://github.com/uWaterloo/api-documentation/blob/master/v2/awards/undergraduate.md


1. To fetch the JSON file to local machine:

brew install wget
wget https://api.uwaterloo.ca/v2/awards/undergraduate.json?key=4abfd4892a60a729f6c2225466121a44


2. To connect to the University of Waterloo Open Data API through the official Python wrapper:
(currently under maintainance due to an Import Error)

from uwaterlooapi import UWaterlooAPI
uw = UWaterlooAPI(api_key="4abfd4892a60a729f6c2225466121a44")
uw.current_weather()
'''


import json
from datetime import datetime


# Personal information
year = "Year Three"
prog = "Computer Science"
citizenship = "Canadian citizen/Permanent resident"



# helper functions:

# beforeDeadlines(deadlines) checks if there's a deadline in the list deadlines that's on/after today.
def beforeDeadlines(deadlines):
    for each in deadlines:
        if each >= datetime.today():
            return True
    return False


# valid(award) checks if the award dictionary is valid today.
def valid(award):
    applicationDeadlines = award["deadlines"]["application"]
    
    deadlines = []
    if applicationDeadlines != ["Varies"] and applicationDeadlines != []:
        for each in applicationDeadlines:
            deadlines.append(datetime.strptime(each, "%B %d"))
    
    if award["status"] == "Active" and (applicationDeadlines == ["Varies"] or applicationDeadlines == [] or beforeDeadlines(deadlines)):
        return True
    
    return False


# qualified(award, year, prog, citizenship) checks if the required conditions to apply for the award are met.
def qualified(award, year, prog, citizenship):

    if citizenship in award["citizenship"] and (prog in award["programs"] or award["programs"] == ["Open to any program"]) and year in award["application"]["enrollment_year"]:
        return True
    
    return False



# main

if __name__ == "__main__":
    with open('undergraduate.json?key=4abfd4892a60a729f6c2225466121a44.json') as jsonFile:
        jsonString = jsonFile.read()
        data = json.loads(jsonString)
        jsonFile.close()
    
        count = 0
        
        for award in data["data"]:
            
            if valid(award) and qualified(award, year, prog, citizenship):
                count += 1
                
                print("{0}. ".format(count))
                print("Value: {0}".format(award["value"]))
                
                if award["application"]["eligibility"] == []:
                    print("Eligibility: N/A")
                else:
                    print("Eligibilities: ")
                    for each in award["application"]["eligibility"]:
                        print(each)
                        
                print("link: {0}\n\n".format(award["link"]))
        
        print("Summary: There're {0} scholarships/awards that you can apply for today!".format(count))

    