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
    
    self.status = "sleeping"
  
    self.refresh()

  def refresh(self):
    self.win.refresh()

  def fillFromViewlist(self, viewlist):
    self.win.erase()
    
    self.win.addstr("(%s) " % self.status)
    self.win.addstr(' '.join(["[%d] %s" % (i, name) for i, name in enumerate(viewlist)]))

    self.refresh()
