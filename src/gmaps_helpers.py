import googlemaps
import requests
import html
import json


class Location:


    def __init__(self, filepath, loc_names_list, loc_coords_list):
        
        ### Use interim method since we will not be making an API call
        ## Initialize the filepath to be manually declared
        self.filepath = filepath
        
        ## Initialize the lists to which we'll append the API responses later
        self.loc_names_list = loc_names_list
        self.loc_coords_list = loc_coords_list

    
    def get_response(self):

        ### Use interim json response to save on API calls ###
        ## Open the saved json response then access results sub-array
        with open(self.filepath) as f:
            data = json.load(f)
        self.response = data['results']
    

    def get_name_from_response(self):

        ## Count the number of results came back from API call
        loops = len(self.response)
        
        ## For each result, get the name and append to the above list
        for l in range(0,loops):
            self.loc_names_list.append(self.response[l]['name'])
    

    def get_coords_from_response(self):

        ## Count the number of results came back from API call
        loops = len(self.response)
        
        ## For each result, get the coords/lat-lon pair and append to the above list
        for l in range(0,loops):
            coords_pair = []
            coords_pair.append(self.response[l]['geometry']['location']['lng'])
            coords_pair.append(self.response[l]['geometry']['location']['lat'])
            self.loc_coords_list.append(coords_pair)
    

    def loc_main(self):

        ## All methods in sequence
        self.get_response()
        self.get_name_from_response()
        self.get_coords_from_response()