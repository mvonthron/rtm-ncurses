#!/usr/bin/env python

import os
import time
import curses
import curses.ascii


_x = None
_y = None
width  = None
height = None

def init_colors():
  curses.start_color()
  curses.use_default_colors()
  
  curses.init_pair(1, curses.COLOR_WHITE, -1)
  curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
  curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_CYAN)
  curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN)


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
  win.addstr(0, 1, '(connected) [1] overview [2] work [3] system')

  return win



def make_inputbar():
  """
  Create input bar
  """
  win = curses.newwin(1, curses.COLS, curses.LINES-1, 0)
  
  win.bkgdset(ord(' '), curses.color_pair(1))
  win.insertln()
  win.addstr('[channel] ')
  
  win.nodelay(0)
  win.timeout(0)
  
  curses.curs_set(1)
  
  return win

#
def populate(win):
  global height, width
  del win
  win = make_contentwin(height, 2*width)
  
  text1 = """This is window 1
This is a very very long line roizaeurpoezaiurpzaoieurapoze aprzothqsdkjhfamozierupazoeiur pourh lskfhqs

But not too much

      no?
      
ok then
"""

  text2 = """This is window 2
And another line 

and another...
"""

  #populate 1
  i=0
  for l in text1.split('\n'):
    win.addstr(i, 0, l)
    i += 1
  
  #populate 2
  i=0
  for l in text2.split('\n'):
    win.addstr(i, width, l)
    i += 1
  
  return win

#
def make_contentwin(h, w):
  win = curses.newpad(h, w)
  
  return win
  
def main(stdscr):
  global _x, _y, width, height
  
  init_colors()
  
  _x = 0
  _y = 0
  width  = curses.COLS
  height = curses.LINES-5
  
  # titlebar
  titlebar_win = make_titlebar()
  titlebar_win.refresh()
  
  # content window
  content_win = make_contentwin(height, width)
  content_win.refresh(_y, _x, 1, 0, height-1, width-1)
  
  # statusbar
  statusbar_win = make_statusbar()
  statusbar_win.refresh()
  
  # inputbar
  inputbar_win = make_inputbar()
  inputbar_win.refresh()  
  
  # main input buffer
  input_buffer = ""
  
  while True:
    # move to own thread
    time.sleep(0.01)
    ch = inputbar_win.getch()
    
    if(-1 == ch):
      continue
    elif(curses.ascii.isprint(ch)):
      inputbar_win.addch(chr(ch))
      input_buffer += chr(ch)
    elif ch == curses.KEY_BACKSPACE or ch == curses.ascii.BS or ch == curses.ascii.DEL:
      inputbar_win.delch(inputbar_win.getyx()[0], inputbar_win.getyx()[1]-1)
      input_buffer = input_buffer[:-1]
    elif ch == curses.KEY_UP:
      inputbar_win.addstr("<KEY_UP>")
    elif ch == curses.ascii.DLE:
      inputbar_win.addstr("<DLE>") #CTRL+P
    elif ch == curses.ascii.SO:
      inputbar_win.addstr("<SO>") #CTRL+N
    elif ch == curses.ascii.TAB:
      inputbar_win.addstr("<TAB>")
    elif ch == curses.ascii.NAK:  #CTRL+U
      inputbar_win.addstr("<CTRL+U>")
    elif ch == curses.ascii.ESC:
      inputbar_win.addstr("<ESC>")
    elif ch == curses.ascii.NL or ch == curses.KEY_ENTER:
      inputbar_win.erase()
      inputbar_win.addstr('[channel] ')
      
      if input_buffer == "populate":
        content_win = populate(content_win)
      elif input_buffer == "next":
        _x = width
      elif input_buffer == "prev":
        _x = 0
      else:
        input_buffer += "\n"
        content_win.addstr(input_buffer)
      
      content_win.refresh(_y, _x, 1, 0, height-1, width-1)
      
      input_buffer = ""
    elif curses.ascii.isctrl(ch):
      inputbar_win.addstr("<CTRL> %d [%s]" % (ch, curses.unctrl(ch)))
        
    inputbar_win.refresh()
  
  time.sleep(8)



if __name__ == '__main__':
  curses.wrapper(main)
