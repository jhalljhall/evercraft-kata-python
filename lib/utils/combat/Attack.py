
class Attack:

    def attack(attacker, defender, dice_roll_result):
        attack_result = False
        
        if dice_roll_result == 20:
            attack_result = True
            return attack_result

        if defender.armor_class <= dice_roll_result:
            attack_result = True
            return attack_result 

        return attack_result 