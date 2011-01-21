# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

import curses

class ContentWindow:
  
  def __init__(self):
    self._x = 0
    self._y = 0
    
    self.view_width  = curses.COLS
    self.view_height = curses.LINES-5
    self.total_width  = 2*curses.COLS
    self.total_height = curses.LINES-5
    
    self.win = curses.newpad(self.total_height, self.total_width)
    
    self.win.bkgdset(ord(' '), curses.color_pair(1))
    self.win.insertln()

    self.refresh()

  def clear(self):
    self.win.addstr("<<< CLEAR >>>")
    self.refresh()
  
  def refresh(self):
    self.win.refresh( self._y,self._x, 1,0, self.view_height-1,self.view_width-1 )

  def writetask(self):
    """test composite drawing of task"""
    title = "This is a task title"
    description = "And this is a task description with a few details\n because details are cool"
    date = "today, from 12:00 to 14:00"
    _x = 1
    _y = 1
    
    # title
    self.win.move(_y, _x)
    self.win.addch(' ', curses.color_pair(2))
    self.win.addch(' ', curses.color_pair(1))
    self.win.addstr(title, curses.A_BOLD)
   
    # date 
    _y += 1
    self.win.move(_y, _x)
    self.win.addch(' ', curses.color_pair(2))
    self.win.addch(' ', curses.color_pair(1))
    self.win.addch(curses.ACS_DIAMOND)
    self.win.addch(' ')
    self.win.addstr(date, curses.COLOR_RED)
    
    # description
    desc = description.split('\n')
    
    for desc_line in desc:
      _y += 1
      self.win.move(_y, _x)
      self.win.addch(' ', curses.color_pair(2))
      self.win.addstr('   ', curses.color_pair(1))
      self.win.addstr(desc_line.lstrip())
    
    self.refresh()

  def writetask2(self):
    """test composite drawing of task"""
    title = "This is another task title"
    description = "I love mon amoureuse\n c'est la meilleure amoureuse de la planete du monde entier"
    date = "today, from 12:00 to 14:00"
    _x = self.view_width+1
    _y = 1
    
    # title
    self.win.move(_y, _x)
    self.win.addch(' ', curses.color_pair(2))
    self.win.addch(' ', curses.color_pair(1))
    self.win.addstr(title, curses.A_BOLD)
    
    # date 
    _y += 1
    self.win.move(_y, _x)
    self.win.addch(' ', curses.color_pair(2))
    self.win.addch(' ', curses.color_pair(1))
    self.win.addch(curses.ACS_DIAMOND)
    self.win.addch(' ')
    self.win.addstr(date, curses.COLOR_RED)
    
    # description
    desc = description.split('\n')
    
    for desc_line in desc:
      _y += 1
      self.win.move(_y, _x)
      self.win.addch(' ', curses.color_pair(2))
      self.win.addstr('   ', curses.color_pair(1))
      self.win.addstr(desc_line.lstrip())
    
    self.refresh()

  def next(self):
    self._x = self.view_width
    self.refresh()
    
  def prev(self):
    self._x = 0
    self.refresh()

  def println(self, msg=None):
    if msg is not None:
      self.win.addstr(msg+"\n")
      self.refresh()
