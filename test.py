import keyboard
import time

run = True
moinplus = 0

class Counter:
    def __init__(self):
        self.moinplus = 0

counter = Counter()

def action_clavier(event):
    global run
    if event.name == 'q':
        print('arrêt')
        run = False
    # les actions à réaliser suite à un appui sur une touche
    # .......

# On initialise l'écouteur d'événements clavier (ici : appui sur une touche)
keyboard.on_press(action_clavier)

# Détecter l'appui sur la touche 'a'
keyboard.on_press_key("a", lambda _: decrement())

# Détecter l'appui sur la touche 'z'
keyboard.on_press_key("z", lambda _: increment())

def increment():
    global moinplus
    counter.moinplus += 1
    print(f"moinplus: {counter.moinplus}")

def decrement():
    global moinplus
    counter.moinplus -= 1
    print(f"moinplus: {counter.moinplus}")


while run:
    time.sleep(1)
    # les actions à réaliser périodiquement
    # .......

# On arrête l'écouteur d'événements clavier
keyboard.unhook_all()
