from os import system
from random import randint

gametitle= "The Dungeons- An Adventure Game"
system("mode 110,30")       #size of window.
system("title" +gametitle)  #title of window.

# function to clear screen.
def cls():
    system('cls')

#declaring global variables
hero_name = None
hero_race = None
hero_class = None
hero_strength = None
hero_magic =  None
hero_life = None
hero_dexterity = None

cls()       #clearing the whole screen before commencing.
print("THE DUNGEONS- AN ADVENTURE GAME!")
#introduction to game story
def Intro():
     print(" ")
     print("Welcome to the dungeons! You are our hero.")
     print("")
     print("Your choices, skills and a bit of luck will influence the outcome of this game.")
     print(" ")
     print("An evil monster is holding innocent travellers prisoners.")
     print("Will you be able to free them or will you perish trying?")
     print(" ")
     input("Press enter to start...")

Intro()

#setting values for character
def hero():
    cls()
    global hero_name
    hero_name=input("""
    Let's begin by creating your character!
    What is your character's name?
    
    >   """)
    print("   Hello! "+""+hero_name+":D")
    global hero_race
    while hero_race is None:
        race_choice=input("""
        Choose your character race from the list below by entering a valid number!
        1.Elf
        2.Dwarf
         
        
        > """)
        if race_choice=="1":
            hero_race= "Elf"
        elif race_choice=="2":
            hero_race= "Dwarf"
        else:
            print("not a valid choice, try again! :(")
    cls()
    global hero_class
    while hero_class is None:
        class_choice = input("""
        Choose your character class from the list below by entering a valid number
        1. Soldier
        2. Wizard

        >""")
        if class_choice=="1":
            hero_class="Soldier"
        elif class_choice=="2":
            hero_class="Wizard"
        else:
            print("Not a valid choice, try again! :(")
hero()



def create_skillsheet():
    cls()
    global hero_name, hero_race, hero_dexterity, hero_life, hero_magic,hero_strength, hero_class
    print("""
        Now let's decide your character's skill sets, which you will use throughout the game.
        In this game, your character has 4 skills:

        -Strength, which you will use in combat or any strength test
        -Dexterity, which you will use in any ability test
        -Magic, which you will use whenever you need to cast a spell or use/inspect a magical item or place
        -Life, which determines your life energy, points will be losy when hurt,
             and whenever life reaches 0, your character dies.

        Depending on your race and class, you will have a certain point-base already calculated by the game.
        You will shortyly be able to increase your skills by rolling a 6-face die.


    Here is your base Character Skills Sheet:
    """)
    #setting base values for all characters.
    hero_strength=5
    hero_magic=0
    hero_dexterity=3
    hero_life=10

    if hero_race== "Elf":
        hero_strength = hero_strength+3
        hero_dexterity = hero_dexterity + 3
        hero_magic = hero_magic + 6
        hero_life =hero_life+2
    elif hero_race == "Dwarf":
        hero_strength = hero_strength + 5
        hero_dexterity = hero_dexterity + 2
        hero_life =hero_life+4

    if hero_race == "Wizard":
        hero_magic = hero_magic + 4

    elif hero_race == "Soldier":
        hero_strength =hero_strength + 3
        hero_life = hero_life+3

    print("""
    Name: """+hero_name+
    """
    Race: """+hero_race+
    """
    Class: """+hero_class+
    """

    Strength: """+str(hero_strength)+
    """
    Dexterity: """+str(hero_dexterity)+
    """
    Magic: """+str(hero_magic)+
    """
    Life: """ +str(hero_life)+
    """

    """)
    input("Press Enter to apply your skills modifiers:")

create_skillsheet()

def modify():
    cls()
    global hero_strength,hero_magic, hero_dexterity, hero_life
    print("To modify your skills, roll a six face die for each of your skills, and the game will add your score to the relevant skill")
    input("Press Enter to roll for Strength")
    roll=randint(1,6)
    print("You rolled: "+ str(roll))
    hero_strength = hero_strength + roll
    input("Press Enter to roll for Dexterity")
    roll=randint(1,6)
    print("You rolled: "+ str(roll))
    hero_dexterity = hero_dexterity + roll
    input("Press Enter to roll for life")
    roll= randint(1,6)
    print("You rolled: "+ str(roll))
    hero_life = hero_life + roll

    input("Press Enter to continue...")
    cls()
    print("""

    Congratulations!! Your character is now ready!
    Your final character sheet is:

    Name:"""+hero_name+
    """
    Race:"""+hero_race+
    """
    Class:"""+hero_class+
    """

    Strength:"""+str(hero_strength)+
    """
    Dexterity:"""+str(hero_dexterity)+
    """
    Magic:"""+str(hero_magic)+
    """
    Life:"""+str(hero_life)+
    """

    """)
    print("It is finally quest time!")
    input("Press Enter to save the travellers, if you dare...")

modify()


