#!usr/bin/python3

import random

from digits_engine import *

class Matrix():

    def random_char(low=0xFF66, high=0xFF9D):
        char = random.randint(int(low), int(high))
        return chr(char)

    def stream(l, x=0, y=0):
        stream = {
                't' : 0.0,
                's' : random.randint(1, 4),
                'x' : x,
                'y' : y,
                'chars' : []
                }
        for i in range(l):
            stream['chars'].append(Matrix.random_char())

        return stream

    def regulate(maximum=0):
        if maximum == 0:
            maximum = DISPLAY['data']['width']*2
        else:
            maximum = maximum
        if len(SPRITES) < maximum:
            while len(SPRITES) < maximum:
                SPRITES.append(Matrix.stream(random.randint(0, int(DISPLAY['data']['height']/4))+4, x=random.randint(0, DISPLAY['data']['width'])))
        elif len(SPRITES) > maximum:
            while len(SPRITES) > maximum:
                SPRITES.pop()
        else:
            pass

    def update():
        for s in SPRITES:
            for i, c in enumerate(s['chars']):
                if i > 0:
                    Display.draw(s['x'], s['y']-i, 0, int(255/s['s'])-i*int((255/s['s'])/len(s['chars'])), 0, c)
                else:
                    Display.draw(s['x'], s['y']-i, int(128/s['s']), int(255/s['s']), int(128/s['s']), c)
            if s['t'] >= s['s']:
                s['y'] += 1
                s['t'] = 0
            s['t'] += 1
        for s in SPRITES:
            if int(s['y'] - len(s['chars'])) >= DISPLAY['data']['height']:
                SPRITES.remove(s)
