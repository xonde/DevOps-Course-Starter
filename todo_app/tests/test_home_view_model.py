import pytest

from todo_app.model.item import Item
from todo_app.view_models.home_view_model import HomeViewModel

@pytest.fixture
def home_view_model() -> HomeViewModel:
    lists = [
        create_list('1', 'Things to do'),
        create_list('2', 'Doing'),
        create_list('3', 'Done')
    ]
    items = [
        create_item('1', 'Item to do', '1'),
        create_item('2', 'Item doing', '2'),
        create_item('3', 'Item done', '3')
    ]
    return HomeViewModel(items, lists)

def test_get_to_do_items(home_view_model: HomeViewModel):
    # Act
    to_do_items = home_view_model.things_to_do_items()

    # Assert
    assert len(to_do_items) == 1
    assert to_do_items[0].name == 'Item to do'

def test_get_doing_items(home_view_model: HomeViewModel):
    # Act
    to_do_items = home_view_model.doing_items()

    # Assert
    assert len(to_do_items) == 1
    assert to_do_items[0].name == 'Item doing'

def test_get_done_items(home_view_model: HomeViewModel):
    # Act
    to_do_items = home_view_model.done_items()

    # Assert
    assert len(to_do_items) == 1
    assert to_do_items[0].name == 'Item done'


def create_list(id, name):
    return {
        'id': id,
        'name': name
    }

def create_items(number_to_create, list_id):
    return list(create_item(i, f'Item {i}', list_id) for i in range(number_to_create))

def create_item(id, name, list_id):
    return Item.from_trello_card({
        'id': id,
        'name': name,
        'idList': list_id
    })
