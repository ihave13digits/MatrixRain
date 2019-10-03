#!/usr/bin/python3

"""
# styles (for white text only)

 1  = bold
 4  = underline
 5  = blink
 7  = highlighted (green)
 8  = light blank
 21 = double underline
 30 = dark blank
 31 = red
 32 = dark green
 33 = yellow
 34 = dark green
 35 = dark blue
 36 = blue
 37 = grey
*38 = white
 41 = bg red
 42 = bg green
 43 = bg yellow
 44 = bg green
 45 = bg dark blue
 46 = bg blue
 47 = bg grey
*48 = bg white
 53 = overline
 58 = bright

"""

text_characters = {#
        'A' : 0, 'a' : 0,
        'B' : 0, 'b' : 0,
        'C' : 0, 'c' : 0,
        'D' : 0, 'd' : 0,
        'E' : 0, 'e' : 0,
        'F' : 0, 'f' : 0,
        'G' : 0, 'g' : 0,
        'H' : 0, 'h' : 0,
        'I' : 0, 'i' : 0,
        'J' : 0, 'j' : 0,
        'K' : 0, 'k' : 0,
        'L' : 0, 'l' : 0,
        'M' : 0, 'm' : 0,
        'N' : 0, 'n' : 0,
        'O' : 0, 'o' : 0,
        'P' : 0, 'p' : 0,
        'Q' : 0, 'q' : 0,
        'R' : 0, 'r' : 0,
        'S' : 0, 's' : 0,
        'T' : 0, 't' : 0,
        'U' : 0, 'u' : 0,
        'V' : 0, 'v' : 0,
        'W' : 0, 'w' : 0,
        'X' : 0, 'x' : 0,
        'Y' : 0, 'y' : 0,
        'Z' : 0, 'z' : 0,
        '0' : 0,
        '1' : 0,
        '2' : 0,
        '3' : 0,
        '4' : 0,
        '5' : 0,
        '6' : 0,
        '7' : 0,
        '8' : 0,
        '9' : 0,
        '`' : 0,
        '~' : 0,
        '!' : 0,
        '@' : 0,
        '#' : 0,
        '$' : 0,
        '%' : 0,
        '^' : 0,
        '&' : 0,
        '*' : 0,
        '(' : 0,
        ')' : 0,
        '-' : 0,
        '_' : 0,
        '=' : 0,
        '+' : 0,
        ',' : 0,
        '.' : 0,
        '<' : 0,
        '>' : 0,
        '/' : 0,
        '?' : 0,
        ';' : 0,
        ':' : 0,
        "'" : 0,
        '"' : 0,
        '[' : 0,
        ']' : 0,
        '{' : 0,
        '}' : 0,
        '|' : 0,
        ' ' : 0,
        '' : 0
        }

menu_data = {
        'bookmark' : 'intro',
        'menu' : 'intro',
        'text_speed' : 0.06,
        'wrap' : 32,
        'r' : 255,
        'g' : 255,
        'b' : 255
        }

menu_color = {
        'white' : {'r' : 255, 'g' : 255, 'b' : 255},
        'grey' : {'r' : 128, 'g' : 128, 'b' : 128},
        'brown' : {'r' : 128, 'g' : 64, 'b' : 32},
        'yellow' : {'r' : 255, 'g' : 255, 'b' : 0},
        'green' : {'r' : 0, 'g' : 128, 'b' : 0},
        'blue' : {'r' : 0, 'g' : 0, 'b' : 255},
        'purple' : {'r' : 128, 'g' : 0, 'b' : 128},
        'red' : {'r' : 255, 'g' : 0, 'b' : 0},
        'orange' : {'r' : 255, 'g' : 128, 'b' : 0}
        }

