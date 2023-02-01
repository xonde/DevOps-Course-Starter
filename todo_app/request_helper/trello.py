import requests
import os

TRELLO_API_KEY = os.getenv('TRELLO_API_KEY')
TRELLO_API_TOKEN = os.getenv('TRELLO_API_TOKEN')

headers = {
  "Accept": "application/json"
}

auth_query = {
  'key': TRELLO_API_KEY,
  'token': TRELLO_API_TOKEN
}

def make_request(method, url, query={}):
    return requests.request(
        method,
        url,
        headers=headers,
        params={**query, **auth_query}
    )
