import random

class Character:

    def __init__(self, data):
        self.name = data['name']
        self.race = data['race']
        self.backstory = data['backstory']
        self.has_hat = data['has_hat']
        self.likes = data['likes']
        self.wins = 0
        self.losses = 0

        self.health = data['health']
        self.original_health = data['health']
        self.strength = data['strength']
        self.speed = data['speed']
        self.game = None

    def show_stats(self):
        self.game.add_log_entry(f"<p class='font-bold'>{self.name}</p>")
        self.game.add_log_entry(f"Health: {self.health}")
        return self
    
    def add_win(self):
        self.wins += 1
        return self
    
    def add_lose(self):
        self.losses += 1
        return self

    def set_game(self, game):
        self.game = game
        return self

    def take_turn(self, target):
        self.game.add_log_entry(f"{self.name}'s turn")
        self.attack(target)
        return self

    def attack(self, target):
        damage_amount = random.randint(0, self.strength)
        if damage_amount == 0:
            self.game.add_log_entry(f"<p class='text-red-500 font-bold'>{self.name} completely missed! {target.name} gets an extra turn!</p>")
            target.attack(self)
            return self
        
        potential_dodge = target.dodge(self)
        if not potential_dodge:
            self.game.add_log_entry(f"{target.name} took {damage_amount} damage")
            target.modify_health(-damage_amount)
        else:
            self.game.add_log_entry(f"<p class='text-orange-500'>{target.name} dodged the attack by {self.name}</p>")
        return self
        
    def dodge(self, target):
        dodge_chance = random.randint(0, 20)
        if dodge_chance <= self.speed:
            return True
        return False

    def modify_health(self, amount):
        self.health += amount

        return self
    
    def reset(self):
        self.health = self.original_health

class Human (Character):
    def __init__(self, data):
        self.img = "https://cdn.leonardo.ai/users/b9f351fc-1769-4fb3-9ede-a73db26291eb/generations/9f6c358e-1932-49cf-a9ca-a5690f8d8f9f/variations/Default_DD_Human_0_9f6c358e-1932-49cf-a9ca-a5690f8d8f9f_1.jpg"
        data['health'] = random.randint(90, 110)
        data['strength'] = random.randint(8,13)
        data['speed'] = random.randint(8, 11)
        super().__init__(data)

class Orc (Character):
    def __init__(self, data):
        self.img = "https://cdn.leonardo.ai/users/b9f351fc-1769-4fb3-9ede-a73db26291eb/generations/de86f84c-e340-45a2-a74c-feec6d6c2058/variations/Default_DD_Orc_3_de86f84c-e340-45a2-a74c-feec6d6c2058_1.jpg?w=512"
        data['health'] = random.randint(98, 105)
        data['strength'] = random.randint(10,13)
        data['speed'] = random.randint(3, 6)
        super().__init__(data)

class Elf (Character):
    def __init__(self, data):
        self.img = "https://cdn.leonardo.ai/users/b9f351fc-1769-4fb3-9ede-a73db26291eb/generations/332f73f3-79c4-4d25-b072-4891b5806fa1/variations/Default_DD_Elf_0_332f73f3-79c4-4d25-b072-4891b5806fa1_1.jpg?w=512"
        data['health'] = random.randint(100, 110)
        data['strength'] = random.randint(8,10)
        data['speed'] = random.randint(10, 15)
        super().__init__(data)

class Dwarf (Character):
    def __init__(self, data):
        self.img = "https://cdn.leonardo.ai/users/b9f351fc-1769-4fb3-9ede-a73db26291eb/generations/4a5324ea-da39-45a5-a50d-305b0d5c40a7/variations/Default_DD_Dwarf_3_4a5324ea-da39-45a5-a50d-305b0d5c40a7_1.jpg"
        data['health'] = random.randint(120, 150)
        data['strength'] = random.randint(10,12)
        data['speed'] = random.randint(1,3)
        super().__init__(data)

class Gnome (Character):
    def __init__(self, data):
        self.img = "https://cdn.leonardo.ai/users/b9f351fc-1769-4fb3-9ede-a73db26291eb/generations/678ad265-cb8b-4d65-81a5-ee9cacaffec8/variations/Default_DD_Gnome_realistic_3_678ad265-cb8b-4d65-81a5-ee9cacaffec8_1.jpg?w=512"
        data['health'] = random.randint(50, 80)
        data['strength'] = random.randint(8,10)
        data['speed'] = random.randint(15, 20)
        super().__init__(data)

class HalfElf (Character):
    def __init__(self, data):
        self.img = "https://cdn.leonardo.ai/users/b9f351fc-1769-4fb3-9ede-a73db26291eb/generations/59341743-a01a-4c94-97b5-ba0f057785ac/variations/Default_DD_HalfElf_human_2_59341743-a01a-4c94-97b5-ba0f057785ac_1.jpg?w=512"
        data['health'] = random.randint(100, 105)
        data['strength'] = random.randint(10,12)
        data['speed'] = random.randint(10, 12)
        super().__init__(data)

class Tiefling (Character):
    def __init__(self, data):
        self.img = "https://cdn.leonardo.ai/users/b9f351fc-1769-4fb3-9ede-a73db26291eb/generations/3ee8f53f-7d7b-4d04-a2f2-d666dbc44081/variations/Default_DD_Tiefling_1_3ee8f53f-7d7b-4d04-a2f2-d666dbc44081_1.jpg?w=512"
        data['health'] = random.randint(85, 103)
        data['strength'] = random.randint(8,13)
        data['speed'] = random.randint(6, 13)
        super().__init__(data)

class Dragonborn (Character):
    def __init__(self, data):
        self.img = "https://cdn.leonardo.ai/users/b9f351fc-1769-4fb3-9ede-a73db26291eb/generations/d0e5d734-ffb7-44da-8b64-5a35b7f41f52/variations/Default_DD_Dragonborn_2_d0e5d734-ffb7-44da-8b64-5a35b7f41f52_1.jpg?w=512"
        data['health'] = random.randint(93, 107)
        data['strength'] = random.randint(8,14)
        data['speed'] = random.randint(6, 15)
        super().__init__(data)

class Halfling (Character):
    def __init__(self, data):
        self.img = "https://cdn.leonardo.ai/users/b9f351fc-1769-4fb3-9ede-a73db26291eb/generations/26e8b7e3-769c-4074-8e99-33ed072f5508/variations/Default_DD_Halfling_realistic_3_26e8b7e3-769c-4074-8e99-33ed072f5508_1.jpg?w=512"
        data['health'] = random.randint(80, 90)
        data['strength'] = random.randint(8,10)
        data['speed'] = random.randint(14, 19)
        super().__init__(data)