#!/usr/bin/env python

import os
import time
import curses



def init_colors():
  curses.start_color()
  curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
  curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)


def make_statusbar():
  win = curses.newwin(1, curses.COLS, curses.LINES-2, 0)
  
  win.bkgdset(ord(' '), curses.color_pair(2))
  win.insertln()
  win.addstr('blah')

  return win


def main(stdscr):
  init_colors()
  
  statusbar_win = make_statusbar()
  statusbar_win.refresh()
  
  time.sleep(5)



if __name__ == '__main__':
  curses.wrapper(main)
