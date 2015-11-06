class Player:
    def __init__(self, name):
        print("Init Player with the name", name)
        self.name = name

    def __str__(self):
        return self.name
