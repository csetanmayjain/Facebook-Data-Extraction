
#accesing our profile data
import facebook
#import requests 
#!usr/bin/env python
# Program to mine data from your own facebook account

import json
def main():
	token = "" #get access token from facebook developer
	graph = facebook.GraphAPI(token)
	#fields = ['first_name', 'location{location}','email','link']
	profile = graph.get_object('me',fields='name,age_range,first_name,last_name,picture,birthday,email,favorite_athletes,favorite_teams,gender,location,quotes,friends,likes')	
	#return desired fields
	print(json.dumps(profile, indent=4))

if __name__ == '__main__':
	main()
    
"""    

#mine data from fb page
import json
import facebook

def main():
	
	graph = facebook.GraphAPI(token)
	page_name = raw_input("Enter a page name: ")
	
	# list of required fields
	fields = ['id','name','about','likes','link','band_members']
	
	fields = ','.join(fields)
	
	page = graph.get_object(page_name, fields=fields)
		
	print(json.dumps(page,indent=4))

if __name__ == '__main__':
	main()    
