#!/usr/bin/python3

STATE = {
        'running' : True,
        'paused' : False,
        'text' : False,
        'explore' : True
        }

TEXT = {
        'file' : 'text_settings.txt',
        'type' : 'dict',
        'data' : {
            'int' : {
                'type' : 'int',
                'data' : {
                    '' : 0
                    }},
            'float' : {
                'type' : 'float',
                'data' : {
                    'spd' : 0.06,
                    'dly' : 0.0
                    }},
            'list' : {
                'type' : 'list',
                'data' : {
                    'type' : 'int',
                    'data' : {
                    'player_clr' : [255, 255, 255, ' '],
                    'text_clr' : [128, 128, 128, ' '],
                    'background' : [0, 0, 0, ' ']
                    }}}
            }
        }

TIME = {
    'file' : 'time.txt',
    'type' : 'float',
    'data' : {
        'target_fps' : 20.0,
        'fps' : 0.0,
        'tick' : 0.0,
        'elapsed_time' : 0.0
        }
    }

SAVE = {
    'file' : 'saves.txt',
    'type' : 'str',
    'data' : {#
        'current_save_slot' : '',
        '1' : '',
        '2' : '',
        '3' : '',
        '4' : '',
        '5' : '',
        '6' : '',
        '7' : '',
        '8' : '',
        '9' : ''
        }
    }

DISPLAY = {
        'file' : 'display.txt',
        'type' : 'int',
        'data' : {
            'brightness' : 3,
            'width' : 80,
            'height' : 24,
            'x' : 16,
            'y' : 16
            }
        }

SPRITES = []

screen_buffer = {}

SAVE_DATA = [SAVE, TEXT, DISPLAY]
