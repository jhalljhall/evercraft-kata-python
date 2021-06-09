from lib.models.Character import Character
from lib.utils.Alignment import Alignment
from lib.utils.Dice import Dice
from lib.utils.Attack import Attack

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

def test_dice_exists():
    dice = Dice
    assert dice

def test_dice_roll():
    dice = Dice(15)
    dice_roll_result = dice.roll()
    assert dice_roll_result == 15

def test_hit_result():
    hero = Character('Hero')
    enemy = Charcter('Enemy')
    dice = Dice(3)
    dice_roll_result = dice.roll()
    am = Attack 
    attackresult = am.attack(attacker, defender, dice_roll_result)
    assert attackresult == false 

def test_dice_twenty():
    hero = Character('Hero')
    enemy = Charcter('Enemy')
    dice = Dice(20)
    dice_roll_result = dice.roll()
    am = Attack 
    attackresult = am.attack(attacker, defender, dice_roll_result)
    assert attackresult == true 
