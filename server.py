from flask import Flask, render_template, session, request, redirect
# app = instance of Flask (class)
app = Flask(__name__)   
app.secret_key = "shhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh, don't tell anyone ... i am here"

from models import character
from models import game

FAKE_DB = {
        'characters': [],
        'standoff': []
    }

CHARACTER_TYPES = {
        'Human': character.Human,
        'Elf': character.Elf,
        'Orc': character.Orc,
        'Halfling': character.Halfling,
        'Dwarf': character.Dwarf,
        'Gnome': character.Gnome,
        'HalfElf': character.HalfElf,
        'Tiefling': character.Tiefling,
        'Dragonborn': character.Dragonborn,
    }

# THIS WILL MOVE!!!
# *******************************  PAGES
@app.route('/')
def hello_world():
    if 'characters' in FAKE_DB:
        for c in FAKE_DB['characters']:
            c.reset()
    return render_template('index.html', FAKE_DB=FAKE_DB)

@app.route("/character")
def character_show():
    if 'data' not in session:
        return redirect('/')
    return render_template('character_show.html')

@app.route("/display/fight")
def display_fight():
    if 'game' not in FAKE_DB:
        return redirect('/')
    return render_template("fight.html", FAKE_DB=FAKE_DB)

# *******************************  CHARACTERS
@app.route("/character/new")
def character_new():
    return render_template("character_create.html", FAKE_DB=FAKE_DB, race_types=CHARACTER_TYPES)

@app.route("/character/create", methods=['POST'])
def character_create():
    
    data = {
        **request.form,
        'likes': int(request.form['likes'])
    }

    character_obj = CHARACTER_TYPES[data['race']](data)
    FAKE_DB['characters'].append(character_obj)

    # redirect to a display route 
    return redirect("/")

@app.route("/standoff/character/add/<int:index>")
def standoff_character_add(index):
    if len(FAKE_DB['standoff']) < 2:
        character = FAKE_DB['characters'].pop(index)
        FAKE_DB['standoff'].append(character)
    return redirect("/")

@app.route("/standoff/character/remove/<int:index>")
def standoff_character_remove(index):
    character = FAKE_DB['standoff'].pop(index)
    FAKE_DB['characters'] = [character] + FAKE_DB['characters']
    return redirect("/")

@app.route("/standoff/character/unload")
def standoff_character_unload():
    for c in FAKE_DB['standoff']:
        FAKE_DB['characters'].append(c)
    FAKE_DB['standoff'].clear()
    return redirect("/")

@app.route("/character/likes")
@app.route("/character/likes/<int:num>")
def character_likes(num=1):
    if 'data' not in session:
        return redirect('/')

    session_copy = session['data']
    session_copy['likes'] += num
    session['data'] = session_copy

    return redirect('/character')


# *******************************  FIGHT

@app.route("/fight")
def fight():
    new_game = game.Game(FAKE_DB['standoff'])
    new_game.battle()
    FAKE_DB['game'] = new_game
    return redirect('/display/fight')

# *******************************  DATABASE
@app.route("/database/save")
def database_save():
    characters_list = []
    for c in FAKE_DB['characters']:
        attributes = c.__dict__
        if 'game' in attributes:
            attributes.pop('game')
        print(attributes)
        characters_list.append(attributes)
    session['characters'] = characters_list
    return redirect('/')

@app.route('/database/load')
def database_load():
    if 'characters' in session:
        characters = session['characters']
        FAKE_DB['characters'].clear()
        for c in characters:
            character_obj = CHARACTER_TYPES[c['race']](c)
            FAKE_DB['characters'].append(character_obj)
    else:
        print("No characters found")
    return redirect('/')

