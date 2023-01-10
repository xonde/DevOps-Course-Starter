class Item:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status
 
    @classmethod
    def from_trello_card(cls, card):
        return cls(card['id'], card['name'], card['idList'])