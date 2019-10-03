#!/usr/bin/python3

import os, sys, time, textwrap

from digits_engine import *
from project_menu import *
from project_var import *

from matrix import *

timeout = 60
start_time = Event.wall_time()

class Engine():

    def event():
        #sel = Event.get_key()
        #if sel == "x":
        t = Event.wall_time()
        TIME['data']['elapsed_time'] = t-start_time
        if TIME['data']['elapsed_time'] >= timeout:
            exit()

    def update():
        if STATE['text'] == True:
            Menu.data("data.txt", "r")
            Menu.menu(menu_data['menu'])
        if STATE['explore'] == True:
            x, y = Display.get_console_size()
            DISPLAY['data']['width'] = x
            DISPLAY['data']['height'] = y
            Display.display()
            Engine.event()
            Matrix.regulate()
            Matrix.update()
            Display.render(end='')

    def start():
        Display.display()
        try:
            os.system('clear')
            Engine.run()
        except FileNotFoundError:
            Menu.data("data.txt", "w")
            Engine.run()

    def run():
        while STATE['running'] == True:
            Event.clock()
            if TIME['data']['tick'] >= 1/TIME['data']['target_fps']:
                TIME['data']['tick'] -= 1/TIME['data']['target_fps']
                Engine.update()
                print("Time Left: {} Strings: {} Screen Dimesions(x, y): {}, {}".format(int(timeout-(Event.wall_time()-start_time)), len(SPRITES),
                    DISPLAY['data']['width'], DISPLAY['data']['height']))

Engine.start()
