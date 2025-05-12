from time import sleep
from random import randint
time = 10
num_secret = randint(1, 10)
name = input("what is your name?")
print("initiating mission Mars")
sleep(2)
print("propellors ready")
sleep(1)
print("initiating launch")
button_press = int(input(f" {name} , are you ready to be the first peon to step foot on mars? yes: 0 | no: 1 "))
if button_press == 0:
    while time != 0:
        print(time)
        sleep(1)
        time -= 1
    if time == 0:
        print("Blast off!")
    sleep(10)
    print(f"mission sucessful. Well Done {name}, you are the first person to step foot on Mars. Congratulations! ")
    sleep(1)
    print("Good ending :D")
    print("You went to mars and you are remembered as a markable person in human history")
elif button_press == 1:
    print(f"it's okay to not do it {name}, you do not need to be the first person to do something.")
    sleep(1)
    print("You can go relax to your place")
    sleep(1)
    print("Afraid ending :|")
    sleep(0.5)
    print("You did not went to mars and you are remembered as the one who backed of the plan because you were scared")
else:
    print("|SYSTEM ERR0R| You pushed a GIANT button with the word |self-destruct| ")
    sleep(2)
    print("THE ROCKET IS GOING TO EXPLODE")
    sleep(1)
    decision = input("GUESS THE CODE T0 GET TO SAFETY!!! (between 1 and 10)")
    if decision == num_secret:
        print(f"you guessed the code and you, aswell as the others got out of the ship")
        sleep(2)
        print(f"Bad ending :[")
        sleep(0.5)
        print("you are remembered as the person who slowed the process to go to mars")
    else:
        print("you did not guessed the code and you, aswell the others got killed in the explosion ")
        sleep(1)
        print("You are a Dumbass ending lol")
        sleep(0.5)
        print("you are remembered as a villain who did not want humanity to go to mars")