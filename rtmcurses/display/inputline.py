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
  
  # characters is in this will be returned to main dispatcher rather
  # than be pre-processed with inputline's own parser
  throwable_char = [
    curses.ascii.DLE,
    curses.ascii.SO,
    curses.ascii.TAB,
    curses.KEY_RESIZE,
  ]
  
  def __init__(self, lines, cols, y, x):
    """
    Create input bar
    """
    MAX_HISTORY_SIZE = 20
    self.history = deque(maxlen=MAX_HISTORY_SIZE)
    self._history_index = MAX_HISTORY_SIZE-1
    
    self._clear_draw(lines, cols, y, x)


  def _clear_draw(self, lines, cols, y, x):
    self.win = curses.newwin(lines, cols, y, x)
    
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
    self.win.refresh()
    
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
    
    elif ch == curses.KEY_UP:
      self.append("<history>")
    
    elif ch in self.throwable_char:
      return ch
      
    elif ch == curses.ascii.NL or ch == curses.KEY_ENTER:
      _buff = self.input_buffer
      self.input_buffer = ""
      self.clear()      
      self.history.append(_buff)
     
      return _buff
  
  def stop(self):
    self.stopflag = True

  def refresh(self):
    self.win.refresh()
  
  def clear(self):
    self.win.erase()
    self.win.addstr(self.inputline_prefix + self.input_buffer)
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
    self.inputline_prefix = "[%s] " % prefix
    self.clear()
    # restoring input buffer
    #  self.win.addstr(self.input_buffer)
    self.refresh()
