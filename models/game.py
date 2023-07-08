import random 

class Game:
    def __init__(self, characters):
        self.characters = characters
        self.active_turn = self.characters[0] if random.randint(1,100) % 2 == 0 else self.characters[1]
        self.passive_turn = self.characters[0] if self.active_turn == self.characters[1] else self.characters[1]
        self.round = 0
        self.log = []

        for character in self.characters:
            character.set_game(self)

    def battle(self):
        self.add_log_entry(f"fighting {self.characters[0].name} against {self.characters[1].name}")

        c1 = self.characters[0]
        c2 = self.characters[1]

        while c1.health > 0 and c2.health > 0:
            for turn_time in range(2):
                self.turn()
            self.next_round()

        self.declair_winner()
        
    def turn(self):
        self.active_turn.take_turn(self.passive_turn)

        temp_char = self.active_turn
        self.active_turn = self.passive_turn
        self.passive_turn = temp_char 

    def next_round(self):
        self.add_log_entry("-"*80)
        self.add_log_entry(f"<p class='text-lg font-bold text-center'>End of Round {self.round + 1}</p>")
        for c in self.characters:
            c.show_stats()
        self.add_log_entry("-"*80)
        self.round += 1
        return self

    def add_log_entry(self, message):
        self.log.append(message)
        return self
    
    def declair_winner(self):
        if self.characters[0].health > 0:
            self.add_log_entry(f"<p class='text-2xl font-bold'>{self.characters[0].name} is the winner</p>")
            self.characters[0].add_win()
            self.characters[1].add_lose()
        else:
            self.add_log_entry(f"<p class='text-2xl font-bold'>{self.characters[1].name} is the winner</p>")
            self.characters[1].add_win()
            self.characters[0].add_lose()
        return self
