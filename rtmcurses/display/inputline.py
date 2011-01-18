# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

import curses
import curses.ascii
import time
import threading
from collections import deque


class InputLine(object):
  
  stopflag = False
  
  # input buffer
  input_buffer = ""
  
  inputline_prefix = ""
  
  def __init__(self):
    """
    Create input bar
    """
    MAX_HISTORY_SIZE = 20
    self.history = deque(maxlen=MAX_HISTORY_SIZE)
    self._history_index = MAX_HISTORY_SIZE-1
    
    # win
    self.win = curses.newwin(1, curses.COLS, curses.LINES-1, 0)
    
    self.win.bkgdset(ord(' '), curses.color_pair(1))
    self.win.insertln()
    self.clear()
    
    self.win.nodelay(0)
    self.win.timeout(0)
    
    curses.curs_set(1)
    self.win.refresh()


  def listen(self):
    """main listening routine
    listen to char entered by user with getch()
    """
    self.input_buffer = ""
    self.clear()
    
    while not self.stopflag:
      time.sleep(0.01)
      ch = self.win.getch()
      
      if(-1 != ch):
        buffer = self.handle(ch)
        if buffer:
          return buffer
    
  
  def handle(self, ch):
    if curses.ascii.isprint(ch):
      self.append_ch(chr(ch))

    elif ch == curses.KEY_BACKSPACE or ch == curses.ascii.BS or ch == curses.ascii.DEL:
      if self.win.getyx()[1] <= len(self.inputline_prefix):
        return 
      
      self.win.delch(self.win.getyx()[0], self.win.getyx()[1]-1)
      self.input_buffer = self.input_buffer[:-1]

    elif ch == curses.ascii.NAK:  #CTRL+U
      self.input_buffer = ""
      self.clear()
    
    elif ch == curses.KEY_UP or ch == curses.ascii.DLE:
      self.append("<history>")
      #self.println(self.history[self._history_index])
      #self._history_index -= 1
      
    
    elif ch == curses.ascii.TAB:
      # handle tab completion ?
      self.append("<TAB>")
      
    elif ch == curses.ascii.NL or ch == curses.KEY_ENTER:
      # buffer and line cleaning done at beginning of listen()
      self.history.append(self.input_buffer)
      return self.input_buffer
  
  def stop(self):
    self.stopflag = True

  def refresh(self):
    self.win.refresh()
  
  def clear(self):
    self.win.erase()
    self.win.addstr(self.inputline_prefix)
    self.win.refresh()

  def append_ch(self, content):
    self.win.addch(content)
    self.input_buffer += content
    self.win.refresh()

  def append(self, content):
    self.win.addstr(content)
    self.input_buffer += content
    self.win.refresh()
  
  def println(self, content):
    self.clear()
    self.input_buffer = content
    self.addstr(self.input_buffer)
    self.refresh()

  def set_prefix(self, prefix):
    #if prefix != self.inputline_prefix:
    self.inputline_prefix = "[%s] " % prefix
    self.win.refresh()
