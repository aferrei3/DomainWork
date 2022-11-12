import requests

api_url = "https://domains.googleapis.com:443"
response = requests.get(api_url)
print(response.json())