@app.route("/database/reset")
def database_reset():
    FAKE_DB.clear()
    FAKE_DB['characters'] = []
    FAKE_DB['standoff'] = []
    default_characters = [
    {
        "name": "Tyler",
        "race": "Human",
        "backstory": "Tyler grew up in a small village, known for its bountiful farmlands. He had an insatiable curiosity and yearned for adventure beyond the village's borders. Determined to explore the vast world, Tyler left his home and embarked on a journey to discover new lands, face formidable challenges, and find his place in history.",
        "has_hat": "No",
        "likes": 0
    },
    {
        "name": "Elara",
        "race": "Elf",
        "backstory": "Elara was raised in the mystical forests of Eldoria. She was trained in the ancient arts of magic by her elven mentors, becoming a skilled spellcaster. Her bond with nature runs deep, and she acts as a protector of the forest, defending it against any threats. Elara wears a hat adorned with magical symbols, which enhances her shel_hasting abilities.",
        "has_hat": "Yes",
        "likes": 0
    },
    {
        "name": "Durin",
        "race": "Dwarf",
        "backstory": "Durin hails from a long line of expert miners and blacksmiths. He was trained in the family's forge from a young age, mastering the art of crafting weapons and armor. Durin's exceptional strength and resilience make him a formidable warrior. He wears a sturdy, broad-brimmed hat to shield his eyes from the sparks and heat of the fhrg_h",
        "has_hat": "Yes",
        "likes": 0
    },
    {
        "name": "Milo",
        "race": "Halfling",
        "backstory": "Milo is a nimble and mischievous halfling who grew up in a bustling city. His small stature and quick reflexes made him a natural thief, adept at sneaking and picking locks. However, Milo has a heart of gold and only steals from the rich and corrupt to help the less fortunate. He doesn't wear a hat, as it might hinder his nimble mhve_hnts.",
        "has_hat": "No",
        "likes": 0
    },
    {
        "name": "Glim",
        "race": "Gnome",
        "backstory": "Glim is a curious and inventive gnome, always tinkering with gadgets and contraptions. Known as a brilliant inventor, Glim has a hat with hidden compartments where he keeps his miniature tools and mechanical devices. His goal is to create something groundbreaking that will be remembered throughout history. Glim's insatiable chri_hity often gets him into trouble, but his quick thinking helps him overcome any obstacles.",
        "has_hat": "Yes",
        "likes": 0
    },
    {
        "name": "Aric",
        "race": "HalfElf",
        "backstory": "Aric is a diplomat with a dual heritage, born to an elven mother and a human father. He grew up in a world where tensions between elves and humans persist. Aric's unique background grants him the ability to bridge gaps between different cultures and mediate conflicts. He doesn't wear a hat, as he believes in openness and transparency.",
        "has_hat": "No",
        "likes": 0
    },
    {
        "name": "Grunk",
        "race": "Orc",
        "backstory": "Grunk was once a savage warrior, feared by many for his brute strength. However, an encounter with a wise old hermit changed his path. The hermit taught Grunk about honor, redemption, and the power of compassion. Since then, Grunk has devoted himself to protecting the innocent and righting past wrongs. Grunk's hat was given to him by the hermit as a symbol of his newfound purpose.",
        "has_hat": "No",
        "likes": 0
    },
    {
        "name": "Lilith",
        "race": "Tiefling",
        "backstory": "Lilith carries a burden that comes with her infernal bloodline. Cursed from birth, she struggles to control her demonic powers. Lilith's hat is adorned with protective runes to help her suppress and channel her chaotic magic. She seeks to understand the origins of her infernal heritage and find a way to break the curse that hhun_h her existence.",
        "has_hat": "Yes",
        "likes": 0
    },
    {
        "name": "Drakar",
        "race": "Dragonborn",
        "backstory": "Drakar was born with the power of dragons flowing through his veins. Raised by a council of wise dragonborn elders, he was trained to harness and control his fiery breath and scales. Drakar's hat resembles the head of a dragon, symbolizing his connection to the ancient draconic lineage. He dreams of uncovering the lost knowledge oh h_h kind.",
        "has_hat": "Yes",
        "likes": 0
    }
]
    for item in default_characters:
        character_obj = CHARACTER_TYPES[item['race']](item)
        FAKE_DB['characters'].append(character_obj)
    return redirect('/')


# end of moving content

# MAKE SURE THIS IS AT THE BOTTOM
if __name__=="__main__":
    app.run(debug=True)