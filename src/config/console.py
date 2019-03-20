import os
import sys
import termios
import tty

import curses


global screen
screen = None

def check_init(f, *args, **kwargs):
    global screen
    def ret(*args, **kwargs):
        if screen == None:
            raise Exception("console not initialized. Call console.init() beforhand")
        return f(*args, **kwargs)
    return ret

def init():
    global screen
    screen = curses.initscr()
    curses.def_prog_mode()
    curses.noecho()
    screen.keypad(True)


@check_init
def close():
    global screen
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    curses.endwin()



def get_size():
    """
        gets and gives console dimention

        Return: (int rows, int columns)
    """
    return os.popen('stty size', 'r').read().split()

@check_init
def set_cursor(line, column):
    """
        sets cursor on given position

        Return: None
    """
    global screen
    screen.move(line, column)

@check_init
def get_input():
    global screen
    screen.refresh()
    return screen.getch()
