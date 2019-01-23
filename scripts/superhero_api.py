import os
import requests
import json
import pandas as pd
from pprint import pprint


def heroname(name):

    print('Fetching Data...')
    r = requests.get('https://superheroapi.com/api.php/10162110525735377/search/' + name)
    print(F'Response Status: {r.status_code}')

    hero = r.json()

    pprint(hero)

def heroid(id):

    print('Fetching Data...')
    r = requests.get('https://superheroapi.com/api.php/10162110525735377/' + id)
    print(F'Response Status: {r.status_code}')

    hero = r.json()

    pprint(hero)
