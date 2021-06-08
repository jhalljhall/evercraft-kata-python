from lib.models.Character import Character
from lib.utils.Alignment import Alignment

def test_set_character_name():
    c = Character
    c.set_name('Bob Ross')
    assert c.get_name() == 'Bob Ross'

def test_create_character():
    c = Character('Bob Ross')
    assert c.get_name() == 'Bob Ross'

def test_set_alignment():
    c = Character('Bob Ross')
    c.set_alignment(Alignment.NEUTRAL)
    assert c.alignment == Alignment.NEUTRAL

def test_character_alignment():
    c = Character('Bob Ross', Alignment.NEUTRAL)
    assert c.alignment == Alignment.NEUTRAL

def test_armor_class():
    c = Character('Bob Ross')
    assert c.get_armor_class() == 10

def test_hit_points():
    c = Character('Bob Ross')
    assert c.get_hit_points() == 5
