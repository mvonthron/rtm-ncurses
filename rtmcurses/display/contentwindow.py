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

  def refresh(self):
    self.win.refresh()

  def println(self, msg):
    self.win.addstr(msg+'\n')
    self.refresh()
