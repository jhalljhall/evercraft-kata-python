from lib.models.Character import Character
from lib.utils.character.Alignment import Alignment
from lib.utils.gameboard.Dice import Dice
from lib.utils.gameboard.DiceType import DiceType
from lib.utils.combat.Attack import Attack
from lib.utils.character.Ability import Ability
from lib.utils.character.AbilityScore import AbilityScore
import unittest

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
    attacker = Character('Hero')
    defender = Character('Enemy')
    dice = Dice(3)
    dice_roll_result = dice.roll()
    am = Attack 
    attackresult = am.attack(attacker, defender, dice_roll_result)
    assert attackresult == False 

def test_dice_twenty():
    attacker = Character('Hero')
    defender = Character('Enemy')
    dice = Dice(20)
    dice_roll_result = dice.roll()
    am = Attack 
    attackresult = am.attack(attacker, defender, dice_roll_result)
    assert attackresult == True

def test_adjust_hit_points():
    attacker = Character('Hero')
    defender = Character('Enemy')
    dice = Dice(11)
    dice_roll_result = dice.roll()
    am = Attack 
    attackresult = am.attack(attacker, defender, dice_roll_result)
    if attackresult == True:
        defender.adjust_hit_points((defender.hit_points - 1))
    assert defender.hit_points == 4

def test_critical_hit():
    attacker = Character('Hero')
    defender = Character('Enemy')
    dice = Dice(20, DiceType.TWENTY)
    dice_roll_result = dice.roll()
    #assume attack power is = 1
    damage = attacker.attack_power
    # is dice.isCritical
    # damage =* 2
    if dice.isCritical == True:
        damage *= 2
    am = Attack 
    attackresult = am.attack(attacker, defender, dice_roll_result)
    if attackresult == True:
        defender.adjust_hit_points((defender.hit_points - damage))
    assert defender.hit_points == 3

def test_is_dead():
    attacker = Character('Hero')
    defender = Character('Enemy')
    dice = Dice(11, DiceType.TWENTY)
    dice_roll_result = dice.roll()
    damage = attacker.attack_power
    while defender.hit_points > 0:
        if dice.isCritical == True:
            damage *= 2
        am = Attack 
        attackresult = am.attack(attacker, defender, dice_roll_result)
        if attackresult == True:
            defender.adjust_hit_points((defender.hit_points - damage))
    assert defender.is_dead() == True


def test_strength_numbers():
    c = Character('Henry')
    assert c.get_abilityscore(Ability.STRENGTH) == 10

def test_dexterity_numbers():
    c = Character('Henry')
    assert c.get_abilityscore(Ability.DEXTERITY) == 10
       
def test_constitution_numbers():
    c = Character('Henry')
    assert c.get_abilityscore(Ability.CONSTITUTION) == 10
      
def test_wisdom_numbers():
    c = Character('Henry')
    assert c.get_abilityscore(Ability.WISDOM) == 10
      
def test_intelligence_numbers():
    c = Character('Henry')
    assert c.get_abilityscore(Ability.INTELLIGENCE) == 10

def test_charisma_numbers():
    c = Character('Henry')
    assert c.get_abilityscore(Ability.CHARISMA) == 10
      
def test_strength_modifiers():
    c = Character('Henry')
    assert c.get_abilitymodifier(Ability.STRENGTH) == 0

def test_dexterity_modifiers():
    c = Character('Henry')
    assert c.get_abilitymodifier(Ability.DEXTERITY) == 0

def test_constitution_modifiers():
    c = Character('Henry')
    assert c.get_abilitymodifier(Ability.CONSTITUTION) == 0

def test_wisdom_modifiers():
    c = Character('Henry')
    assert c.get_abilitymodifier(Ability.WISDOM) == 0

def test_intelligence_modifiers():
    c = Character('Henry')
    assert c.get_abilitymodifier(Ability.INTELLIGENCE) == 0

