from microbit import *

# State
# 0 - coffee, 1 - choose card, 2 - wait for shake, 3 - display card
state = 0


def nextState():
    global state
    state = (state + 1) % 4
    return


# Cards
cards = [0, 1, 2, 3, 5, 8, 13, 20, 40, 100]
currentCard = 0


def animateCard():
    string = str(cards[currentCard])
    stringLen = len(string)
    if (stringLen == 1):
        display.show(string)
    else:
        display.scroll(string)
    return


# Coffee
image_coffee_1 = Image("00500:05000:99999:90099:09900")
image_coffee_2 = Image("05000:00500:99999:90099:09900")
coffee_images = [image_coffee_1, image_coffee_2]
currentCoffee = 0


def animateCoffee():
    global currentCoffee
    display.show(coffee_images[currentCoffee])
    currentCoffee = currentCoffee + 1
    currentCoffee = currentCoffee % 2
    sleep(500)
    return


# Program
def was_button_pressed():
    pressed = 0
    if (button_a.was_pressed()):
        pressed = pressed + 1
    if (button_b.was_pressed()):
        pressed = pressed + 2
    return pressed


while True:
    pressed = was_button_pressed()
    if pressed == 3:
        nextState()
    else:
        if state == 0:
            animateCoffee()
        elif state == 1:
            if pressed == 1:
                currentCard = currentCard - 1
                if currentCard < 0:
                    currentCard = len(cards) - 1
            elif pressed == 2:
                currentCard = currentCard + 1
                if currentCard == len(cards):
                    currentCard = 0
            animateCard()
        elif state == 2:
            if accelerometer.was_gesture("shake"):
                nextState()
            else:
                display.show(Image.DIAMOND)
        elif state == 3:
            animateCard()
