import requests
import os

headers = {
  "Accept": "application/json"
}

def load_params(query):
  TRELLO_API_KEY = os.environ.get('TRELLO_API_KEY')
  TRELLO_API_TOKEN = os.environ.get('TRELLO_API_TOKEN')

  auth_query = {
    'key': TRELLO_API_KEY,
    'token': TRELLO_API_TOKEN
  }

  return {**query, **auth_query}


def make_request(method, url, query={}):
    return requests.request(
        method,
        url,
        headers=headers,
        params=load_params(query)
    )
