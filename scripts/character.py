import os


class Character:

    health = 10
    power = 2
    defense = 1

    items = []

    def __init__(self, name):
        self.name = name

    def hello(self):
        return f'Hello, I am {self.name} the ruthless!'

    def attack(self, enemy):
        damage = (self.power - enemy.defense)
        enemy.health = enemy.health - damage
        print(f'{self.name} attacks {enemy.name}!')
        print(f'Andres deals {damage} to {enemy.name}...')
        print(f'{enemy.name} has {enemy.health} remaining health.')


andres = Character('Andres')
enemy = Character('Evil Man')