def Scene_1():
    cls()
    choice = None  
    while choice is None:
        user_input=input("""
    You have entered the secret dungeon...
    It is dark, however thankfully your torch is lit and you can see upto 20ft infront of you.
    The dungeon alley is scattered with bones of shape that you don't recognize,
    you can smell the dampness of the wall mixed with a scent you can't quite figure.
    You walk down the narrow alley, until you reach a dead end.

    The alley continues on the left, and on the right.

        What do you do?

        1.Turn Left
        2.Turn Right
    >""")

        if user_input=="1" or user_input=="turn left":
            choice="1"
            Scene2()
        elif user_input=="2" or user_input=="turn right":
            choice="2"
            Scene3()
        else: print("""
            Not a valid choice, type a number or "turn left" / "turn right"
            """)

def Scene2():
    cls()
    choice= None
    while choice is None:
        user_input=input("""
    From the darkness behind you.. you hear a loud, strange noise.

    What do you do?

    1 - Continue walking
    2 - Stop to listen

    > """)
        if user_input=="1" or user_input=="continue":
            choice="1"
            combat()
        elif user_input=="2" or user_input=="stop":
            choice="2"
            analyze()
        else:
            print("""
            Not a valid choice, type a number or "continue" / "stop"
            """)

def Scene3():
    cls()
    choice= None
    while choice is None:
        user_input=input("""
    From the darkness behind you.. you hear a strange noise.

    What do you do?

    1 - Continue walking
    2 - Stop to listen

    > """)
        if user_input=="1" or user_input=="continue":
            choice="1"
            combat()
        elif user_input=="2" or user_input=="stop":
            choice="2"
            analyze()
        else:
            print("""
            Not a valid choice, type a number or "continue" / "stop"
            """)


def analyze():
    cls()
    print("A giant rock falls from the ceiling, roll a die to see if you can dodge it.. or you will be crashed by it!")
    roll=randint(1,6)
    print("You rolled: "+str(roll))
    if roll+hero_dexterity > 10:
        print ("""
        You dodge the stone and survive! Danger is not over though..
        The strange noise in the darkness continues, and it feels a lot closer now..""")
        input("Press Enter to continue...")
        combat()
        
    else:
        print("You are smashed by the rock.. You die. The game is over.")
        input("Press Enter to exit the game.")


def combat():
    cls()
    global hero_life
    print("Your life: "+str(hero_life))
    print("A horrible Lich attacks you!")
    input("Press Enter to combat...")
    lich = [10, 14]                              #make a list containing strenght and life of the Lich.
    while lich[1] > 0 or hero_life > 0: 
        char_roll=randint(1,6)
        print("You rolled: "+str(char_roll))
        monst_roll=randint(1,6)
        print("The monster rolled: "+str(monst_roll))
        if char_roll+hero_strength >= monst_roll+lich[0]:
            print("You hit the monster!")
            lich[1] = lich[1] - randint(1,6)
        else: 
            print("The monster hits you!")
            hero_life = hero_life - randint (1,6)
            
    if hero_life>0:
        print("You defeated the Lich, congratulations!!")
        input("press enter to continue..")
        Scene4()
        
    else:
        print("You lost.. your friends will never be freed.. and you're dead.")
        input("Press Enter to exit the game")

Scene_1()


def Scene4():
    cls()
    choice = None  
    while choice is None:
        user_input=input("""
    You sucessfully defeated the Lich!
    What's that sound???
    It sounds like the travellers screaming for help! Quick! You need to save them!

    
    LOOK, ITS THE MONSTER...what is that? Is that a...Demogorgon?!?

        What will you do?

        1.Fight it
        2.Tread Carefully
    >""")

        if user_input=="1" or user_input=="turn left":
            choice="1"
            fight()
        elif user_input=="2" or user_input=="turn right":
            choice="2"
            think()
        else: print("""
            Not a valid choice, type a number or "fight it" / "tread carefully"
            """)
def think():
    cls()
    print("The Demogorgon is quite strong. Do you think you have what it takes to defeat him?")
    roll=randint(1,6)
    print("You rolled: "+str(roll))
    if roll+hero_strength > 10:
        if roll+hero_magic>3:
            print ("""
            Let's take on this Monster and save the travellers!!! """)
            input("Press Enter to continue...")
            fight()
        else:
            print("You are crushed by the Demogorgon. The game is over.")
            input("Press Enter to exit the game.")

def fight():
    cls()
    global hero_life
    print("The Demogorgon has seen you! It's heading towards you.")
    input("Press Enter to fight...")
    dem = [10, 14]
    while dem[1] > 0 or hero_life > 0: 
        new_roll=randint(1,6)
        print("You rolled: "+str(new_roll))
        dem_roll=randint(1,6)
        print("The monster rolled: "+str(dem_roll))
        if new_roll+hero_strength >= dem_roll+dem[0]:
            print("You hit the monster!")
            dem[1] = dem[1] - randint(1,6)
            printf("Monster's life: "+ dem[1])
        else: 
            print("The Demogorgon hits you!")
            hero_life = hero_life - randint (1,6)
            print("Your life: "+ str(hero_life))
    if hero_life>0:
        print("You defeated the Demogorgon, congratulations!!")
        print(" ")
        print("You freed the travellers!! GOOD JOB!")
        input("Press Enter to exit")
    else:
        print("You lost.. your friends will never be freed.. and you're dead.")
        input("Press Enter to exit the game")


