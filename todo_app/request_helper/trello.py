import requests
import os

# 5c35fdf9de8cfa1419659630
TRELLO_API_KEY = os.getenv('TRELLO_API_KEY')
TRELLO_API_TOKEN = os.getenv('TRELLO_API_TOKEN')

headers = {
  "Accept": "application/json"
}

authQuery = {
  'key': TRELLO_API_KEY,
  'token': TRELLO_API_TOKEN
}

def make_request(method, url, query={}):
    return requests.request(
        method,
        url,
        headers=headers,
        params={**query, **authQuery}
    )
