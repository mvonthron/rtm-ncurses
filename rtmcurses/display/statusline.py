# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

import curses


class StatusLine:
  
  def __init__(self, disp_lines, disp_cols): # lines, cols, y, x):
    """
    Create status bar

    The status bar lists available channels
    """
    
    self.status   = "sleeping"
    self.viewlist = []
    self.colors   = {}
    
    self.disp_lines = disp_lines
    self.lines  = 1
    self.cols   = disp_cols
    self.y = disp_lines - (self.lines+1)
    self.x = 0
    
    self.win = curses.newwin(self.lines, self.cols, self.y, self.x)

    self.win.bkgdset(ord(' '), curses.color_pair(2))
    self.win.insertln()
    
    
    self.refresh()

  def refresh(self):
    self.win.erase()
    
    content = "(%s) " % self.status
    content += ' '.join("[%d] %s" % (i, name) for i, name in enumerate(self.viewlist))    
    
    self.lines = (len(content)/self.cols) + 1
    self.y = self.disp_lines - (self.lines+1)
    self.win.mvwin(self.y, self.x)
    self.win.resize(self.lines, self.cols)
    
    # we cannot reuse `content` since it doesn't handle colors
    self.win.addstr("(%s)" % self.status)
    current_len = len(self.status)+2
    for i, name in enumerate(self.viewlist):
      # keeping track of length already written so that we don't split a name
      current_len += len(" [%d] %s" % (i, name))
      if current_len < self.cols:
        if name in self.colors:
          self.win.addstr(" [%d] %s" % (i, name), self.colors[name])
        else:
          self.win.addstr(" [%d] %s" % (i, name))
      else:
        self.win.addstr("\n")
        current_len = 0
    
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
