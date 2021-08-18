#Mark Boady and Matthew Burlick
#Drexel University 2020
#CS 172


import random
import time

## TODO: import CustomMonster class here
from monster import CustomMonster
def driver():
	## TODO: Get first monster's name, health, description, basicAttackDamange, specialAttackDamage, defenseDamage, defenseName here.
    # Instantiate a CustomMonster using that info.
    monName1 = input("Enter monster 1 name:")
    monHealth1 = int(input("\nEnter a number for monster 1 health:"))
    description1 = input("\nEnter monster 1 description:")
    basNum1 = int(input("\nEnter a number for monster 1 basic attack damage:"))
    speNum1 = int(input("\nEnter a number for monster 1 special attack damage:"))
    defNum1 = int(input("\nEnter a number for monster 1 defense damage:"))
    basAtt1 = input("\nEnter monster 1 basic attack name:")
    speAtt1 = input("\nEnter monster 1 special attack name:")
    defAtt1 = input("\nEnter monster 1 defense name:")
    first = CustomMonster(monName1, monHealth1, description1, basNum1, speNum1, defNum1, basAtt1, speAtt1, defAtt1)
    #this should be an instance of your CustomMonster class

# TODO: Get second monster's name, health, description, basicAttackDamange, specialAttackDamage, defenseDamage, defenseName here.
    # Instantiate a CustomMonster using that info.
    monName2 = input("Enter monster 2 name:")
    monHealth2 = int(input("\nEnter a number for monster 2 health:"))
    description2 = input("\nEnter monster 2 description:")
    basNum2 = int(input("\nEnter a number for monster 2 basic attack damage:"))
    speNum2 = int(input("\nEnter a number for monster 2 special attack damage:"))
    defNum2 = int(input("\nEnter a number for monster 2 defense damage:"))
    basAtt2 = input("\nEnter monster 2 basic attack name:")
    speAtt2 = input("\nEnter monster 2 special attack name:")
    defAtt2 = input("\nEnter monster 2 defense name:")
    second = CustomMonster(monName2, monHealth2, description2, basNum2, speNum2, defNum2, basAtt2, speAtt2, defAtt2)
    #this should be an instance of your CustomMonster class

    winner = monster_battle(first, second)
    #this should be an instance of your CustomMonster class




#This function has two monsters fight and returns the winner
def monster_battle(m1, m2):

    #first reset everyone's health!
    #####TODO######
    m1.resetHealth()
    m2.resetHealth()
    #next print out who is battling
    print("Starting Battle Between")
    print(m1.getName()+": "+m1.getDescription())
    print(m2.getName()+": "+m2.getDescription())


    #Whose turn is it?
    attacker = None
    defender = None

    #Select Randomly whether m1 or m2 is the initial attacker
    #to other is the initial definder
    ######TODO######
    selectPlayer = random.choice([1,2])
    if selectPlayer == 1:
        attacker = m1
        defender = m2
    else:
        attacker = m2
        defender = m1

    print(attacker.getName()+" goes first.")
    #Loop until either monster is unconscious (health < 1) or choose to stop.
    while( m1.getHealth() > 0 and m2.getHealth() > 0):
        #Ask the user a move among special attack, basic attack, defense or the stop.
        move = input('Pick one of these (s)pecial attack, (b)asic attack, (d)efense or sto(p):')

        #It will be nice for output to record the damage done
        before_health=defender.getHealth()

        #for each of the options above, apply the appropriate attack and
        #print out who did what attack on whom
        #basic attack
        if( move.lower() == "b"):
            # Attacker uses basic attack on defender
            # and print results by calling print_results function
            ######TODO######
            attacker.basicAttack(defender)
            print('{} used {} on {}'.format(attacker.getName(), attacker.getBasicName(), defender.getName()))
            print('The attack did {} damage.'.format(attacker.getBasicAttackDamage()))
        #defense attack
        elif move.lower() == "d":
            # Defend! and print results by calling print_results function
            ######TODO######
            attacker.defenseAttack(defender)
            print('{} used {} on {}'.format(attacker.getName(), attacker.getDefenseName(), defender.getName()))
            print('The attack did {} damage.'.format(attacker.getDefenseAttackDamage()))
        #special attack
        elif move.lower() == "s":
            # Special Attack! and print results by calling print_results function
            ######TODO######
            attacker.specialAttack(defender)
            print('{} used {} on {}'.format(attacker.getName(), attacker.getSpecialName(), defender.getName()))
            print('The attack did {} damage.'.format(attacker.getSpecialAttackDamage()))
        elif move.lower() == 'p':
            break

        print('{} at {}'.format(attacker.getName(), attacker.getHealth()))
        print('{} at {}'.format(defender.getName(), defender.getHealth()))
        switch = attacker
        attacker = defender
        defender = switch
            #stop the fight


        #Swap attacker and defender
        #switch = attacker
        #attacker = defender
        #defender = switch
        #Print the names and healths after this round
        ######TODO######

        #if attacker.getHealth() < 0:
            #attacker.setHealth(0)
        #elif defender.getHealth() < 0:
            #defender.setHealth(0)

        #print()

    # Print out who won.
    # Return who won
    #print('Battle is over. let\'s see who has won...')
    ######TODO######
    if attacker.getHealth() > defender.getHealth():
        print('\nBattle is over. let\'s see who has won...')
        print('{} is victorious!'.format(attacker.getName()))
    else:
        print('\nBattle is over. let\'s see who has won...')
        print('{} is victorious!'.format(defender.getName()))

#Print status updates
####TODO####


def print_results(attacker,defender,attack,hchange):
    ####TODO####
    # Get the name of the attacker and the defender.
    # then give status updates based on the the attack. For more
    # info refer to the example trace.
    attackerName = attacker.getName()
    defenderName = defender.getName()
    res = str(hchange)

    print("{} used {} on {}".format(attackerName, attack, defenderName))
    print("The attack did {} damage.".format(res))

#----------------------------------------------------
if __name__=="__main__":
    #Ideally ever battle will be different
    #But for reproducability, we'll seed the random number generator as 0

    random.seed(0)
    driver()