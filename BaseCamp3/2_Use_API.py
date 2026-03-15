# Import requests module to make http requests
import requests
import json

# The URL and the query params, as indicated by the API spec / doc.
# Refer https://rapidapi.com/hub
url = "https://real-time-news-data.p.rapidapi.com/search"
querystring = {"query":"AI Research","limit":"10","time_published":"anytime","country":"US","lang":"en"}

# Add Headers to the request
headers = {
	"x-rapidapi-key": "012ea5f51emsha209a0c6433707fp13f528jsndad181f9b450",					   
	"x-rapidapi-host": "real-time-news-data.p.rapidapi.com"
}

# Place a request and receive the response
response = requests.get(url, headers=headers, params=querystring)
response_data = response.json ()

# Align better the JSON content
print(json.dumps(response_data, indent=4))