menu = {# Technical
        'intro' : { # Intro
            'prompt' : 'Title',
            'style' : 5,
            'command' : {
                '1' : {'cmd' : '1', 'menu' : '1-1', 'prompt' : 'New Game'},
                '2' : {'cmd' : '2', 'menu' : 'bookmark', 'prompt' : 'Continue'},
                '3' : {'cmd' : '3', 'menu' : 'settings', 'prompt' : 'Settings'},
                }},
        'data' : { #
            'prompt' : 'Data',
            'style' : 5,
            'command' : {
                '1' : {'cmd' : '1', 'menu' : 'bookmark', 'prompt' : ''},
                '2' : {'cmd' : '2', 'menu' : 'bookmark', 'prompt' : ''},
                '3' : {'cmd' : '3', 'menu' : 'bookmark', 'prompt' : ''},
                '4' : {'cmd' : '4', 'menu' : 'bookmark', 'prompt' : ''},
                '5' : {'cmd' : '5', 'menu' : 'bookmark', 'prompt' : ''},
                '6' : {'cmd' : '6', 'menu' : 'bookmark', 'prompt' : ''},
                '7' : {'cmd' : '7', 'menu' : 'bookmark', 'prompt' : ''},
                '8' : {'cmd' : '8', 'menu' : 'bookmark', 'prompt' : ''},
                '9' : {'cmd' : '9', 'menu' : 'bookmark', 'prompt' : ''},
                '0' : {'cmd' : 'x', 'menu' : 'bookmark', 'prompt' : 'Cancel'}
                }},
        'settings' : { # Settings
            'prompt' : 'Settings',
            'style' : 5,
            'command' : {
                '1' : {'cmd' : '1', 'menu' : 'speed_settings', 'prompt' : 'Text Speed'},
                '2' : {'cmd' : '2', 'menu' : 'color_settings', 'prompt' : 'Text Color'},
                '0' : {'cmd' : '0', 'menu' : 'bookmark', 'prompt' : 'Done'}
                }},
        'color_settings' : { # Color Settings
            'prompt' : 'Text Color Settings',
            'style' : 5,
            'command' : {
                'white' : {'cmd' : 'white', 'menu' : 'settings', 'prompt' : 'White'},
                'grey' : {'cmd' : 'grey', 'menu' : 'settings', 'prompt' : 'Grey'},
                'brown' : {'cmd' : 'brown', 'menu' : 'settings', 'prompt' : 'Brown'},
                'yellow' : {'cmd' : 'yellow', 'menu' : 'settings', 'prompt' : 'Yellow'},
                'green' : {'cmd' : 'green', 'menu' : 'settings', 'prompt' : 'Green'},
                'blue' : {'cmd' : 'blue', 'menu' : 'settings', 'prompt' : 'Blue'},
                'purple' : {'cmd' : 'purple', 'menu' : 'settings', 'prompt' : 'Purple'},
                'red' : {'cmd' : 'red', 'menu' : 'settings', 'prompt' : 'Red'},
                'orange' : {'cmd' : 'orange', 'menu' : 'settings', 'prompt' : 'Orange'}
                }},
        'speed_settings' : { # Speed Settings
            'prompt' : 'Text Speed Settings',
            'style' : 5,
            'command' : {
                '1' : {'cmd' : '1', 'menu' : 'settings', 'prompt' : 'Slowest'},
                '2' : {'cmd' : '2', 'menu' : 'settings', 'prompt' : 'Slow'},
                '3' : {'cmd' : '3', 'menu' : 'settings', 'prompt' : 'Normal'},
                '4' : {'cmd' : '4', 'menu' : 'settings', 'prompt' : 'Fast'},
                '5' : {'cmd' : '5', 'menu' : 'settings', 'prompt' : 'Fastest'}
                }},
        # Story
        '1-1' : { # 
            'prompt' : '',
            'style' : 5,
            'command' : {
                '1' : {'cmd' : '1', 'menu' : '', 'prompt' : ''},
                '2' : {'cmd' : '2', 'menu' : '', 'prompt' : ''},
                '3' : {'cmd' : '3', 'menu' : '', 'prompt' : ''},
                '4' : {'cmd' : '4', 'menu' : '', 'prompt' : ''},
                '5' : {'cmd' : '5', 'menu' : '', 'prompt' : ''},
                '6' : {'cmd' : '6', 'menu' : '', 'prompt' : ''},
                '7' : {'cmd' : '7', 'menu' : '', 'prompt' : ''},
                '8' : {'cmd' : '8', 'menu' : '', 'prompt' : ''},
                '9' : {'cmd' : '9', 'menu' : '', 'prompt' : ''},
                'x' : {'cmd' : 'x', 'menu' : '', 'prompt' : 'Quit'}
                }},
        }
