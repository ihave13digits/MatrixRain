#!/usr/bin/python3

# Terminengine by digits version 0.1.2019.6

import os, sys, time, textwrap

from project_menu import *
from project_var import *

game_folder = os.path.dirname(__file__)

clear_cmd = ''

if sys.platform.startswith('win32'):
    clear_cmd = 'cls'
else:
    clear_cmd = 'clear'

try:
    os.mkdir(os.path.join(game_folder, 'data'))
    data_folder = os.path.join(game_folder, 'data')
    os.mkdir(os.path.join(data_folder, 'save'))
    save_folder = os.path.join(data_folder, 'save')
except FileExistsError:
    data_folder = os.path.join(game_folder, 'data')
    save_folder = os.path.join(data_folder, 'save')

class Data:

    def menu():
        wrapped_txt = str('\n'.join(textwrap.wrap(menu[menu_data['menu']]['prompt'], menu_data['wrap'], break_long_words=False)))
        for c in wrapped_txt:
            sys.stdout.write("\x1b[{};2;{};{};{}m".format(menu[menu_data['menu']]['style'], menu_data['r'], menu_data['g'], menu_data['b']) + c + '\x1b[0m')
            sys.stdout.flush()
            time.sleep(menu_data['text_speed'])
        print("\n"* margin)
        print("(1) Save")
        print("(2) Load")
        print("(3) Name")
        print("(0) Back")
        sel = input(": ")
        Text.clear()
        if sel == "1":
            Data.select_save(mode='s')
        if sel == "2":
            Data.select_save(mode='l')
        if sel == "3":
            Data.select_save(mode='n')
        if sel == "0":
            pass

    def select_save(mode=''):
        Data.loadsaves()
        wrapped_txt = str('\n'.join(textwrap.wrap(menu[menu_data['menu']]['prompt'], menu_data['wrap'], break_long_words=False)))
        for c in wrapped_txt:
            sys.stdout.write("\x1b[{};2;{};{};{}m".format(menu[menu_data['menu']]['style'], menu_data['r'], menu_data['g'], menu_data['b']) + c + '\x1b[0m')
            sys.stdout.flush()
            time.sleep(menu_data['text_speed'])
        print("(1) {}".format(SAVE['data']['1']))
        print("(2) {}".format(SAVE['data']['2']))
        print("(3) {}".format(SAVE['data']['3']))
        print("(4) {}".format(SAVE['data']['4']))
        print("(5) {}".format(SAVE['data']['5']))
        print("(6) {}".format(SAVE['data']['6']))
        print("(7) {}".format(SAVE['data']['7']))
        print("(8) {}".format(SAVE['data']['8']))
        print("(9) {}".format(SAVE['data']['9']))
        sel = input(": ")
        Text.clear()
        if sel == "1":
            save = '1'
        if sel == "2":
            save = '2'
        if sel == "3":
            save = '3'
        if sel == "4":
            save = '4'
        if sel == "5":
            save = '5'
        if sel == "6":
            save = '6'
        if sel == "7":
            save = '7'
        if sel == "8":
            save = '8'
        if sel == "9":
            save = '9'
        else:
            if SAVE['data']['current_save_slot'] != '':
                save = SAVE['data']['current_save_slot']

        if mode == 's':
            try:
                os.mkdir(path.join(save_folder, save))
            except FileExistsError:
                pass
            Text.stream("Saving Data", spd=0, end='', clr='b')
            Text.stream("...", spd=0.09, dly=.5/0.09, clr='a')
            for save_data in SAVE_DATA:
                Data.save(save, save_data)
            Data.name(save)
            Data.savesaves()
            SAVE['data']['current_save_slot'] = save

        if mode == 'l':
            for save_data in SAVE_DATA:
                Data.load(save, save_data, quick=True)

            SAVE['data']['current_save_slot'] = save

        if mode == 'n':
            Data.name(save)

    def name(save):
        if SAVE['data'][save] == '':
            print("Enter Save Tag")
            SAVE['data'][save] = input(": ")
            #input()
            Text.clear()
        elif SAVE['data'][save] != '':
            print("Rename Save Tag? Y/N")
            sel = input(": ").lower()
            Text.clear()
            if sel == "y":
                print("Enter New Save Tag")
                SAVE['data'][save] = input(": ")
                #input()
                os.system(clear_cmd)
            if sel == "n":
                pass

    def save(save, target, quick=False):
        if quick == False:
            Text.stream("Saving Data", spd=0, end='', clr='b')
            Text.stream("...", spd=0.09, dly=.5/0.09, clr='a')

        os.chdir(save_folder)
        with open(os.path.join(save, target['file']), 'w') as f:
            if target['type'] == 'dict':
                for data in target['data']:
                    if target['data'][data]['type'] == 'list':
                        for l in target['data'][data]['data']['data']:
                            for value in target['data'][data]['data']['data'][l]:
                                f.write(str(value)+"|")
                            f.write("\n")
                    else:
                        for d in target['data'][data]['data']:
                            f.write(str(target['data'][data]['data'][d]))
                            f.write("\n")
            else:
                if target['type'] == 'list':
                    for L in target['data']['data']:
                        for l in target['data']['data'][L]:
                            f.write(str(l)+"|")
                        f.write("\n")
                else:
                    for data in target['data']:
                        f.write(str(target['data'][data]))
                        f.write("\n")
        os.chdir(game_folder)

    def load(save, target, quick=False):
        try:
            if quick == False:
                Text.stream("Loading Data", spd=0, end='', clr='b')
                Text.stream("...", spd=0.09, dly=.5/0.09, clr='a')

            os.chdir(save_folder)
            with open(os.path.join(save, target['file']), 'r') as f:
                if target['type'] == 'dict':
                    for data in target['data']:
                        if target['data'][data]['type'] == 'list':
                            for d in target['data'][data]['data']['data']:
                                line = f.readline().strip()
                                temp_data = ''
                                x = 0
                                for l in line:
                                    if l != "|":
                                        temp_data += l
                                    else:
                                        if target['data'][data]['data']['type'] == 'str':
                                            target['data'][data]['data']['data'][d][x] = str(temp_data)
                                        if target['data'][data]['data']['type'] == 'int':
                                            target['data'][data]['data']['data'][d][x] = int(temp_data)
                                        x += 1
                                        temp_data = ''
                        else:
                            for attribute in target['data'][data]['data']:
                                if target['data'][data]['type'] == 'str':
                                    target['data'][data]['data'][attribute] = str(f.readline().strip())
                                if target['data'][data]['type'] == 'bool':
                                    target['data'][data]['data'][attribute] = bool(f.readline().strip())
                                if target['data'][data]['type'] == 'int':
                                    target['data'][data]['data'][attribute] = int(f.readline().strip())
                                if target['data'][data]['type'] == 'float':
                                    target['data'][data]['data'][attribute] = float(f.readline().strip())
                else:
                    if target['type'] == 'list':
                        for data in target['data']['data']:
                            line = f.readline().strip()
                            temp_data = ''
                            x = 0
                            for l in line:
                                if l != "|":
                                    temp_data += l
                                else:
                                    if target['data']['type'] == 'str':
                                        target['data']['data'][data][x] = str(temp_data)
                                    if target['data']['type'] == 'int':
                                        target['data']['data'][data][x] = int(temp_data)
                                    x += 1
                                    temp_data = ''
                    else:
                        for data in target['data']:
                            if target['type'] == 'str':
                                target['data'][data] = str(f.readline().strip())
                            if target['type'] == 'int':
                                target['data'][data] = int(f.readline().strip())
                            if target['type'] == 'float':
                                target['data'][data] = float(f.readline().strip())
                            if target['type'] == 'bool':
                                target['data'][data] = bool(f.readline().strip())

                f.close()
            os.chdir(game_folder)
        except FileNotFoundError:
            print("No Data")

    def savesaves():
        os.chdir(save_folder)
        for x in range(1, 9):
            try:
                with open(os.path.join('{}'.format(str(x).strip()), SAVE['file']), 'w') as f:
                    for data in SAVE['data']:
                        f.write(str(SAVE['data'][data]))
                        f.write('\n')
            except FileNotFoundError:
                pass
        os.chdir(game_folder)

    def loadsaves():
        os.chdir(save_folder)
        for x in range(1, 9):
            try:
                with open(os.path.join('{}'.format(str(x).strip()), SAVE['file']), 'r') as f:
                    for data in SAVE['data']:
                        SAVE['data'][data] = str(f.readline().strip())

                    f.close()
            except FileNotFoundError:
                pass
        os.chdir(game_folder)

