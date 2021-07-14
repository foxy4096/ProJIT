class Player:
    
    def __init__(self, name, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self.name = name

    def is_playing(self):
        return f"{self.name} is playing."


mario = Player("Mario")
print(mario.name)
print(mario.is_playing())