from todo_app.request_helper import trello
from todo_app.model.item import Item

def get_items(board_id):
    items = trello.make_request('GET', f"https://api.trello.com/1/boards/{board_id}/cards").json()
    return list(Item.from_trello_card(item) for item in items)

def add_item(list_id, title):
    trello.make_request(
        'POST', 
        'https://api.trello.com/1/cards', 
        {
            'idList': list_id,
            'name': title
        })

def save_item(item_id, list_id):
    trello.make_request('PUT', f'https://api.trello.com/1/cards/{item_id}', {
        'idList': list_id
    })