class Menu():

    def data(save, mode):
        os.chdir(save_folder)
        with open(save, mode) as f:
            if mode == "w":
                for key in menu_data:
                    f.write(str(menu_data[key]))
                    f.write("\n")

            if mode == "r":
                menu_data['bookmark'] = str(f.readline().strip())
                menu_data['menu'] = str(f.readline().strip())
                menu_data['text_speed'] = float(f.readline().strip())
                menu_data['wrap'] = int(f.readline().strip())
                menu_data['r'] = int(f.readline().strip())
                menu_data['g'] = int(f.readline().strip())
                menu_data['b'] = int(f.readline().strip())
        os.chdir(game_folder)

    def menu(M, margin=3):
        wrapped_txt = str('\n'.join(textwrap.wrap(menu[menu_data['menu']]['prompt'], menu_data['wrap'], break_long_words=False)))
        for c in wrapped_txt:
            sys.stdout.write("\x1b[{};2;{};{};{}m".format(menu[menu_data['menu']]['style'], menu_data['r'], menu_data['g'], menu_data['b']) + c + '\x1b[0m')
            sys.stdout.flush()
            time.sleep(menu_data['text_speed'])
        print("\n"* margin)
        for m in menu[menu_data['menu']]['command']:
            print("({}) {}".format(
                menu[menu_data['menu']]['command'][m]['cmd'],
                menu[menu_data['menu']]['command'][m]['prompt']))
        sel = input(": ")
        os.system(clear_cmd)
        if sel == "x":
            Menu.data("data.txt", "w")
            STATE['running'] = False
        try:
            if menu_data['menu'] == "speed_settings":
                if sel == "1":
                    menu_data['text_speed'] = 0.12
                if sel == "2":
                    menu_data['text_speed'] = 0.09
                if sel == "3":
                    menu_data['text_speed'] = 0.06
                if sel == "4":
                    menu_data['text_speed'] = 0.03
                if sel == "5":
                    menu_data['text_speed'] = 0.01
            if menu_data['menu'] == "color_settings":
                    menu_data['r'] = menu_color[sel]['r']
                    menu_data['g'] = menu_color[sel]['g']
                    menu_data['b'] = menu_color[sel]['b']
            if menu_data['menu'] == "intro":
                if sel == "2":
                    menu_data['menu'] = menu_data['bookmark']
            if menu[menu_data['menu']]['command'][sel]['menu'] == "bookmark":
                menu_data['menu'] = menu_data['bookmark']
            if sel == "home":
                menu_data['menu'] = "intro"
            if sel == "settings" or sel == "options":
                menu_data['menu'] = "settings"
            else:
                if menu[menu_data['menu']]['command'][sel]['menu'] != "bookmark":
                    menu_data['menu'] = menu[menu_data['menu']]['command'][sel]['menu']
                if menu_data['menu'] != "intro" and menu_data['menu'] != "settings" and menu_data['menu'] != "speed_settings" and menu_data['menu'] != "color_settings":
                    menu_data['bookmark'] = menu[menu_data['menu']]['command'][sel]['menu']
        except KeyError:
            pass
        Menu.data("data.txt", "w")

