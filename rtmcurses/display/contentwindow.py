# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

import curses


class ContentWindow:
  def __init__(self):
    self.win = curses.newwin(curses.LINES-5, curses.COLS, 1, 0)
    
    self.win.bkgdset(ord(' '), curses.color_pair(1))
    self.win.insertln()

    self.win.refresh()

  def clear(self):
    self.win.addstr("<<< CLEAR >>>")
    self.refresh()
  
  def refresh(self):
    self.win.refresh()

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
    
    #~ self.win.move(1, 70)
    #~ self.win.addstr(' 1 ', curses.color_pair(2) | curses.A_BOLD)
    #~ 
    #~ self.win.addch(' ')
    #~ self.win.addch(curses.ACS_PI)
    #~ self.win.addch(' ')
    #~ self.win.addch(curses.ACS_RARROW)
    #~ self.win.addch(' ')
    #~ self.win.addch(curses.ACS_NEQUAL)
    #~ self.win.addch(' ')
    #~ self.win.addch(curses.ACS_LANTERN)
    #~ self.win.addch(' ')
    #~ self.win.addch(curses.ACS_DIAMOND)
    
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


  def println(self, msg=None):
    if msg is not None:
      self.win.addstr(msg+"\n")
      self.refresh()
