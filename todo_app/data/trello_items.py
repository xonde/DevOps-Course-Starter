from todo_app.request_helper import trello
from todo_app.model.item import Item

def get_items(boardId):
    items = trello.make_request('GET', f"https://api.trello.com/1/boards/{boardId}/cards").json()
    return list(Item.from_trello_card(item) for item in items)

def add_item(listId, title):
    trello.make_request(
        'POST', 
        'https://api.trello.com/1/cards', 
        {
            'idList': listId,
            'name': title
        })

def save_item(itemId, listId):
    trello.make_request('PUT', f'https://api.trello.com/1/cards/{itemId}', {
        'idList': listId
    })