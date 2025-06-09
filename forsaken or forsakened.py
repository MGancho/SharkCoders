from random import randint
from time import sleep
Noob_strength = 2
Noob_intelligence = 3
Noob_stamina = 5

_007n7_strength = 1
_007n7_intelligence = 4
_007n7_stamina = 5
_007n7_health = 1

Shedletsky_strength = 4
Shedletsky_intelligence = 3
Shedletsky_stamina = 3
Shedletsky_health = 1

Guest_1337_strength = 5
Guest_1337_intelligence = 1
Guest_1337_stamina = 4

Chance_strength = randint(1,5)
Chance_intelligence = randint(1,5)
Chance_stamina = randint(1,5)

Two_Time_strength = 5
Two_Time_intelligence = 3
Two_Time_stamina = 2

Elliot_strength = 0
Elliot_intelligence = 6
Elliot_stamina = 4

Dusekkar_strength = 1
Dusekkar_intelligence = 7
Dusekkar_stamina = 2

Taph_strength = 2
Taph_intelligence = 6
Taph_stamina = 2

Builderman_strength = 1
Builderman_intelligence = 8
Builderman_stamina = 1

Total_Strength = Noob_strength + _007n7_strength + Shedletsky_strength + Guest_1337_strength + Chance_strength + Two_Time_strength + Elliot_strength + Dusekkar_strength + Taph_strength + Builderman_strength
Total_Intelligence = Noob_intelligence + _007n7_intelligence + Shedletsky_intelligence + Guest_1337_intelligence + Chance_intelligence + Two_Time_intelligence + Elliot_intelligence + Dusekkar_intelligence + Taph_intelligence + Builderman_intelligence
Total_Stamina = Noob_stamina + _007n7_stamina + Shedletsky_stamina + Guest_1337_stamina + Chance_stamina + Two_Time_stamina + Elliot_stamina + Dusekkar_stamina + Taph_stamina + Builderman_stamina
Escolha = input("START GAME? yes | no : ")
Escolha = Escolha.capitalize()
if Escolha == "No":
    sleep(0.5)
    print("ok, whenever you want to start, tell me")
elif Escolha == "Yes":
    sleep(0.5)
    print("Let's do this")
    sleep(0.5)
    print("you were trapped by an entity called 'The spectre'")
    sleep(2)
    print("He tortures people for fun, and he is know to be merciless")
    sleep(2.75)
    print("you and your colleagues are going to enter the limbo")
    sleep(2)
    print("and the reward of entering and gettin out is freedom ")
    sleep(1.75)
    print("The people who are going with you are:")
    sleep(1.5)
    print("Jack - yourself")
    sleep(1.5)
    print("007n7 - hacker who literally made chaos")
    sleep(3)
    print("Shedletsky - your best friend")
    sleep(2)
    print("Guest - a war veteran")
    sleep(1.5)
    print("Chance - a gambler")
    sleep(1.5)
    print("Two Time - killer who sacrificed his best friend for his cult (the respawn)")
    sleep(3.5)
    print("Elliot - Chef who we do not know how the hell he ended up there")
    sleep(3.5)
    print("Dusekkar - A wizard")
    sleep(1.5)
    print("Taph - A bomber who cannot speak")
    sleep(1.5)
    print("Builderman - the creator of the creature")
    sleep(2)
    print("But someone has to be left behind, to make sure the plan does not raise suspicion")
    sleep(2)
    f1 = input("Who will it be? ")
    f1 = f1.capitalize()
    match f1:
        case "Jack":
            print("you decided to be left behind")
            sleep(1.5)
            print("For the best of them")
            sleep(1.5)
            print("But HE sees you and he wants you to tell him where they are")
            sleep(1.5)
            final1_2 = input("Will you snitch yes | no : ")
            final1_2 = final1_2.capitalize()
            if final1_2 == "Yes":
                sleep(1.5)
                print("You decided to tell the truth")
                sleep(1.5)
                print("So as a reward you are free")
                sleep(1.5)
                print("But you are forced to see your friends die")
                sleep(1.5)
                print("while they know you snitched on them")
                sleep(1.5)
                print("Ending 1: The snitch - you won, but at what cost")
            elif final1_2 == "No":
                sleep(1.5)
                print("You decided to lie")
                sleep(1.5)
                print("Although he respects your decision of not telling where they went")
                sleep(1.5)
                print("He decides to kill you for trying to trick him ")
                sleep(1.5)
                print("Ending 2: Heroic ending - you sacrificed yourself to help others. Because of that, you are honoured and remembered")
        case "007n7":
            Total_Stamina -= _007n7_stamina
            Total_Strength -= _007n7_strength
            Total_Intelligence -= _007n7_intelligence
        case "Shedletsky":
            Total_Stamina -= Shedletsky_stamina
            Total_Strength -= Shedletsky_strength
            Total_Intelligence -= Shedletsky_intelligence
        case "Guest":
            Total_Stamina -= Guest_1337_stamina
            Total_Strength -= Guest_1337_strength
            Total_Intelligence -= Guest_1337_intelligence
        case "Chance":
            Total_Stamina -= Chance_stamina
            Total_Strength -= Chance_strength
            Total_Intelligence -= Chance_intelligence
        case "Two Time":
            Total_Stamina -= Two_Time_stamina
            Total_Strength -= Two_Time_strength
            Total_Intelligence -= Two_Time_intelligence
        case "Elliot":
            Total_Stamina -= Elliot_stamina
            Total_Strength -= Elliot_strength
            Total_Intelligence -= Elliot_intelligence
        case "Dusekkar":
            Total_Stamina -= Dusekkar_stamina
            Total_Strength -= Dusekkar_strength
            Total_Intelligence -= Dusekkar_intelligence
        case "Taph":
            Total_Stamina -= Taph_stamina
            Total_Strength -= Taph_strength
            Total_Intelligence -= Taph_intelligence
        case "Builderman":
            Total_Stamina -= Builderman_stamina
            Total_Strength -= Builderman_strength
            Total_Intelligence -= Builderman_intelligence
