#!/usr/bin/env python

import os
import time
import curses



def init_colors():
  curses.start_color()
  curses.use_default_colors()
  
  curses.init_pair(1, curses.COLOR_WHITE, -1)
  curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)


def make_titlebar():
  """
  Create title bar
  
  The title bar has a simple decorative and help purpose
  """
  win = curses.newwin(1, curses.COLS, 0, 0)
  
  win.bkgdset(ord(' '), curses.color_pair(2))
  win.insertln()
  win.addstr(0, 1, 'RTMilk')

  return win
  

def make_statusbar():
  """
  Create status bar
  
  The status bar lists available channels
  """
  win = curses.newwin(1, curses.COLS, curses.LINES-2, 0)
  
  win.bkgdset(ord(' '), curses.color_pair(2))
  win.insertln()
  win.addstr(0, 1, '(status) [1] overview')

  return win



def make_inputbar():
  """
  Create input bar
  """
  win = curses.newwin(1, curses.COLS, curses.LINES-1, 0)
  
  win.bkgdset(ord(' '), curses.color_pair(1))
  win.insertln()
  win.addstr('[channel] ')
  
  win.timeout(0)
  
  curses.curs_set(1)
  
  return win

def make_contentwin():
  win = curses.newwin(curses.LINES-5, curses.COLS, 1, 0)
  
  win.bkgdset(ord(' '), curses.color_pair(1))
  win.insertln()
  win.addstr('< content >')

  return win
  
def main(stdscr):
  init_colors()
  
  # titlebar
  titlebar_win = make_titlebar()
  titlebar_win.refresh()
  
  # content window
  content_win = make_contentwin()
  content_win.refresh()
  
  # statusbar
  statusbar_win = make_statusbar()
  statusbar_win.refresh()
  
  # inputbar
  inputbar_win = make_inputbar()
  inputbar_win.refresh()  
  
  while True:
    # move to own thread
    time.sleep(0.01)
    ch = inputbar_win.getch()
    
    if(-1 == ch):
      continue
      
    inputbar_win.addch(chr(ch))
    inputbar_win.refresh()
  
  time.sleep(8)



if __name__ == '__main__':
  curses.wrapper(main)
