class User_model:
    pokemon_cards = list()

    def __init__(self, username, password, user_id, mail):
        self.user_id = user_id
        self.mail = mail
        self.username = username
        self.password = password

    def add_pokemon_card(self, card):
        self.pokemon_cards.append(card)

    def remove_pokemon_card(self, card):
        self.pokemon_cards.remove(card)

    def authenticate(self, username, password):
        return username == self.username and password == self.password
