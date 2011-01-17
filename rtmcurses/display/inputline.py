# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

import curses
import curses.ascii
import time
import threading

class InputLine(threading.Thread):
  
  stopflag = False
  
  # input buffer
  input_buffer = ""
  
  def __init__(self):
    """
    Create input bar
    """
    self.win = curses.newwin(1, curses.COLS, curses.LINES-1, 0)
    
    self.win.bkgdset(ord(' '), curses.color_pair(1))
    self.win.insertln()
    self.win.addstr('[channel] ')
    
    self.win.nodelay(0)
    self.win.timeout(0)
    
    curses.curs_set(1)
    self.win.refresh()


  def listen(self):
    """main listening routine
    listen to char entered by user with getch()
    """
    
    while not self.stopflag:
      time.sleep(0.01)
      ch = self.win.getch()
      
      if(-1 != ch):
        buffer = self.handle(ch)
        if buffer:
          return buffer
    
  
  def handle(self, ch):
    need_refresh = False
    
    if ord('q') == ch:
      self.stop()
    
    if curses.ascii.isprint(ch):      
      self.win.addch(chr(ch))
      self.input_buffer+= chr(ch)
      need_refresh = True
    elif ch == curses.ascii.NAK:  #CTRL+U
      self.win.erase()
      self.input_buffer = ""
      need_refresh = True
    elif ch == curses.ascii.NL or ch == curses.KEY_ENTER:
      return self.input_buffer
      
    if need_refresh:
      self.win.refresh()

  def stop(self):
    self.stopflag = True
