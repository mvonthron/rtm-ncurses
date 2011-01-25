# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

import curses


class StatusLine:
  
  def __init__(self):
    """
    Create status bar

    The status bar lists available channels
    """
    self.win = curses.newwin(1, curses.COLS, curses.LINES-2, 0)

    self.win.bkgdset(ord(' '), curses.color_pair(2))
    self.win.insertln()
    
    self.status   = "sleeping"
    self.viewlist = []
    self.colors   = {}
  
    self.refresh()

  def refresh(self):
    self.win.erase()
    
    self.win.addstr("(%s)" % self.status)
    for i, name in enumerate(self.viewlist):
      if name in self.colors:
        self.win.addstr(" [%d] %s" % (i, name), self.colors[name])
      else:
        self.win.addstr(" [%d] %s" % (i, name))
    
    self.win.refresh()

  def set_color(self, view, color):
    self.colors[view] = color
    self.refresh()

  def set_status(self, status):
    if status != self.status:
      self.status = status
      self.refresh()

  def fillFromViewlist(self, viewlist=None):
    if not viewlist is None:
      self.viewlist = viewlist

    self.refresh()