class Text:

    def clear():
        os.system(clear_cmd)

    def count_chars(txt):
        for char in txt:
            if char in text_characters:
                text_characters[char] += 1
            else:
                text_characters[''] += 1

    def show_chars(char=""):
        if char == "":
            return text_characters
        else:
            return text_characters[char]

    def clear_char_count():
        for char in text_characters:
            text_characters[char] = 0

    def crypt(txt, key=47, mode='e'):
        chars = "a0Z1b2Y3c4X5d6W7e8V9f`U~g,T.h?S!i@R#j$Q%k^P&l*O-m=N_n+M(o)L{p}K[q]J<r>I;s:H/t'G\"u|F vEwDxCyBzA"
        cypher = ""
        for c in txt:
            if c in chars:
                if mode == "e":
                    character = (chars.find(c) + key) % 94
                if mode == "d":
                    character = (chars.find(c) - key) % 94
                cypher += chars[character]
            else:
                cypher += c
        return cypher

    def stream(text_file, r=menu_data['r'], g=menu_data['g'], b=menu_data['b'], FBG=0, spd=menu_data['text_speed'], dly=0, hdr='', hdr_m=1, end='', end_x=1, clr=''):
        if '.txt' in text_file:
            with open(text_file, 'r') as txt:
                if dly == 0:
                    if clr == 'b':
                        os.system(clear_cmd)
                    if clr == 'b+a':
                        os.system(clear_cmd)
                    if hdr != '':
                        print(hdr + '\n' * hdr_m)
                    for char in txt:
                        for c in char:
                            sys.stdout.write("\x1b[{};2;{};{};{}m".format(FBG, r, g, b) + c + '\x1b[0m')
                            sys.stdout.flush()
                            time.sleep(spd)
                    if clr == 'a':
                        os.system(clear_cmd)
                    if clr == 'b+a':
                        os.system(clear_cmd)
                    print(end * end_x, end='')

                if dly > 0:
                    delay = spd * dly
                    if clr == 'b':
                        os.system(clear_cmd)
                    if clr == 'b+a':
                        os.system(clear_cmd)
                    if hdr != '':
                        print(hdr + '\n' * hdr_m)
                    for char in txt:
                        for c in char:
                            sys.stdout.write("\x1b[{};2;{};{};{}m".format(FBG, r, g, b) + c + '\x1b[0m')
                            sys.stdout.flush()
                            time.sleep(spd)
                    print(end * end_x, end='')
                    time.sleep(delay)
                    if clr == 'a':
                        os.system(clear_cmd)
                    if clr == 'b+a':
                        os.system(clear_cmd)
        else:
            if dly == 0:
                if clr == 'b':
                    os.system(clear_cmd)
                if clr == 'b+a':
                    os.system(clear_cmd)
                if hdr != '':
                    print(hdr + '\n' * hdr_m)
                for c in text_file:
                    sys.stdout.write("\x1b[{};2;{};{};{}m".format(FBG, r, g, b) + c + '\x1b[0m')
                    sys.stdout.flush()
                    time.sleep(spd)
                if clr == 'a':
                    os.system(clear_cmd)
                if clr == 'b+a':
                    os.system(clear_cmd)
                print(end * end_x, end='')

            if dly > 0:
                delay = spd * dly
                if clr == 'b':
                    os.system(clear_cmd)
                if clr == 'b+a':
                    os.system(clear_cmd)
                if hdr != '':
                    print(hdr + '\n' * hdr_m)
                for c in text_file:
                    sys.stdout.write("\x1b[{};2;{};{};{}m".format(FBG, r, g, b) + c + '\x1b[0m')
                    sys.stdout.flush()
                    time.sleep(spd)
                print(end * end_x, end='')
                time.sleep(delay)
                if clr == 'a':
                    os.system(clear_cmd)
                if clr == 'b+a':
                    os.system(clear_cmd)

