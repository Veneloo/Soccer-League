#####################################################################################################
## Author: Axel Cazorla                                                                            ##
## Date: 9/21/2023                                                                                 ##
##                                                                                                 ##
##  This is the back-end of our web app, it will serve as the backbone to what we are building.    ##
##                                                                                                 ##
##                                                                                                 ##
##                                                                                                 ##
#####################################################################################################
import requests

url = "https://api-football-v1.p.rapidapi.com/v3/timezone"

headers = {
	"X-RapidAPI-Key": "1aa7dc7db4msh16f890c04202182p1f3efdjsn4fe3a701536d",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())