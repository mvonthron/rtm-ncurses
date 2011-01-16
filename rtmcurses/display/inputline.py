# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

import curses
import curses.ascii
import time
import threading

class InputLine(object):
  
  _listening_thread = None
  _listening_stop = False
  
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


  # thread related methods
  def listen(self, decision=True):
    """start listening thread on input line
    if arg 'decision' set to False, the thread is stopped (if any)
    
    """
    if decision is True:
      """start listening tread"""
      self._listening_stop = False
      self._listening_thread = threading.Thread(target=self._listen_task)
      self._listening_thread.start()
      
    elif _listening_thread.is_alive():
      """stop listening thread"""
      self._listening_stop = True


  def _listen_task(self):
    """main listening routine
    listen to char entered by user with getch()
    """
    while self._listening_stop is not True:
      time.sleep(0.01)
      ch = self.win.getch()
      
      if -1 != ch:
        self.handle(ch)
        
  def handle(self, ch):
    need_refresh = False
    
    if ord('q') == ch:
      self._listening_stop = True
    
    if curses.ascii.isprint(ch):      
      self.win.addch(chr(ch))
      need_refresh = True
    
    if need_refresh:
      self.win.refresh()
