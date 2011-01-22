# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

import curses
import display

class ContentWindow:
  def __init__(self):
    self._x = 0
    self._y = 0
    
    self.view_height = curses.LINES-5
    self.view_width  = curses.COLS
    self.pad_height  = curses.LINES-5
    self.pad_width   = curses.COLS
    
    self.win = curses.newpad(self.pad_height, self.pad_width)
    
    self.win.bkgdset(ord(' '), curses.color_pair(1))
    self.win.insertln()

    self.refresh()

  def clear(self):
    self.win.addstr("<<< CLEAR >>>")
    self.refresh()
  
  def refresh(self, view_x=None, view_y=None):
    if view_x is None and view_y is None:
      self.win.refresh( self._y,self._x, 1,0, self.view_height-1,self.view_width-1 )
    else:
      self.win.refresh( view_y, view_x, 1,0, self.view_height-1, self.view_width-1 )

  def resize(self, _w, _h):
    pass

  def resize_pad(self, width=None, height=None):
    if not width is None:
      self.pad_width = width
    if not height is None:
      self.pad_height = height
    
    del self.win
    self.win = curses.newpad(self.pad_height, self.pad_width)


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

  def fillFromViews(self, views):
    self.win.erase()
    
    for v in views.itervalues():
      if not isinstance(v, display.View):
        raise Exception("invalid argument")
        
      row = v.y
      for line in v.buffer.split('\n'):
        self.win.addstr(row, v.x, line)
        row += 1

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
