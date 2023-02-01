class HomeViewModel:

    def __init__(self, items, lists):
        self._items = items
        self._lists = lists

    @property
    def items(self):
        return self._items

    @property
    def lists(self):
        return self._lists

    def name_for_list(self, id):
        return list(list['name'] for list in self.lists if list['id'] == id)[0]

    def id_for_list(self, name):
        return list(list['id'] for list in self.lists if list['name'] == name)[0]

    def get_items(self, status):
        return list(item for item in self.items if item.status == status)

    def doing_items(self):
        return self.get_items(self.id_for_list('Doing'))

    def things_to_do_items(self):
        return self.get_items(self.id_for_list('Things to do'))

    def done_items(self):
        return self.get_items(self.id_for_list('Done'))
