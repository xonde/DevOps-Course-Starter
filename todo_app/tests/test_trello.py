import os
import pytest
import requests
from dotenv import load_dotenv, find_dotenv
from todo_app import app

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()

    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, 'request', stub)
    response = client.get('/')
    assert response.status_code == 200
    assert 'Item to do' in response.data.decode()

def stub(method, url, headers, params):
    test_board_id = os.environ.get('BOARD_ID')

    if url == f'https://api.trello.com/1/boards/{test_board_id}/lists' and method == 'GET':
        fake_response_data = [
            {
                'id': '1',
                'name': 'Things to do',
            },
            {
                'id': '2',
                'name': 'Doing',
            },
            {
                'id': '3',
                'name': 'Done',
            }
        ]
        return StubResponse(fake_response_data)

    if url == f'https://api.trello.com/1/boards/{test_board_id}/cards' and method == 'GET':
        fake_response_data = [
            {
                'id': '1',
                'name': 'Item to do',
                'idList': '1'
            },
            {
                'id': '2',
                'name': 'Item doing',
                'idList': '2'
            },
            {
                'id': '3',
                'name': 'Item done',
                'idList': '3'
            }
        ]

        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')
