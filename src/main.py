from config import console
import time

import curses

screen = curses.initscr()
console.init()

print(curses.termname())

left = curses.newwin(10, 10, 0, 0)
right = curses.newwin(10, 10, 0, 10)
left.border()
right.box()

#left.addstr(' '*99, curses.A_REVERSE)
#right.addstr('.'*99, curses.COLOR_RED)

left.refresh()
right.refresh()

console.screen.refresh()

time.sleep(1)

console.close()

'''
console.init()

print(console.get_size())
for i in range(5):
    print(console.get_input())


console.close()
'''
