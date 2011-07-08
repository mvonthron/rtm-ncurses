# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

import curses


class TitleLine:
  def __init__(self, lines, cols, y=0, x=0, content=None):
    """
    Create title bar

    The title bar has a simple decorative and help purpose
    """
    
    self.buffer = 'RTMilk'
    
    self.win = curses.newwin(lines, cols, y, x)

    self.win.bkgdset(ord(' '), curses.color_pair(2))
    self.win.insertln()
    self.win.addstr(0, 1, self.buffer)

    self.refresh()
    
  def refresh(self):
    self.win.refresh()

  def resize(self):
    del self.win
    self.win = curses.newwin(1, curses.COLS, 0, 0)

    self.win.bkgdset(ord(' '), curses.color_pair(2))
    self.win.insertln()
    self.win.addstr(0, 1, self.buffer)
    
    self.refresh()
    
    