class Event():

    def get_fps():
        return TIME['data']['fps']

    def elapsed_time():
        return TIME['data']['elapsed_time']

    def wall_time():
        return time.time()

    def clock():
        TIME['data']['tick'] += 1/TIME['data']['target_fps']
        time.sleep(1/TIME['data']['target_fps'])
        TIME['data']['elapsed_time'] += 1/TIME['data']['target_fps']

    def get_key():
        os.system("stty raw -echo")
        c = sys.stdin.read(1)
        os.system("stty -raw echo")
        return c

class Display:

    def get_console_size():
        numbers = ['1','2','3','4','5','6','7','8','9','0']
        x, y, t = '', '', 0
        line = str(os.get_terminal_size())

        for c in line:
            if c == "=":
                t += 1
            for n in numbers:
                if c == n:
                    if t == 1:
                        x += c
                    if t == 2:
                        y += c

        return int(x), int(y)

    def display():
        pixel = [TEXT['data']['list']['data']['data']['background'][0],
                TEXT['data']['list']['data']['data']['background'][1],
                TEXT['data']['list']['data']['data']['background'][2],
                TEXT['data']['list']['data']['data']['background'][3]]
        for y in range(DISPLAY['data']['height']):
            for x in range(DISPLAY['data']['width']):
                key = '{}-{}'.format(x,y)
                screen_buffer[key] = pixel

    def get_pixel(x, y):
        pixel = screen_buffer['{}-{}'.format(x, y)]
        R = pixel[0]
        G = pixel[1]
        B = pixel[2]
        C = pixel[3]
        return R, G, B, C

    def draw(x, y, r, g, b, c):
        screen_buffer['{}-{}'.format(x, y)] = [r, g, b, c]

    def render(pxl='', margin=0, end=''):
        Text.clear()
        pixels = ['░░', '▒▒', '▓▓', '██']
        if pxl == '':
            pxl = pixels[DISPLAY['data']['brightness']]
        for y in range(DISPLAY['data']['height']):
            for x in range(DISPLAY['data']['width']):
                r, g, b, pxl = Display.get_pixel(x, y)
                sys.stdout.write("\x1b[{};2;{};{};{}m".format(38, r, g, b) + pxl + '\x1b[0m')
            print(end)
        if end != "":
            print("\n"*margin)