def test_charisma_modifiers():
    c = Character('Henry')
    assert c.get_abilitymodifier(Ability.CHARISMA) == 0

def test_strength_lowerbound():
    c = Character('Henry')
    assert c.get_abilityscore(Ability.STRENGTH) >= 1

def test_strength_upperbound():
    c = Character('Henry')
    assert c.get_abilityscore(Ability.STRENGTH) <= 20

def test_ability_score_out_of_highrange_exception():
    c = Character('Henry')
    try:
        c.set_abilityscore(Ability.STRENGTH, 21)
    except:
        assert true == true

def test_ability_score_out_of_lowrange_exception():
    c = Character('Henry')
    try:
        c.set_abilityscore(Ability.STRENGTH, 0)
    except:
        assert true == true

def test_modifier_range():
    number = 3
    c = Character('Henry')
    c.set_abilityscore(Ability.STRENGTH, number)
    abscore = AbilityScore(Ability.STRENGTH)
    abscore.score = number
    cscore = c.get_ability(Ability.STRENGTH)
    assert cscore.mod == abscore.mod

def test_strengthModifier_attack():
    attacker = Character('Hero')
    defender = Character('Enemy')
    attacker.set_abilityscore(Ability.STRENGTH, 15)
    dice = Dice(9, DiceType.TWENTY)
    attack_data = {'attacker':attacker, 'defender':defender, 'dice':dice, 'attackAbility':Ability.STRENGTH, 'defendAbility':Ability.DEXTERITY}
    atk = Attack(attack_data)
    
    # if dice.isCritical == True:
    #     am.damage *= 2
    # attackresult = am.attack(attacker, defender, dice_roll_result)
    # if attackresult == True:
    #     defender.adjust_hit_points((defender.hit_points - am.damage))

    assert defender.hit_points == 2

def test_strengthModifier_critical():
    attacker = Character('Hero')
    defender = Character('Enemy')
    attacker.set_abilityscore(Ability.STRENGTH, 15)
    dice = Dice(18, DiceType.TWENTY)
    attack_data = {'attacker':attacker, 'defender':defender, 'dice':dice, 'attackAbility':Ability.STRENGTH, 'defendAbility':Ability.DEXTERITY}
    atk = Attack(attack_data)
    # while defender.hit_points > 0:
    #     if dice.isCritical == True:
    #         am.damage *= 2
    #     attackresult = am.attack(attacker, defender, dice_roll_result)
    #     if attackresult == True:
    #         defender.adjust_hit_points((defender.hit_points - am.damage))
    assert defender.is_dead() == True

def test_strengthModifier_miss():
    attacker = Character('Hero')
    defender = Character('Enemy')
    attacker.set_abilityscore(Ability.STRENGTH, 5)
    dice = Dice(11, DiceType.TWENTY)
    attack_data = {'attacker':attacker, 'defender':defender, 'dice':dice, 'attackAbility':Ability.STRENGTH, 'defendAbility':Ability.DEXTERITY}
    atk = Attack(attack_data)
    
    # if dice.isCritical == True:
    #     am.damage *= 2
    # attackresult = am.attack(attacker, defender, dice_roll_result)
    # if attackresult == True:
    #     defender.adjust_hit_points((defender.hit_points - am.damage))

    assert defender.hit_points == 5

    def test_strengthModifier_miss():
    attacker = Character('Hero')
    defender = Character('Enemy')
    attacker.set_abilityscore(Ability.STRENGTH, 5)
    dice = Dice(12, DiceType.TWENTY)
    attack_data = {'attacker':attacker, 'defender':defender, 'dice':dice, 'attackAbility':Ability.STRENGTH, 'defendAbility':Ability.DEXTERITY}
    atk = Attack(attack_data)
    
    # if dice.isCritical == True:
    #     am.damage *= 2
    # attackresult = am.attack(attacker, defender, dice_roll_result)
    # if attackresult == True:
    #     defender.adjust_hit_points((defender.hit_points - am.damage))

    assert defender.hit_points == 4