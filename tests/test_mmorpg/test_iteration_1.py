from lib.models.Character import Character

def test_set_character_name():
    c = Character
    c.set_name('Bob Ross')
    assert c.get_name() == 'Bob Ross'

# def test_set_character_name():
#     c = Character
#     c.name = 'Bob Ross'
#     assert c.name == 'Bob Ross'