from foo.bar import bar
from lib.models import Character

# def test_my_bar():
#     assert bar() == "foobar"

def test_set_character_name():
    c = Character
    c.set_name('Bob Ross')
    assert c.get_name() == 'Bob Ross'